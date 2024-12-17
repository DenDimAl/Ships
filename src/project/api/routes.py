from tokenize import group
from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, status, Depends

from project.infrastructure.postgres.models import ScheduleOfGate
from project.infrastructure.postgres.repository.captain_repo import CaptainRepository
from project.infrastructure.postgres.repository.ship_repo import ShipRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.BrigadeSchema import BrigadeSchema
from project.schemas.CaptainSchema import CaptainSchema
from project.schemas.GateSchema import GateSchema
from project.schemas.LoaderSchema import LoaderSchema
from project.schemas.SupplierSchema import SupplierSchema
from project.schemas.ships import ShipSchema
from project.schemas.ClientSchema import ClientSchema
from project.schemas.CargoSchema import CargoSchema
from project.schemas.healthcheck import HealthCheckSchema
from project.schemas.PortSchema import PortSchema
from project.schemas.CraneSchema import CraneSchema
from project.schemas.RouteSchema import RouteSchema
from project.schemas.CruiseSchema import CruiseSchema
from project.schemas.OrderSchema import OrderSchema
from project.schemas.UserSchema import UserSchema, UserCreateUpdateSchema
from project.schemas.ScheduleOfGateSchema import ScheduleOfGateSchema
from project.core.exceptions import *
from project.api.depends import database, ship_repo, cap_repo, load_repo, client_repo, sup_repo, cargo_repo, brig_repo, \
    port_repo, crane_repo, gate_repo, route_repo, cruise_repo, order_repo, schedule_repo, user_repo, get_current_user, check_for_admin_access

from project.resource.auth import get_password_hash

router = APIRouter()

#Корабли______________________________________________________________________________________
@router.get("/all_ships", response_model=list[ShipSchema])
async def get_all_ships() -> list[ShipSchema]:

    async with database.session() as session:
        await ship_repo.check_connection(session=session)
        all_ships = await ship_repo.get_all_ships(session=session)

    return all_ships

@router.get("/ship/{ship_id}", response_model=ShipSchema, status_code=status.HTTP_200_OK)
async def get_ship_by_id(ship_id:int) -> ShipSchema:
    try:
        async with database.session() as session:
            ship = await ship_repo.get_ship_by_id(session=session, ship_id=ship_id)
    except ShipNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return ship

@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=status.HTTP_200_OK)
async def check_health() -> HealthCheckSchema:
    async with database.session() as session:
        db_is_ok = await ship_repo.check_connection(session=session)
    return HealthCheckSchema(
        db_is_ok=db_is_ok,
    )
@router.post("/add_ship", response_model=ShipSchema, status_code=status.HTTP_201_CREATED)
async def add_ship(
    ship_dto: ShipSchema,
) -> ShipSchema:
    try:
        async with database.session() as session:
            new_ship = await ship_repo.create_ship(session=session, ship=ship_dto)
    except ShipAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_ship


@router.put(
    "/update_ship/{ship_id}",
    response_model=ShipSchema,
    status_code=status.HTTP_200_OK,
)
async def update_ship(
    ship_id: int,
    ship_dto: ShipSchema,
) -> ShipSchema:
    try:
        async with database.session() as session:
            updated_ship = await ship_repo.update_ship(
                session=session,
                ship_id=ship_id,
                ship=ship_dto,
            )
    except ShipNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_ship


@router.delete("/delete_ship/{ship_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ship(
    ship_id: int,
) -> None:
    try:
        async with database.session() as session:
            ship = await ship_repo.delete_ship(session=session, ship_id=ship_id)
    except ShipNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return ship
#Капитаны___________________________________________________________________________________

@router.get("/get_all_captains", response_model=list[CaptainSchema])
async def get_all_captains() -> list[CaptainSchema]:

    async with database.session() as session:
        await cap_repo.check_connection(session=session)
        all_caps = await cap_repo.get_all_captains(session=session)

    return all_caps

@router.get("/get_captain_by_id", response_model=CaptainSchema, status_code=status.HTTP_200_OK)
async def get_captain_by_id(cap_pn:str) -> CaptainSchema:
    try:
        async with database.session() as session:
            cap = await cap_repo.get_captain_by_pn(session=session, cap_pn=cap_pn)
    except CaptainNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return cap

