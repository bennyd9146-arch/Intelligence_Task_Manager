from database import agent_db
from fastapi import APIRouter ,HTTPException


router_agent = APIRouter(prefix="/agents")

@router_agent.post("/")
def r_create_agent(body:dict):
    agent_db.create_agent(body)


@router_agent.get("/")
def r_get_all_agents():
    agent_db.all_get_agents()


@router_agent.get("/{id}")
def r_get_all_agents_by_id(id:int):
    agent_db.get_agent_by_id(id)


@router_agent.put("/{id}")
def r_update_agent(id:int,body):
    agent_db.updete_agent(id,body)


# @router_agent.put("/{id}/deactivate")
# def agent_deactivate():
    