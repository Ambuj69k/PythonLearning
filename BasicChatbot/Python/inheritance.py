##inheritance 
##car class blueprint


class Car:
    def __init__(self,windows,doors,engine):
        self.windows=windows
        self.doors=doors
        self.engine=engine

    def driving(self):
        print("car is driving")

class Audi(Car):
    def __init__(self,windows,doors,engine,horsepower):
        """hume upar ki saaari properties inherit karne ke liye super ka use karna padeta hai 
        simply super keywork. __init__ and simply jo hum inherit karna hai uska naam likh te hai
        then wo properties simply humare paas aa gyi"""
        super().__init__(windows,doors,engine)
        self.horsepower=horsepower

car1=Car(4,4,"V6")

audi1=Audi(4,4,"V6",400)

print(audi1.windows)
print(audi1.doors)
print(audi1.engine)
print(audi1.horsepower)
print(car1.windows)
print(car1.doors)
print(car1.engine)

print(id(car1))
print(id(audi1))
audi1.driving()