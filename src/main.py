from fastapi import FastAPI

from .api.routes import router

app = FastAPI(title="Clean API Example", version="1.0")

app.include_router(router)
