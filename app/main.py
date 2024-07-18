from fastapi import FastAPI
from .routers import items,users
from .internal import admin
from .database import models
app=FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(admin.router)

@app.get('/')
def root():
    return {"message":"hello world"}

