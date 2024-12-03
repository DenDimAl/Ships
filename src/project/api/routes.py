from tokenize import group
from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, status

from project.infrastructure.postgres.repository.captain_repo import CaptainRepository
from project.infrastructure.postgres.repository.ship_repo import ShipRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.CaptainSchema import CaptainSchema
from project.schemas.ships import ShipSchema
from project.schemas.healthcheck import HealthCheckSchema
from project.core.exceptions import *
from project.api.depends import database, ship_repo, cap_repo


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
            ship = await ship_repo.delete_user(session=session, ship_id=ship_id)
    except ShipNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return ship
#Капитаны___________________________________________________________________________________


@router.get("/all_captains", response_model=list[CaptainSchema])
async def get_all_caps() -> list[CaptainSchema]:

    async with database.session() as session:
        await cap_repo.check_connection(session=session)
        all_caps = await cap_repo.get_all_captains(session=session)

    return all_caps

@router.get("/get_captain_by_pn/{cap_pn}", response_model=CaptainSchema, status_code=status.HTTP_200_OK)
async def get_cap_by_pn(cap_pn:str) -> CaptainSchema:
    try:
        async with database.session() as session:
            cap = await cap_repo.get_captain_by_pn(session=session, cap_pn=cap_pn)
    except CaptainNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=error.message)
    return cap

@router.post("/add_captain", response_model=ShipSchema, status_code=status.HTTP_201_CREATED)
async def add_captain(
    captain: CaptainSchema,
) -> CaptainSchema:
    try:
        async with database.session() as session:
            new_cap = await cap_repo.create_captain(session=session, captain=captain)
    except ShipAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_cap


@router.put(
    "/update_captain/{captain_pn}",
    response_model=ShipSchema,
    status_code=status.HTTP_200_OK,
)
async def update_captain(
    cap_pn: str,
    cap_dto: CaptainSchema,
) -> ShipSchema:
    try:
        async with database.session() as session:
            updated_cap = await cap_repo.update_captain(
                session=session,
                cap_pn=cap_pn,
                cap=cap_dto,
            )
    except CaptainNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_cap


@router.delete("/delete_ship/{ship_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_captain(
    cap_pn: str,
) -> None:
    try:
        async with database.session() as session:
            cap = await cap_repo.delete_cap(session=session, cap_pn=cap_pn)
    except CaptainNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return cap
