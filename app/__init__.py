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

@app.route('/nfl/worker/', methods=['POST'])
def worker():
    retries = 0
    game_lines = []
    while len(game_lines) == 0 and retries < 3:
        NFLScraper.fill_games()
        game_lines = NFLScraper.get_games_lines()
        retries += 1
    Game.update_lines(game_lines)
    return jsonify(game_lines)

@app.route('/nfl/fill/')
def fill():
    print("UPDATING")
    NFLScraper.fill_games()
    return jsonify(NFLScraper.get_games_lines()), 200

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