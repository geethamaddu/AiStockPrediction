from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Multi Agent stock prediction system", version="2.0.0")
app.include_router(router)