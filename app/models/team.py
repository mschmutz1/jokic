import datetime
from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120))
    name = db.Column(db.String(120))
    abr = db.Column(db.String(120))
    conf = db.Column(db.String(120))
    div = db.Column(db.String(120))
    games_favorite = db.relationship('Game', foreign_keys='Game.team_1_id', backref='team_1', lazy='dynamic')
    games_underdog = db.relationship('Game', foreign_keys='Game.team_2_id', backref='team_2', lazy='dynamic')

    def to_string(self):
        return '{} {}'.format(self.city, self.name)

    def __repr__(self):
        return '<{} {}>'.format(self.city, self.name)

    def __eq__(self, other):
        if isinstance(other, basestring):
            return '{} {}'.format(self.city, self.name) == other
        else:
            return False

    @classmethod
    def find_team(cls, team_name):
        split_name = team_name.split(' ')
        if len(split_name) != 2:
            split_name[0:2] = [' '.join(split_name[0:2])]
        loc, name = split_name
        return Team.query.filter(Team.city == loc).filter(Team.name == name).first()
