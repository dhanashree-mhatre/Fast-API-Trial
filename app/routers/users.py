from fastapi import APIRouter,Depends,HTTPException
from ..database.schemas import CreateUser,UserDisplay,LoginUser
from ..database.models import User
from sqlalchemy.orm import Session
from ..dependencies import get_database
router=APIRouter(
    tags=["users"],
    prefix="/user"
)

@router.get('/users/')
def get_users(db:Session=Depends(get_database)):
    users=db.query(User).all()
    if not users:
        raise HTTPException(status_code=404,detail="No one have registered yet.")
    return users

@router.post('/')
async def read_user_me(user:CreateUser,db:Session=Depends(get_database)):
    email_check = db.query(User).filter(User.email ==user.email or User.username==user.username).first() 
    if email_check!=None:
        return {"message":"user does not exist."}
    else:
        try:
            user_row=User(**user.model_dump())
            db.add(user_row)
            db.commit()
            db.refresh(user_row)
        except:
            raise HTTPException(status_code=419, detail="Internal error")
        return {"message":"user registered successfully","data":user_row}
    

@router.post('/login')
async def user_login(user_cred:LoginUser,db:Session=Depends(get_database)):
    user=db.query(User).filter(User.email==user_cred.email).first() 
    if not user:
        return {"message":"user does not exist."}
    else:
        if user.password==user_cred.password:
            return {"message":"user logged in successfully","data":user}
        else:
             return {"message":"Incorrect Password."}






           