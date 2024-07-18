from sqlalchemy import create_engine,Column,Integer,String,Boolean,Float
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sqlalchemy.orm



database_url="sqlite:///./database.db"
engine=create_engine(database_url)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=sqlalchemy.orm.declarative_base()

class User(Base):
    __tablename__="users"
    id=Column(Integer,index=True,primary_key=True)
    email=Column(String,unique=True)
    username=Column(String,unique=True)
    password=Column(String)
    is_admin=Column(Boolean,default=False)

class Item(Base):
    __tablename__="items"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    description=Column(String,nullable=True)
    price=Column(Float,nullable=False)

Base.metadata.create_all(bind=engine)