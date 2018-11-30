import datetime
from app import db

class Spread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    points = db.Column(db.Float)
    favorite = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)