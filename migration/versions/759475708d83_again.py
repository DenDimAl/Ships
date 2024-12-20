"""again

Revision ID: 759475708d83
Revises: 
Create Date: 2024-12-04 16:38:01.562025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from project.core.config import settings


# revision identifiers, used by Alembic.
revision: str = '759475708d83'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('captains',
    sa.Column('personnel_number', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('fio', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('paycheck', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('personnel_number'),
    schema='my_app_schema'
    )
    op.create_table('cargos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cargo_type', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('volume', sa.Integer(), nullable=False),
    sa.Column('containments', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('delivery_cost', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('clients',
    sa.Column('face_number', sa.Integer(), nullable=False),
    sa.Column('name_of_the_firm', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('accompalience_date', sa.DateTime(), nullable=True),
    sa.Column('state_or_private', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('face_number'),
    schema='my_app_schema'
    )
    op.create_table('loaders',
    sa.Column('personnel_number', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('fio', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('responsobility', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('paycheck', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('personnel_number'),
    schema='my_app_schema'
    )
    op.create_table('ports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('town', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('month_spendings', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('ships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=True),
    sa.Column('ship_type', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('max_volume', sa.Integer(), nullable=False),
    sa.Column('max_weight', sa.Integer(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.Column('spendings', sa.Integer(), nullable=False),
    sa.Column('fuel_spendings', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('suppliers',
    sa.Column('face_number', sa.Integer(), nullable=False),
    sa.Column('name_of_the_firm', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('accompalience_date', sa.DateTime(), nullable=True),
    sa.Column('state_or_private', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('face_number'),
    schema='my_app_schema'
    )
    op.create_table('brigades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_brigade', sa.Integer(), nullable=False),
    sa.Column('signed_employee', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.ForeignKeyConstraint(['signed_employee'], ['my_app_schema.loaders.personnel_number'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('cranes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('port_number', sa.Integer(), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=False),
    sa.Column('month_spendings', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['port_number'], ['my_app_schema.ports.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('gates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_in_port', sa.Integer(), nullable=False),
    sa.Column('number_of_port', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['number_of_port'], ['my_app_schema.ports.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_starting_port', sa.Integer(), nullable=False),
    sa.Column('number_of_ending_port', sa.Integer(), nullable=False),
    sa.Column('route_length', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['number_of_ending_port'], ['my_app_schema.ports.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_starting_port'], ['my_app_schema.ports.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('cruises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('awaiting_date_of_start', sa.DateTime(), nullable=False),
    sa.Column('awaiting_date_of_end', sa.DateTime(), nullable=False),
    sa.Column('actual_date_of_start', sa.DateTime(), nullable=False),
    sa.Column('actual_date_of_end', sa.DateTime(), nullable=False),
    sa.Column('ship', sa.Integer(), nullable=False),
    sa.Column('captain', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('type_of_cargo', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('number_of_route', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['captain'], ['my_app_schema.captains.personnel_number'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_route'], ['my_app_schema.routes.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ship'], ['my_app_schema.ships.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_cargo', sa.Integer(), nullable=False),
    sa.Column('number_of_client', sa.Integer(), nullable=False),
    sa.Column('number_of_supplier', sa.Integer(), nullable=False),
    sa.Column('date_of_ordering', sa.DateTime(), nullable=False),
    sa.Column('awaiting_date_of_receiving', sa.DateTime(), nullable=False),
    sa.Column('actual_date_of_receiving', sa.DateTime(), nullable=False),
    sa.Column('awaiting_date_of_deliviring', sa.DateTime(), nullable=False),
    sa.Column('actual_date_of_deliviring', sa.DateTime(), nullable=False),
    sa.Column('number_of_cruise', sa.Integer(), nullable=False),
    sa.Column('cost_of_delivery', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['number_of_cargo'], ['my_app_schema.cargos.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_client'], ['my_app_schema.clients.face_number'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_cruise'], ['my_app_schema.cruises.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_supplier'], ['my_app_schema.suppliers.face_number'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    op.create_table('scheduleofgate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_served_cruise', sa.Integer(), nullable=False),
    sa.Column('number_of_gate', sa.Integer(), nullable=False),
    sa.Column('number_of_port', sa.Integer(), nullable=False),
    sa.Column('number_of_brigade', sa.Integer(), nullable=False),
    sa.Column('awaiting_date_of_start', sa.DateTime(), nullable=False),
    sa.Column('awaiting_date_of_end', sa.DateTime(), nullable=False),
    sa.Column('actual_date_of_start', sa.DateTime(), nullable=False),
    sa.Column('actual_date_of_end', sa.DateTime(), nullable=False),
    sa.Column('up_or_down', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['number_of_brigade'], ['my_app_schema.brigades.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_gate'], ['my_app_schema.gates.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_port'], ['my_app_schema.ports.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['number_of_served_cruise'], ['my_app_schema.cruises.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='my_app_schema'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scheduleofgate', schema='my_app_schema')
    op.drop_table('orders', schema='my_app_schema')
    op.drop_table('cruises', schema='my_app_schema')
    op.drop_table('routes', schema='my_app_schema')
    op.drop_table('gates', schema='my_app_schema')
    op.drop_table('cranes', schema='my_app_schema')
    op.drop_table('brigades', schema='my_app_schema')
    op.drop_table('suppliers', schema='my_app_schema')
    op.drop_table('ships', schema='my_app_schema')
    op.drop_table('ports', schema='my_app_schema')
    op.drop_table('loaders', schema='my_app_schema')
    op.drop_table('clients', schema='my_app_schema')
    op.drop_table('cargos', schema='my_app_schema')
    op.drop_table('captains', schema='my_app_schema')
    # ### end Alembic commands ###
