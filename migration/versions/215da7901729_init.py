"""init

Revision ID: 215da7901729
Revises: 
Create Date: 2024-11-17 15:24:46.347438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '215da7901729'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ships',
    sa.Column('NumberOfShip', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=True),
    sa.Column('ShipType', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Speed', sa.Integer(), nullable=False),
    sa.Column('Spendings', sa.Integer(), nullable=False),
    sa.Column('FuelSpendings', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('NumberOfShip'),
    schema='my_app_schema'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ships', schema='my_app_schema')
    # ### end Alembic commands ###
