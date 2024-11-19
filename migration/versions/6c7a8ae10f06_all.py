"""all

Revision ID: 6c7a8ae10f06
Revises: 215da7901729
Create Date: 2024-11-20 01:39:57.665888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c7a8ae10f06'
down_revision: Union[str, None] = '215da7901729'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('captains',
    sa.Column('PersonnelNumber', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Fio', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Experience', sa.Integer(), nullable=True),
    sa.Column('Paycheck', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('PersonnelNumber'),
    schema='my_app_schema'
    )
    op.create_table('cargos',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('CargoType', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Volume', sa.Integer(), nullable=False),
    sa.Column('Containments', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Weight', sa.Integer(), nullable=False),
    sa.Column('DeliveryCost', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    schema='my_app_schema'
    )
    op.create_table('clients',
    sa.Column('FaceNumber', sa.Integer(), nullable=False),
    sa.Column('NameOfTheFirm', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('AccompalienceDate', sa.DateTime(), nullable=True),
    sa.Column('StateOrPrivate', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('FaceNumber'),
    schema='my_app_schema'
    )
    op.create_table('loaders',
    sa.Column('PersonnelNumber', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Fio', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Responsobility', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('Experience', sa.Integer(), nullable=True),
    sa.Column('Paycheck', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('PersonnelNumber'),
    schema='my_app_schema'
    )
    op.create_table('ports',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Town', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('MonthSpendings', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    schema='my_app_schema'
    )
    op.create_table('suppliers',
    sa.Column('FaceNumber', sa.Integer(), nullable=False),
    sa.Column('NameOfTheFirm', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('AccompalienceDate', sa.DateTime(), nullable=True),
    sa.Column('StateOrPrivate', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('FaceNumber'),
    schema='my_app_schema'
    )
    op.create_table('brigades',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('NumberOfBrigade', sa.Integer(), nullable=False),
    sa.Column('SignedEmployee', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.ForeignKeyConstraint(['SignedEmployee'], ['my_app_schema.loaders.PersonnelNumber'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Id'),
    schema='my_app_schema'
    )
    op.create_table('cranes',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('PortNumber', sa.Integer(), nullable=False),
    sa.Column('Experience', sa.Integer(), nullable=False),
    sa.Column('MonthSpendings', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['PortNumber'], ['my_app_schema.ports.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Id'),
    schema='my_app_schema'
    )
    op.create_table('gates',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('NumberInPort', sa.Integer(), nullable=False),
    sa.Column('NumberOfPort', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['NumberOfPort'], ['my_app_schema.ports.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Id'),
    schema='my_app_schema'
    )
    op.create_table('routes',
    sa.Column('NumberOfRoute', sa.Integer(), nullable=False),
    sa.Column('NumberOfStartingPort', sa.Integer(), nullable=False),
    sa.Column('NumberOfEndingPort', sa.Integer(), nullable=False),
    sa.Column('RouteLength', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['NumberOfEndingPort'], ['my_app_schema.ports.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfStartingPort'], ['my_app_schema.ports.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('NumberOfRoute'),
    schema='my_app_schema'
    )
    op.create_table('cruises',
    sa.Column('NumberOfCruise', sa.Integer(), nullable=False),
    sa.Column('AwaitingDateOfStart', sa.DateTime(), nullable=False),
    sa.Column('AwaitingDateOfEnd', sa.DateTime(), nullable=False),
    sa.Column('ActualDateOfStart', sa.DateTime(), nullable=False),
    sa.Column('ActualDateOfEnd', sa.DateTime(), nullable=False),
    sa.Column('Ship', sa.Integer(), nullable=False),
    sa.Column('Captain', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('TypeOfCargo', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('NumberOfRoute', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Captain'], ['my_app_schema.captains.PersonnelNumber'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfRoute'], ['my_app_schema.routes.NumberOfRoute'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['Ship'], ['my_app_schema.ships.NumberOfShip'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('NumberOfCruise'),
    schema='my_app_schema'
    )
    op.create_table('orders',
    sa.Column('NumberOfOrder', sa.Integer(), nullable=False),
    sa.Column('NumberOfCargo', sa.Integer(), nullable=False),
    sa.Column('NumberOfClient', sa.Integer(), nullable=False),
    sa.Column('NumberOfSupplier', sa.Integer(), nullable=False),
    sa.Column('DateOfOrdering', sa.DateTime(), nullable=False),
    sa.Column('AwaitingDateOfReceiving', sa.DateTime(), nullable=False),
    sa.Column('ActualDateOfReceiving', sa.DateTime(), nullable=False),
    sa.Column('AwaitingDateOfDeliviring', sa.DateTime(), nullable=False),
    sa.Column('ActualDateOfDeliviring', sa.DateTime(), nullable=False),
    sa.Column('NumberOfCruise', sa.Integer(), nullable=False),
    sa.Column('CostOfDelivery', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['NumberOfCargo'], ['my_app_schema.cargos.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfClient'], ['my_app_schema.clients.FaceNumber'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfCruise'], ['my_app_schema.cruises.NumberOfCruise'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfSupplier'], ['my_app_schema.suppliers.FaceNumber'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('NumberOfOrder'),
    schema='my_app_schema'
    )
    op.create_table('scheduleofgate',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('NumberOfServedCruise', sa.Integer(), nullable=False),
    sa.Column('NumberOfGate', sa.Integer(), nullable=False),
    sa.Column('NumberOfPort', sa.Integer(), nullable=False),
    sa.Column('NumberOfBrigade', sa.Integer(), nullable=False),
    sa.Column('AwaitingDateStart', sa.DateTime(), nullable=False),
    sa.Column('AwaitingDateOfEnd', sa.DateTime(), nullable=False),
    sa.Column('ActualDateOfStart', sa.DateTime(), nullable=False),
    sa.Column('ActualDateOfEnd', sa.DateTime(), nullable=False),
    sa.Column('UpOrDown', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['NumberOfBrigade'], ['my_app_schema.brigades.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfGate'], ['my_app_schema.gates.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfPort'], ['my_app_schema.ports.Id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['NumberOfServedCruise'], ['my_app_schema.cruises.NumberOfCruise'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Id'),
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
    op.drop_table('ports', schema='my_app_schema')
    op.drop_table('loaders', schema='my_app_schema')
    op.drop_table('clients', schema='my_app_schema')
    op.drop_table('cargos', schema='my_app_schema')
    op.drop_table('captains', schema='my_app_schema')
    # ### end Alembic commands ###