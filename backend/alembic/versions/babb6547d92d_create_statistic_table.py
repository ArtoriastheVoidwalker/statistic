"""

Revision ID: babb6547d92d
Revises: 
Create Date: 2022-06-13 15:05:18.185625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'babb6547d92d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('statistic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('view', sa.Integer(), nullable=False),
    sa.Column('click', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('cpc', sa.Float(), nullable=False),
    sa.Column('cpm', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_statistic_id'), 'statistic', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_statistic_id'), table_name='statistic')
    op.drop_table('statistic')
    # ### end Alembic commands ###
