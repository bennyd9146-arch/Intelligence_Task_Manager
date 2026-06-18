from fastapi  import FastAPI
import uvicorn
from routes import agent_routes

app = FastAPI()
app.include_router(agent_routes.router_agent)
@app.get("/")
def root():
    return {"massege" : "wellcom" }

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
