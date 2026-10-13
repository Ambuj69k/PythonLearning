"""
simply iterators jo hai list, tuple,string
jaise data type ko iterator me convert karta hai 
ab ye kya karta hai sipmly next element ek ek karke 
return karta hai for loop bhi internally iteraotrs ka hi use karte hai 
next element find karne ke liye next() ya obj __next__ ka use karek hum nikal sakte
hai next value sabse important ye hai ki 
agar last value ke baad hum firse iterator call karte hai to simply wo 
stopiteration ka exception through karta hai 
"""


liss=[2,3,4]

aj=iter(liss)

print(next(aj))
print(next(aj))
print(next(aj))
print(next(aj))