from fastapi import APIRouter ,HTTPException
from database import mission_db,agent_db

router_mission = APIRouter(prefix="/missions")

@router_mission.post()
def create_mission(body:dict):
    mission_db.create_mission(body)


@router_mission.get()
def get_all_missions():
    mission_db.get_all_missions()


@router_mission.get("/{id}")
def get_mission_by_id(id:int):
    mission_db.get_mission_by_id(id)
    