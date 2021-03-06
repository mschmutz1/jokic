"""empty message

Revision ID: 7e2615d56d64
Revises: d167e6e59591
Create Date: 2018-11-26 21:45:14.003596

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from datetime import timedelta


# revision identifiers, used by Alembic.
revision = '7e2615d56d64'
down_revision = 'd167e6e59591'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    teams_table = op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('abr', sa.String(length=120), nullable=True),
    sa.Column('conf', sa.String(length=120), nullable=True),
    sa.Column('div', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    week_table = op.create_table('week',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('week_number', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_1_id', sa.Integer(), nullable=True),
    sa.Column('team_2_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('score_team_1', sa.Integer(), nullable=True),
    sa.Column('score_team_2', sa.Integer(), nullable=True),
    sa.Column('week_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_1_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['team_2_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['week_id'], ['week.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spread',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('points', sa.Float(), nullable=True),
    sa.Column('favorite', sa.Boolean(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    insert_json = []
    end_date = datetime.strptime('20 Nov 2018', '%d %b %Y')
    for week_number in range(12, 22):
        date = end_date
        end_date = date + timedelta(days=7)
        week_hash = {
            'year': 2018,
            'week_number': week_number,
            'start_date': date,
            'end_date': end_date
        }
        insert_json.append(week_hash)

    op.bulk_insert(week_table, insert_json)

    op.bulk_insert(teams_table,
                   [
                       {
                           "city": "Arizona",
                           "name": "Cardinals",
                           "abr": "ARI",
                           "conf": "NFC",
                           "div": "West"
                       },
                       {
                           "city": "Atlanta",
                           "name": "Falcons",
                           "abr": "ATL",
                           "conf": "NFC",
                           "div": "South"
                       },
                       {
                           "city": "Baltimore",
                           "name": "Ravens",
                           "abr": "BAL",
                           "conf": "AFC",
                           "div": "North"
                       },
                       {
                           "city": "Buffalo",
                           "name": "Bills",
                           "abr": "BUF",
                           "conf": "AFC",
                           "div": "EAST"
                       },
                       {
                           "city": "Carolina",
                           "name": "Panthers",
                           "abr": "CAR",
                           "conf": "NFC",
                           "div": "South"
                       },
                       {
                           "city": "Cincinnati",
                           "name": "Bengals",
                           "abr": "CIN",
                           "conf": "AFC",
                           "div": "North"
                       },
                       {
                           "city": "Chicago",
                           "name": "Bears",
                           "abr": "CIN",
                           "conf": "NFC",
                           "div": "North"
                       },
                       {
                           "city": "Cleveland",
                           "name": "Browns",
                           "abr": "CLE",
                           "conf": "AFC",
                           "div": "North"
                       },
                       {
                           "city": "Dallas",
                           "name": "Cowboys",
                           "abr": "DAL",
                           "conf": "NFC",
                           "div": "East"
                       },
                       {
                           "city": "Denver",
                           "name": "Broncos",
                           "abr": "DEN",
                           "conf": "AFC",
                           "div": "West"
                       },
                       {
                           "city": "Detroit",
                           "name": "Lions",
                           "abr": "DET",
                           "conf": "NFC",
                           "div": "North"
                       },
                       {
                           "city": "Green Bay",
                           "name": "Packers",
                           "abr": "GB",
                           "conf": "NFC",
                           "div": "North"
                       },
                       {
                           "city": "Houston",
                           "name": "Texans",
                           "abr": "HOU",
                           "conf": "AFC",
                           "div": "South"
                       },
                       {
                           "city": "Indianapolis",
                           "name": "Colts",
                           "abr": "IND",
                           "conf": "AFC",
                           "div": "South"
                       },
                       {
                           "city": "Jacksonville",
                           "name": "Jaguars",
                           "abr": "JAX",
                           "conf": "AFC",
                           "div": "South"
                       },
                       {
                           "city": "Kansas City",
                           "name": "Chiefs",
                           "abr": "KC",
                           "conf": "AFC",
                           "div": "West"
                       },
                       {
                           "city": "Miami",
                           "name": "Dolphins",
                           "abr": "MIA",
                           "conf": "AFC",
                           "div": "East"
                       },
                       {
                           "city": "Minnesota",
                           "name": "Vikings",
                           "abr": "MIN",
                           "conf": "AFC",
                           "div": "North"
                       },
                       {
                           "city": "New England",
                           "name": "Patriots",
                           "abr": "NE",
                           "conf": "AFC",
                           "div": "East"
                       },
                       {
                           "city": "New Orleans",
                           "name": "Saints",
                           "abr": "NO",
                           "conf": "NFC",
                           "div": "South"
                       },
                       {
                           "city": "New York",
                           "name": "Giants",
                           "abr": "NYG",
                           "conf": "NFC",
                           "div": "East"
                       },
                       {
                           "city": "New York",
                           "name": "Jets",
                           "abr": "NYJ",
                           "conf": "AFC",
                           "div": "East"
                       },
                       {
                           "city": "Oakland",
                           "name": "Raiders",
                           "abr": "OAK",
                           "conf": "AFC",
                           "div": "West"
                       },
                       {
                           "city": "Philadelphia",
                           "name": "Eagles",
                           "abr": "PHI",
                           "conf": "NFC",
                           "div": "East"
                       },
                       {
                           "city": "Pittsburgh",
                           "name": "Steelers",
                           "abr": "PIT",
                           "conf": "AFC",
                           "div": "North"
                       },
                       {
                           "city": "Los Angeles",
                           "name": "Chargers",
                           "abr": "SD",
                           "conf": "AFC",
                           "div": "West"
                       },
                       {
                           "city": "Seattle",
                           "name": "Seahawks",
                           "abr": "SEA",
                           "conf": "NFC",
                           "div": "West"
                       },
                       {
                           "city": "San Francisco",
                           "name": "49ers",
                           "abr": "SF",
                           "conf": "NFC",
                           "div": "West"
                       },
                       {
                           "city": "Los Angeles",
                           "name": "Rams",
                           "abr": "STL",
                           "conf": "NFC",
                           "div": "West"
                       },
                       {
                           "city": "Tampa Bay",
                           "name": "Buccaneers",
                           "abr": "TB",
                           "conf": "NFC",
                           "div": "South"
                       },
                       {
                           "city": "Tennessee",
                           "name": "Titans",
                           "abr": "TEN",
                           "conf": "AFC",
                           "div": "South"
                       },
                       {
                           "city": "Washington",
                           "name": "Redskins",
                           "abr": "WAS",
                           "conf": "NFC",
                           "div": "East"
                       }
                   ])
    # ### end Alembic commands ###


def downgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###

    # ### end Alembic commands ###
