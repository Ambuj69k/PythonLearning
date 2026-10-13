"""
classes,constructor,attributes,methods

classes are blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data."""

class Car:
    def __init__(self,model,year,type):
        self.model=model
        self.year=year
        self.type=type

    def __init__(self,model,year,type,color):
        self.model=model
        self.year=year
        self.type=type
        self.color=color


car1=Car("Toyota",2020,"Sedan","yellow")

print(car1.model)


"""
simply question ye hai ki hum python me simply multiple constructors bana sakte hai kya 
and answer hai nhi kyu ki python me multiple constructors nhi hote hai but hum default arguments ka use karke multiple constructors ka effect create kar sakte hai"""


