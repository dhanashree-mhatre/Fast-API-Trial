from fastapi import APIRouter, Depends, HTTPException
from ..database.models import Item
from ..database.schemas import ItemCreate,ItemDisplay
from ..dependencies import get_database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/items")
async def add_items(item:ItemCreate,db:Session=Depends(get_database)):
    item_row=Item(**item.model_dump())
    db.add(item_row)
    db.commit()
    db.refresh(item_row)
    return item_row

@router.get("/")
async def read_items(db:Session=Depends(get_database)):
    items=db.query(Item).all()
    return items


@router.get("/{item_id}")
async def read_item(item_id: int,db:Session=Depends(get_database)):
    items=db.query(Item).filter(Item.id==item_id).first()
    if not items:
        return {"message":"Item not found"}
    return {"item":items }


@router.put(
    "/{item_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: int,name:str=None,description:str=None, db:Session=Depends(get_database)):
    items=db.query(Item).filter(Item.id==item_id).first()
    if not items:
        return {"message":"no item found with this id"}
    if name is not None:
        items.name=name
    if description is not None:
        items.description=description   
    db.commit()
    db.refresh(items)
    return {"message":"success"}