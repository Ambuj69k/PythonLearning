"""
decorators ko samjhne ke liye hum aise samjh sakte hai ki ek toll
 jaisa hota hai ki koi bhi request ho pehle decorators ke through jayegi 
 aur agar hume usme koi changes karna hua to hum kar sakte hai simply
"""

"""ab isko example ke through samjhte hai 
write a decorator that measures the time a function takes to execute
"""

# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start= time.time()
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(f"{func.__name__} ran in {end-start}")
#         return result
#     return wrapper
# @timer
# def example_function(n):
#     time.sleep(n)
#     print("executed")


# example_function(2)


"""
create a decorator to print the fucntion name and the values 
of its arguments every time the function is called
"""

def FunctionDecorator(func):
    def wrapper(*args):
        result=func(*args)
        functionname=func.__name__
        values=args

        print(f"funtion name is {functionname} and the values are {values} and length of arguments is {len(values)}")
        return result
    return wrapper

@FunctionDecorator
def add(a,b)->int:
    return a+b

add(2,3)



"""implement decorator that chaches the return values of a function , so that when its called with the same arguments , the cached value is returned instead of re-executing the function"""