@router.post("/add_captain", response_model=CaptainSchema, status_code=status.HTTP_201_CREATED)
async def add_captain(
    cap_dto: CaptainSchema,
) -> CaptainSchema:
    try:
        async with database.session() as session:
            new_cap = await cap_repo.create_captain(session=session, captain=cap_dto)
    except CaptainAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_cap

@router.put(
    "/update_captain",
    response_model=CaptainSchema,
    status_code=status.HTTP_200_OK,
)
async def update_captain(
    cap_pn: str,
    cap_dto: CaptainSchema,
) -> CaptainSchema:
    try:
        async with database.session() as session:
            updated_cap = await cap_repo.update_captain(
                session=session,
                cap_pn=cap_pn,
                cap=cap_dto
            )
    except CaptainNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_cap

@router.delete("/delete_captain", status_code=status.HTTP_204_NO_CONTENT)
async def delete_captain(
    cap_pn: str,
) -> None:
    try:
        async with database.session() as session:
            cap = await cap_repo.delete_captain(session=session, cap_pn=cap_pn)
    except CaptainNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return cap
#Погрузчики____________________________________________________________________________________

@router.get("/get_all_loaders", response_model=list[LoaderSchema])
async def get_all_loaders() -> list[LoaderSchema]:

    async with database.session() as session:
        await load_repo.check_connection(session=session)
        all_loads = await load_repo.get_all_loaders(session=session)

    return all_loads

@router.get("/get_loader_by_id", response_model=LoaderSchema, status_code=status.HTTP_200_OK)
async def get_loader_by_id(load_pn:str) -> LoaderSchema:
    try:
        async with database.session() as session:
            load = await load_repo.get_loader_by_pn(session=session, load_pn=load_pn)
    except LoaderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return load

@router.post("/add_loader", response_model=LoaderSchema, status_code=status.HTTP_201_CREATED)
async def add_loader(
    load_dto: LoaderSchema,
) -> LoaderSchema:
    try:
        async with database.session() as session:
            new_load = await load_repo.create_loader(session=session, loader=load_dto)
    except LoaderAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_load

@router.put(
    "/update_loader",
    response_model=LoaderSchema,
    status_code=status.HTTP_200_OK,
)
async def update_loader(
    load_pn: str,
    load_dto: LoaderSchema,
) -> LoaderSchema:
    try:
        async with database.session() as session:
            updated_load = await load_repo.update_loader(
                session=session,
                load_pn=load_pn,
                load=load_dto
            )
    except LoaderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_load

@router.delete("/delete_loader", status_code=status.HTTP_204_NO_CONTENT)
async def delete_loader(
    load_pn: str,
) -> None:
    try:
        async with database.session() as session:
            load = await load_repo.delete_loader(session=session, load_pn=load_pn)
    except LoaderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return load
#Клиенты-------------------------------------------------------------------------------------------------------

@router.get("/get_all_clients", response_model=list[ClientSchema])
async def get_all_clients() -> list[ClientSchema]:

    async with database.session() as session:
        await client_repo.check_connection(session=session)
        all_clients = await client_repo.get_all_clients(session=session)

    return all_clients

@router.get("/get_client_by_fn", response_model=ClientSchema, status_code=status.HTTP_200_OK)
async def get_client_by_fn(client_fn:int) -> ClientSchema:
    try:
        async with database.session() as session:
            client = await client_repo.get_client_by_fn(session=session, client_fn=client_fn)
    except ClientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return client

@router.post("/add_client", response_model=ClientSchema, status_code=status.HTTP_201_CREATED)
async def add_client(
    client_dto: ClientSchema,
) -> ClientSchema:
    try:
        async with database.session() as session:
            new_client = await client_repo.create_client(session=session, client=client_dto)
    except ClientAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_client

@router.put(
    "/update_client",
    response_model=ClientSchema,
    status_code=status.HTTP_200_OK,
)
async def update_client(
    client_fn: int,
    client_dto: ClientSchema,
) -> ClientSchema:
    try:
        async with database.session() as session:
            updated_client = await client_repo.update_client(
                session=session,
                client_fn=client_fn,
                client=client_dto
            )
    except ClientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_client

