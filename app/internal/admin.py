from fastapi import APIRouter,Depends,HTTPException
from ..database.schemas import CreateUser,UserDisplay,LoginUser
from ..database.models import User
from sqlalchemy.orm import Session
from ..dependencies import get_database
import random

router=APIRouter(
    tags=["admin"],
    prefix="/admin"
)

@router.post("/login")
async def admin_login(user_cred:LoginUser,db:Session=Depends(get_database)):
    user=db.query(User).filter(User.email==user_cred.email).first() 
    if not user:
        return {"message":"user does not exist."}
    elif  user.is_admin==False:
        return {"message":"user does not exist."}
    else:
        if user.password==user_cred.password:
            return {"message":"user logged in successfully","data":user}
        else:
             return {"message":"Incorrect Password."}
