from flask import Flask
from flask import jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import psycopg2
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models.week import Week
from app.models.game import Game
from app.models.spread import Spread
from app.models.team import Team
from app.NFLScraper import NFLScraper

@app.route('/')
def hello_world():
    return "Hello word"

@app.route('/nfl/fill/')
def fill():
    print("UPDATING")
    NFLScraper.fill_games()
    print("DONE")
    return jsonify(NFLScraper.get_games_lines())

@app.route('/nfl/get_lines/')
def index():
    return jsonify(NFLScraper.get_games_lines())

@app.route('/nfl/update_lines/')
def update_lines():
    Game.update_lines(NFLScraper.get_games_lines())
    return jsonify(NFLScraper.get_games_lines())

@app.route('/nfl/current_week/')
def current_week():
    return str(Week.get_current_week())