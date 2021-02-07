"""add health data

Revision ID: db27ff0e56d1
Revises: 
Create Date: 2021-02-07 13:09:38.022552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db27ff0e56d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('health',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('county', sa.Text(), nullable=True),
    sa.Column('state_code', sa.Integer(), nullable=True),
    sa.Column('county_code', sa.Integer(), nullable=True),
    sa.Column('year_span', sa.Text(), nullable=True),
    sa.Column('measure_name', sa.Text(), nullable=True),
    sa.Column('measure_id', sa.Integer(), nullable=True),
    sa.Column('numerator', sa.Float(), nullable=True),
    sa.Column('denominator', sa.Float(), nullable=True),
    sa.Column('raw_value', sa.Float(), nullable=True),
    sa.Column('confidence_interval_lower_bound', sa.Float(), nullable=True),
    sa.Column('confidence_interval_upper_bound', sa.Float(), nullable=True),
    sa.Column('date_release_year', sa.Integer(), nullable=True),
    sa.Column('fipscode', sa.Integer(), nullable=True),
    sa.Column('dt_updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('health')
    # ### end Alembic commands ###