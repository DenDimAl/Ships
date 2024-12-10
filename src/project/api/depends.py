from project.infrastructure.postgres.repository.ship_repo import ShipRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.infrastructure.postgres.repository.captain_repo import CaptainRepository
from project.infrastructure.postgres.repository.loader_repo import LoaderRepository
from project.infrastructure.postgres.repository.client_repo import ClientRepository
from project.infrastructure.postgres.repository.supplier_repo import SupplierRepository
from project.infrastructure.postgres.repository.cargo_repo import CargoRepository
from project.infrastructure.postgres.repository.brigade_repo import BrigadeRepository
from project.infrastructure.postgres.repository.port_repo import PortRepository
from project.infrastructure.postgres.repository.crane_repo import CraneRepository
from project.infrastructure.postgres.repository.gate_repo import GateRepository
from project.infrastructure.postgres.repository.route_repo import RouteRepository
from project.infrastructure.postgres.repository.cruise_repo import CruiseRepository
from project.infrastructure.postgres.repository.order_repo import OrderRepository
from project.infrastructure.postgres.repository.scheduleofgate_repo import ScheduleRepository
schedule_repo = ScheduleRepository()
order_repo = OrderRepository()
cruise_repo = CruiseRepository()
route_repo = RouteRepository()
gate_repo = GateRepository()
crane_repo = CraneRepository()
port_repo = PortRepository()
brig_repo = BrigadeRepository()
cargo_repo = CargoRepository()
sup_repo = SupplierRepository()
client_repo = ClientRepository()
load_repo = LoaderRepository()
ship_repo = ShipRepository()
cap_repo = CaptainRepository()
database = PostgresDatabase()