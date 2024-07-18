from typing import Annotated
from .database.models import SessionLocal 
from fastapi import Header, HTTPException




#database
async def get_database():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()

    