from pydantic import BaseModel,EmailStr


class UserBase(BaseModel):
    email:EmailStr
    username:str
    is_admin:bool=False

class CreateUser(UserBase):
    password:str 

class LoginUser(BaseModel):
    email:EmailStr
    password:str 
    
class UserDisplay(UserBase):
    id:int

class ItemBase(BaseModel):
    name:str
    description:str
    price:float

class ItemCreate(ItemBase):
    pass 

class ItemDisplay(ItemBase):
    id:int





