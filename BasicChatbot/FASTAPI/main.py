from fastapi import FastAPI,Depends
from models import Product
from database import SessionLocal,engine
import database_models
from sqlalchemy.orm import Session
app=FastAPI()

# database_models.Base.metadata.create_all(bind=engine)

@app.get('/')
def welcome():
    return "welcome buddy to my broken world"

"""
pydantic is use for simply for data validation 
if we are want to send the data to server in json format then 
we generally use pydantic
"""
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
products=[
    Product(id=1,name="phone",description="budget friendly phone",price=9999,quantity=10),
    Product(id=2,name="laptop",description="budget friendly laptop",price=590,quantity=10),
    Product(id=3,name="T.V",description="budget friendly t.v",price=5032,quantity=10),
    Product(id=4,name="Earbuds",description="budget friendly earbuds",price=349,quantity=10),
    Product(id=5,name="WashingMachine",description="budget friendly washingmaching",price=1000,quantity=10)
]


"""
we are writing a function which will simply add all the value from here to posgres
"""

def init__db():
    db=SessionLocal()
    """
    simply pehle hum cound of table check karenge then simply add karenge

    """
    count=0
    count=db.query(database_models.Product).count()
    if count==0:
        for prouct in products:
            db.add(database_models.Product(**prouct.model_dump()))
        db.commit()
    db.close()

init__db()
@app.get('/products')
def get_all_products(db:Session=Depends(get_db)):

    """
    instead of inrepository value ab hume kya chaiye simply
    hume database se value chaiye 
    uske liye pehle
    hume connection chaiye,
    query jo hum use karenge query karne ke liye
    """
    db_products=db.query(database_models.Product).all()
    # db=SessionLocal()
    # db.query()
    return db_products

"""
now simply jab hume id ke base pe get karna hota hai product fast api me 
to hum simply 
{} ke base pe karte hai means is brace ke andar jo hum accept karne waale hai 
wo daalna hota hai and same name se hume argument accept karna hota hai then uska 
data type deke hum usko use kar sakte hai 
"""

@app.get("/product/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
    product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if product:
        return product
    return "product not found"
    # for product in products:
    #     if product.id==id:
    #         return product
    #     else:
    #         return "product not found" 

"""
for posting the data like getting by id we donot have to use {} in route we simply 
accept the argument for which we need to create a data simply nothing more than that
now what we have to do is simply
we will do the same
"""

@app.post('/Product')
def add_product(product:Product,db:Session=Depends(get_db)):
    product_exist=db.query(database_models.Product).filter(database_models.Product.id==product.id).first()
    if product_exist:
         return "product already exist you can not add this product"

    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return "product added successfully"
    # if product.id!=0:
    #     products.append(product)
    #     return "producted added sucessfully"
    # else:
    #     return "invalid product"

@app.put("/product")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    exist_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()

    if exist_product:
        """
        for updating the simple value we need to do one thing only we just need to update the value 
        of existing value then we need to commit simply """
        exist_product.id=product.id
        exist_product.name=product.name
        exist_product.quantity=product.quantity
        exist_product.price=product.price
        exist_product.description=product.description
        db.commit()
        return "product updated successfully"
    # for i in range(len(products)):
    #     if products[i].id==id:
    #         products[i]=product
    #         return "product updated sucessfully"
    return f"product with {id} is not exist in db"

@app.delete("/product/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if product:
        db.delete(product)
        db.commit()
        return "product deleted successfully"
    # for i in range(len(products)):
    #     if products[i].id==id:
    #         products.pop(i)
    #         return "product deleted sucessfully"

    return f"product with {id} does not exist in the database"

"""
for dealing with database like in c# we used entity framework core for orm 
here we are using sql alchmey which is also providing a orm in python based backend 
"""


"""
now hum dependency injection kaise karte hai wo dekhenge
simply hum jo bhi inject karna hai usko
simply Session() variable me daalenge simply 
aur ek chij import karna padta hai fastapi se Depends ye kya karta hai 
simply batata hai ki ye object yaha inject 
karna hai
argument me simply db:Session=Depends(method which we wnat to inject)"""

