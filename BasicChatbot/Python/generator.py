"""
generator ka main idea hai saari value ko ek sath memorly me load karne ki jagah jaisa ki 
list karta hai ye kya karta hai jab zaroorat pade to hi value generate karta hai 
yield keyword use karte hai isko iterator bhi bol sakte ho but ye python ke through banta hai
agar humko custom iterator banana hai to basically kya hota hai simply 
hume iter function jo ki object return karta hai and next function chaiye so python ne kya bola
mai bana dunga but isko hum generator bolenge
"""


def funct():
    yield 1
    yield 2
    yield 3

on=funct()
print(next(on))

print(next(on))
print(next(on))
print(next(on))