"""
is file me hum connection string simply use karke data se connect karenge
sabse pehle hume sessionmaker lana hoga jo ki hume sqlalchemy.orm se milta hai 
ab hum local ke session banate hai right 
now session banate hai localy data base se connect karne ke liye 
ab usme kuch arguments hote hai wo hume dene hote hai 
jaie autocommit hum isko intially false rakhenge kyu ki simply
hum manually commit karenge 
autoflush false rakhenge and simly bind= engine dena hota hai engine simpy 
kya karta hai connection banata hai db ke saath create_engine() isme 
hume db_url dena hota hai iske baad simply 
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
db_url=os.getenv("DATABASE_URL")
engine=create_engine(db_url)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

