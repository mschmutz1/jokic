import datetime
from datetime import timedelta
from app import db

class Week(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, default=2018)
    week_number = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)
    games = db.relationship('Game', backref='week', lazy='dynamic')

    @classmethod
    def get_current_week(cls, time):
        return Week.query.filter(Week.start_date <= time).filter(Week.end_date >= time).first()