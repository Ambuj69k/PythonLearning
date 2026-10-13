"""
ab sql supported model banane ke liye hume class ko base se inherit karwana padega 
aur wo base jo hoga wo object hoga declarative_base() ka jo ki hum sql alchemy.ext.declarative se import karenge
ab isse humara orm hogaya now 
hum main.py me jaake batayenge ki sqlalchemy please create a table for us
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import Mapped,mapped_column
Base=declarative_base()
class Product(Base):
    __tablename__="Product"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)


"""
migration file generate karne ke liye mapped column use karna padta hai
 jo ki sqlalchemy.orm me hai 

 from sqlalchemy.orm import Mapped , mapped_column
 """
class employee(Base):
    __tablename__='Employee'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column()
    email:Mapped[str]=mapped_column()