@router.delete("/delete_client", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(
    client_fn: int,
) -> None:
    try:
        async with database.session() as session:
            client = await client_repo.delete_client(session=session, client_fn=client_fn)
    except ClientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return client
#Поставщики____________________________________________________________________________________________________

@router.get("/get_all_suppliers", response_model=list[SupplierSchema])
async def get_all_suppliers() -> list[SupplierSchema]:

    async with database.session() as session:
        await sup_repo.check_connection(session=session)
        all_sups = await sup_repo.get_all_suppliers(session=session)

    return all_sups

@router.get("/get_supplier_by_fn", response_model=SupplierSchema, status_code=status.HTTP_200_OK)
async def get_supplier_by_fn(sup_fn:int) -> SupplierSchema:
    try:
        async with database.session() as session:
            sup = await sup_repo.get_supplier_by_fn(session=session, supplier_fn=sup_fn)
    except SupplierNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return sup

@router.post("/add_supplier", response_model=SupplierSchema, status_code=status.HTTP_201_CREATED)
async def add_supplier(
    sup_dto: SupplierSchema,
) -> SupplierSchema:
    try:
        async with database.session() as session:
            new_supplier = await sup_repo.create_supplier(session=session, supplier=sup_dto)
    except SupplierAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_supplier

@router.put(
    "/update_supplier",
    response_model=SupplierSchema,
    status_code=status.HTTP_200_OK,
)
async def update_supplier(
    sup_fn: int,
    sup_dto: SupplierSchema,
) -> SupplierSchema:
    try:
        async with database.session() as session:
            updated_sup = await sup_repo.update_supplier(
                session=session,
                supplier_fn=sup_fn,
                supplier=sup_dto
            )
    except SupplierNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_sup

@router.delete("/delete_supplier", status_code=status.HTTP_204_NO_CONTENT)
async def delete_supplier(
    sup_fn: int,
) -> None:
    try:
        async with database.session() as session:
            sup = await sup_repo.delete_supplier(session=session, supplier_fn=sup_fn)
    except SupplierNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return sup
#Грузы___________________________________________________________________________________________________

@router.get("/get_all_cargos", response_model=list[CargoSchema])
async def get_all_cargos() -> list[CargoSchema]:

    async with database.session() as session:
        await cargo_repo.check_connection(session=session)
        all_cargos = await cargo_repo.get_all_cargos(session=session)

    return all_cargos

@router.get("/get_cargo_by_id", response_model=CargoSchema, status_code=status.HTTP_200_OK)
async def get_cargo_by_id(cargo_id:int) -> CargoSchema:
    try:
        async with database.session() as session:
            car = await cargo_repo.get_cargo_by_id(session=session, cargo_id=cargo_id)
    except CargoNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return car

@router.post("/add_cargo", response_model=CargoSchema, status_code=status.HTTP_201_CREATED)
async def add_cargo(
    car_dto: CargoSchema,
) -> CargoSchema:
    try:
        async with database.session() as session:
            new_cargo = await cargo_repo.create_cargo(session=session, supplier=car_dto)
    except CargoAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_cargo

@router.put(
    "/update_cargo",
    response_model=CargoSchema,
    status_code=status.HTTP_200_OK,
)
async def update_cargo(
    cargo_id: int,
    car_dto: CargoSchema,
) -> CargoSchema:
    try:
        async with database.session() as session:
            updated_car = await cargo_repo.update_cargo(
                session=session,
                cargo_id=cargo_id,
                cargo=car_dto
            )
    except CargoNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_car

@router.delete("/delete_cargo", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cargo(
    cargo_id: int,
) -> None:
    try:
        async with database.session() as session:
            car = await cargo_repo.delete_cargo(session=session, cargo_id=cargo_id)
    except CargoNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return car
#Бригады___________________________________________________________________________________________________

@router.get("/get_all_brigades", response_model=list[BrigadeSchema])
async def get_all_brigades() -> list[BrigadeSchema]:

    async with database.session() as session:
        await brig_repo.check_connection(session=session)
        all_brigades = await brig_repo.get_all_brigades(session=session)

    return all_brigades

@router.get("/get_brigade_by_id", response_model=BrigadeSchema, status_code=status.HTTP_200_OK)
async def get_brigade_by_id(brigade_id:int) -> BrigadeSchema:
    try:
        async with database.session() as session:
            brig = await brig_repo.get_brigade_by_id(session=session, brig_id=brigade_id)
    except BrigadeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return brig

@router.post("/add_brigade", response_model=BrigadeSchema, status_code=status.HTTP_201_CREATED)
async def add_brigade(
    brig_dto: BrigadeSchema,
) -> BrigadeSchema:
    try:
        async with database.session() as session:
            new_brig = await brig_repo.create_brigade(session=session, brigade=brig_dto)
    except BrigadeAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_brig

@router.put(
    "/update_brigade",
    response_model=BrigadeSchema,
    status_code=status.HTTP_200_OK,
)
async def update_brigade(
    brigade_id: int,
    brig_dto: BrigadeSchema,
) -> BrigadeSchema:
    try:
        async with database.session() as session:
            updated_brig = await brig_repo.update_brigade(
                session=session,
                brigade_id=brigade_id,
                brig=brig_dto
            )
    except BrigadeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_brig

@router.delete("/delete_brigade", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brigade(
    brig_id: int,
) -> None:
    try:
        async with database.session() as session:
            brig = await brig_repo.delete_brigade(session=session, brig_id=brig_id)
    except BrigadeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return brig
#Порты______________________________________________________________________________________________

@router.get("/get_all_ports", response_model=list[PortSchema])
async def get_all_ports() -> list[PortSchema]:

    async with database.session() as session:
        await port_repo.check_connection(session=session)
        all_ports = await port_repo.get_all_ports(session=session)

    return all_ports

@router.get("/get_port_by_id", response_model=PortSchema, status_code=status.HTTP_200_OK)
async def get_port_by_id(port_id:int) -> PortSchema:
    try:
        async with database.session() as session:
            port = await port_repo.get_port_by_id(session=session, port_id=port_id)
    except PortNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return port

@router.post("/add_port", response_model=PortSchema, status_code=status.HTTP_201_CREATED)
async def add_port(
    port_dto: PortSchema,
) -> PortSchema:
    try:
        async with database.session() as session:
            new_port = await port_repo.create_port(session=session, port=port_dto)
    except PortAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_port

@router.put(
    "/update_port",
    response_model=PortSchema,
    status_code=status.HTTP_200_OK,
)
async def update_port(
    port_id: int,
    port_dto: PortSchema,
) -> PortSchema:
    try:
        async with database.session() as session:
            updated_port = await port_repo.update_port(
                session=session,
                port_id=port_id,
                port=port_dto
            )
    except PortNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_port

@router.delete("/delete_port", status_code=status.HTTP_204_NO_CONTENT)
async def delete_port(
    port_id: int,
) -> None:
    try:
        async with database.session() as session:
            port = await port_repo.delete_port(session=session, port_id=port_id)
    except PortNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return port
#Краны_____________________________________________________________________________________________

@router.get("/get_all_cranes", response_model=list[CraneSchema])
async def get_all_cranes() -> list[CraneSchema]:

    async with database.session() as session:
        await crane_repo.check_connection(session=session)
        all_cranes = await crane_repo.get_all_cranes(session=session)

    return all_cranes

@router.get("/get_crane_by_id", response_model=CraneSchema, status_code=status.HTTP_200_OK)
async def get_crane_by_id(crane_id:int) -> CraneSchema:
    try:
        async with database.session() as session:
            crane = await crane_repo.get_crane_by_id(session=session, crane_id=crane_id)
    except CraneNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return crane

@router.post("/add_crane", response_model=CraneSchema, status_code=status.HTTP_201_CREATED)
async def add_crane(
    crane_dto: CraneSchema,
) -> CraneSchema:
    try:
        async with database.session() as session:
            new_crane = await crane_repo.create_crane(session=session, crane=crane_dto)
    except CraneAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_crane

@router.put(
    "/update_crane",
    response_model=CraneSchema,
    status_code=status.HTTP_200_OK,
)
async def update_crane(
    crane_id: int,
    crane_dto: CraneSchema,
) -> CraneSchema:
    try:
        async with database.session() as session:
            updated_crane = await crane_repo.update_crane(
                session=session,
                crane_id=crane_id,
                crane=crane_dto
            )
    except CraneNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_crane

@router.delete("/delete_crane", status_code=status.HTTP_204_NO_CONTENT)
async def delete_crane(
    crane_id: int,
) -> None:
    try:
        async with database.session() as session:
            crane = await crane_repo.delete_crane(session=session, crane_id=crane_id)
    except CraneNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return crane
#Доки_____________________________________________________________________________________________________

@router.get("/get_all_gates", response_model=list[GateSchema])
async def get_all_gates() -> list[GateSchema]:

    async with database.session() as session:
        await gate_repo.check_connection(session=session)
        all_gates = await gate_repo.get_all_gates(session=session)

    return all_gates

@router.get("/get_gate_by_id", response_model=GateSchema, status_code=status.HTTP_200_OK)
async def get_gate_by_id(gate_id:int) -> GateSchema:
    try:
        async with database.session() as session:
            gate = await gate_repo.get_gate_by_id(session=session, gate_id=gate_id)
    except GateNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return gate

@router.post("/add_gate", response_model=GateSchema, status_code=status.HTTP_201_CREATED)
async def add_gate(
    gate_dto: GateSchema,
) -> GateSchema:
    try:
        async with database.session() as session:
            new_gate = await gate_repo.create_gate(session=session, crane=gate_dto)
    except GateAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_gate

@router.put(
    "/update_gate",
    response_model=GateSchema,
    status_code=status.HTTP_200_OK,
)
async def update_gate(
    gate_id: int,
    gate_dto: GateSchema,
) -> GateSchema:
    try:
        async with database.session() as session:
            updated_gate = await gate_repo.update_gate(
                session=session,
                gate_id=gate_id,
                gate=gate_dto
            )
    except GateNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_gate

@router.delete("/delete_gate", status_code=status.HTTP_204_NO_CONTENT)
async def delete_gate(
    gate_id: int,
) -> None:
    try:
        async with database.session() as session:
            gate = await gate_repo.delete_gate(session=session, gate_id=gate_id)
    except GateNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return gate
#Маршруты________________________________________________________________________________________________

@router.get("/get_all_routes", response_model=list[RouteSchema])
async def get_all_routes() -> list[RouteSchema]:

    async with database.session() as session:
        await route_repo.check_connection(session=session)
        all_routes = await route_repo.get_all_routes(session=session)

    return all_routes

@router.get("/get_route_by_id", response_model=RouteSchema, status_code=status.HTTP_200_OK)
async def get_route_by_id(route_id:int) -> RouteSchema:
    try:
        async with database.session() as session:
            route = await route_repo.get_route_by_id(session=session, route_id=route_id)
    except RouteNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return route

@router.post("/add_route", response_model=RouteSchema, status_code=status.HTTP_201_CREATED)
async def add_route(
    route_dto: RouteSchema,
) -> RouteSchema:
    try:
        async with database.session() as session:
            new_route = await route_repo.create_route(session=session, crane=route_dto)
    except RouteAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_route

@router.put(
    "/update_route",
    response_model=RouteSchema,
    status_code=status.HTTP_200_OK,
)
async def update_route(
    route_id: int,
    route_dto: RouteSchema,
) -> RouteSchema:
    try:
        async with database.session() as session:
            updated_route = await route_repo.update_route(
                session=session,
                route_id=route_id,
                route=route_dto
            )
    except RouteNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_route

@router.delete("/delete_route", status_code=status.HTTP_204_NO_CONTENT)
async def delete_route(
    route_id: int,
) -> None:
    try:
        async with database.session() as session:
            route = await route_repo.delete_route(session=session, route_id=route_id)
    except RouteNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return route
#Круизы______________________________________________________________________________________________________

@router.get("/get_all_cruises", response_model=list[CruiseSchema])
async def get_all_cruises() -> list[CruiseSchema]:

    async with database.session() as session:
        await cruise_repo.check_connection(session=session)
        all_cruises = await cruise_repo.get_all_cruises(session=session)

    return all_cruises

@router.get("/get_cruise_by_id", response_model=CruiseSchema, status_code=status.HTTP_200_OK)
async def get_cruise_by_id(cruise_id:int) -> CruiseSchema:
    try:
        async with database.session() as session:
            cruise = await cruise_repo.get_cruise_by_id(session=session, cruise_id=cruise_id)
    except CruiseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return cruise

@router.post("/add_cruise", response_model=CruiseSchema, status_code=status.HTTP_201_CREATED)
async def add_cruise(
    cruise_dto: CruiseSchema,
) -> CruiseSchema:
    try:
        async with database.session() as session:
            new_cruise = await cruise_repo.create_cruise(session=session, cruise=cruise_dto)
    except CruiseAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_cruise

@router.put(
    "/update_cruise",
    response_model=CruiseSchema,
    status_code=status.HTTP_200_OK,
)
async def update_cruise(
    cruise_id: int,
    cruise_dto: CruiseSchema,
) -> CruiseSchema:
    try:
        async with database.session() as session:
            updated_cruise = await cruise_repo.update_cruise(
                session=session,
                cruise_id=cruise_id,
                cruise=cruise_dto
            )
    except CruiseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_cruise

@router.delete("/delete_cruise", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cruise(
    cruise_id: int,
) -> None:
    try:
        async with database.session() as session:
            cruise = await cruise_repo.delete_cruise(session=session, cruise_id=cruise_id)
    except CruiseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return cruise
#Заказы__________________________________________________________________________________________________________

@router.get("/get_all_cruises", response_model=list[CruiseSchema])
async def get_all_cruises() -> list[CruiseSchema]:

    async with database.session() as session:
        await cruise_repo.check_connection(session=session)
        all_cruises = await cruise_repo.get_all_cruises(session=session)

    return all_cruises

@router.get("/get_cruise_by_id", response_model=CruiseSchema, status_code=status.HTTP_200_OK)
async def get_cruise_by_id(cruise_id:int) -> CruiseSchema:
    try:
        async with database.session() as session:
            cruise = await cruise_repo.get_cruise_by_id(session=session, cruise_id=cruise_id)
    except CruiseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return cruise

@router.post("/add_cruise", response_model=CruiseSchema, status_code=status.HTTP_201_CREATED)
async def add_cruise(
    cruise_dto: CruiseSchema,
) -> CruiseSchema:
    try:
        async with database.session() as session:
            new_cruise = await cruise_repo.create_cruise(session=session, cruise=cruise_dto)
    except CruiseAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_cruise

@router.put(
    "/update_cruise",
    response_model=CruiseSchema,
    status_code=status.HTTP_200_OK,
)
async def update_cruise(
    cruise_id: int,
    cruise_dto: CruiseSchema,
) -> CruiseSchema:
    try:
        async with database.session() as session:
            updated_cruise = await cruise_repo.update_cruise(
                session=session,
                cruise_id=cruise_id,
                cruise=cruise_dto
            )
    except CruiseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_cruise

@router.delete("/delete_cruise", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cruise(
    cruise_id: int,
) -> None:
    try:
        async with database.session() as session:
            cruise = await cruise_repo.delete_cruise(session=session, cruise_id=cruise_id)
    except CruiseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return cruise
#Заказы_______________________________________________________________________________________________________

@router.get("/get_all_orders", response_model=list[OrderSchema])
async def get_all_orders() -> list[OrderSchema]:

    async with database.session() as session:
        await order_repo.check_connection(session=session)
        all_orders = await order_repo.get_all_orders(session=session)

    return all_orders

@router.get("/get_order_by_id", response_model=OrderSchema, status_code=status.HTTP_200_OK)
async def get_order_by_id(order_id:int) -> OrderSchema:
    try:
        async with database.session() as session:
            order = await order_repo.get_order_by_id(session=session, order_id=order_id)
    except OrderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return order

@router.post("/add_order", response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def add_order(
    order_dto: OrderSchema,
) -> OrderSchema:
    try:
        async with database.session() as session:
            new_order = await order_repo.create_order(session=session, order=order_dto)
    except OrderAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_order

@router.put(
    "/update_order",
    response_model=OrderSchema,
    status_code=status.HTTP_200_OK,
)
async def update_order(
    order_id: int,
    order_dto: OrderSchema,
) -> OrderSchema:
    try:
        async with database.session() as session:
            updated_order = await order_repo.update_order(
                session=session,
                order_id=order_id,
                order=order_dto
            )
    except OrderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_order

@router.delete("/delete_order", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order_id: int,
) -> None:
    try:
        async with database.session() as session:
            order = await order_repo.delete_order(session=session, order_id=order_id)
    except OrderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return order
#Расписания____________________________________________________________________________________________________

@router.get("/get_all_schedules", response_model=list[ScheduleOfGateSchema])
async def get_all_schedules() -> list[ScheduleOfGateSchema]:

    async with database.session() as session:
        await schedule_repo.check_connection(session=session)
        all_schedules = await schedule_repo.get_all_schedules(session=session)

    return all_schedules

@router.get("/get_schedule_by_id", response_model=ScheduleOfGateSchema, status_code=status.HTTP_200_OK)
async def get_schedule_by_id(schedule_id:int) -> ScheduleOfGateSchema:
    try:
        async with database.session() as session:
            schedule = await schedule_repo.get_schedule_by_id(session=session, schedule_id=schedule_id)
    except OrderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return schedule

@router.post("/add_schedule", response_model=ScheduleOfGateSchema, status_code=status.HTTP_201_CREATED)
async def add_schedule(
    schedule_dto: ScheduleOfGateSchema,
) -> ScheduleOfGateSchema:
    try:
        async with database.session() as session:
            new_schedule = await schedule_repo.create_schedule(session=session, schedule=schedule_dto)
    except ScheduleAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_schedule

@router.put(
    "/update_schedule",
    response_model=ScheduleOfGateSchema,
    status_code=status.HTTP_200_OK,
)
async def update_schedule(
    schedule_id: int,
    schedule_dto: ScheduleOfGateSchema,
) -> ScheduleOfGateSchema:
    try:
        async with database.session() as session:
            updated_schedule = await schedule_repo.update_schedule(
                session=session,
                schedule_id=schedule_id,
                schedule=schedule_dto
            )
    except ScheduleNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_schedule

@router.delete("/delete_schedule", status_code=status.HTTP_204_NO_CONTENT)
async def delete_schedule(
    schedule_id: int,
) -> None:
    try:
        async with database.session() as session:
            schedule = await schedule_repo.delete_schedule(session=session, schedule_id=schedule_id)
    except ScheduleNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return schedule

@router.get(
    "/all_users",
    response_model=list[UserSchema],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_current_user)],
)
async def get_all_users() -> list[UserSchema]:
    async with database.session() as session:
        all_users = await user_repo.get_all_users(session=session)

    return all_users


@router.get(
    "/user/{user_id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_current_user)],
)
async def get_user_by_id(
    user_id: int,
) -> UserSchema:
    try:
        async with database.session() as session:
            user = await user_repo.get_user_by_id(session=session, user_id=user_id)
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return user


@router.post(
    "/add_user",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_user(
    user_dto: UserCreateUpdateSchema,
    current_user: UserSchema = Depends(get_current_user),
) -> UserSchema:
    check_for_admin_access(user=current_user)
    try:
        async with database.session() as session:
            user_dto.password = get_password_hash(password=user_dto.password)
            new_user = await user_repo.create_user(session=session, user=user_dto)
    except UserAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_user


@router.put(
    "/update_user/{user_id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
)
async def update_user(
    user_id: int,
    user_dto: UserCreateUpdateSchema,
    current_user: UserSchema = Depends(get_current_user),
) -> UserSchema:
    check_for_admin_access(user=current_user)
    try:
        async with database.session() as session:
            user_dto.password = get_password_hash(password=user_dto.password)
            updated_user = await user_repo.update_user(
                session=session,
                user_id=user_id,
                user=user_dto,
            )
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_user


@router.delete(
    "/delete_user/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_id: int,
    current_user: UserSchema = Depends(get_current_user),
) -> None:
    check_for_admin_access(user=current_user)
    try:
        async with database.session() as session:
            user = await user_repo.delete_user(session=session, user_id=user_id)
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return user