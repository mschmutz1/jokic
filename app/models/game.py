import datetime
from app import db
from app.models.team import Team
from app.models.spread import Spread
from app.models.week import Week

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_1_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_2_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    date = db.Column(db.DateTime)
    score_team_1 = db.Column(db.Integer)
    score_team_2 = db.Column(db.Integer)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
    spreads = db.relationship('Spread', backref='game', lazy='dynamic', order_by="desc(Spread.created_date)", primaryjoin="Spread.game_id==Game.id")

    @classmethod
    def update_lines(cls, game_lines):
        if len(game_lines) == 0:
            return

        for new_game in game_lines:
            game_found = False

            current_week = Week.get_current_week(new_game['Date'])
            games = current_week.games
            previous_game_entry = None

            for existing_game in games:
                if existing_game.team_1.to_string() == new_game['Favorite'] or existing_game.team_1.to_string() == new_game['Underdog']:
                    if existing_game.team_2.to_string() == new_game['Favorite'] or existing_game.team_2.to_string() == new_game['Underdog']:
                        game_found = True
                        favorite = existing_game.team_1.to_string() == new_game['Favorite']
                        previous_game_entry = existing_game
                        break

            if not game_found:
                print(new_game['Favorite'])
                print(new_game['Underdog'])
                game = Game(date = new_game['Date'],
                            team_1_id = Team.find_team(new_game['Favorite']).id,
                            team_2_id = Team.find_team(new_game['Underdog']).id,
                            week_id = current_week.id)
                db.session.add(game)
                db.session.flush()
                spread = Spread(game_id = game.id, points = new_game['Line'], favorite = True)
                db.session.add(spread)
            else:
                old_spread = previous_game_entry.spreads.first()
                if old_spread.points != float(new_game['Line']) or not favorite:
                    spread = Spread(game_id=previous_game_entry.id, points=new_game['Line'], favorite=favorite)
                    db.session.add(spread)

        current_week.last_updated = datetime.datetime.now()
        db.session.add(current_week)
        db.session.commit()
