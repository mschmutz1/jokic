"""games table

Revision ID: 8b4d8fd6009a
Revises: ef52bffbb991
Create Date: 2018-11-22 14:49:58.051886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b4d8fd6009a'
down_revision = 'ef52bffbb991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###