from fastapi import FastAPI
from routes.expresses_routes import express_api_router

app = FastAPI()

app.include_router(express_api_router)
