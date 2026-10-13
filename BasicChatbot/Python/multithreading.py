"""
lets learn like this supppose hum ek restaurant me gye aur ek pizza order kiya
ek burger kiya aur ek coffee order ki now 
agr hum traditional way dekhe kya hoga pehle kitchen me pizza banaya ab lets suppose 
pizza banaane me 5s laga aur burger banaya burger banane me 3 second lage 1 second me
let say coffee bana di ab in total 9 second lag gaye what 
if agar hum pizza ko oven me daalte hi burger making and coffee machine start kar de to
humara saara kaam 5 second me ho jayega exactly this way hume 
api calls me hote hai ho sakta hai multiple db calls hai har ek call ko 
5 second lag rhe hai aur synchronously karne gaye to latency ka provlem aayega isko hum resolve call
ko simultaneously execute karke kar sakte hai uske liye hume jyada kuch nhi karna hota 
hai 
ye hum multithreading se bhi kar sakte hai achieve and asynchronous se bhi kar sakte hai 
dono ke alag tarike hai same kaam karne ka 

now sabse pehele ek chij dekhte hai jisko hum concurrency kehte hai 
concurrency : multiple kaam ko is tarike se manage karna ki unki progress overlap ho sake

parllelism : muliple task litreally ek hi time pe execute hona jaise ki multiple cpu cores

sequential execution: ek task khatam hone ke baad doosra start hona 


multithreading : imagine karte hai ek office me 3 employee hai har employee apna task handle kar sakte hai 
process= ek running program
thread=  us process ke andar execution ka ek path, jo doosre thread ke saath resources share kar sakte hai 

multiple threading me multipe thread use karke multipe tasks ko manage kar sakte hai

"""

# import time 
# import threading
# def tasks(name):
#     print(f"{name} started")
#     time.sleep(2)
#     print(f"{name} completed")

# # tasks("task one")
# # tasks("task two")
# # tasks("task three")


# t1=threading.Thread(target=tasks,args=("task1",))
# t2=threading.Thread(target=tasks,args=("thask2",))
# t3=threading.Thread(target=tasks,args=("task3",))

# t1.start()
# t2.start()
# t3.start()
"""
pehle kya ho rha tha saara task main thread hi execute kar rha tha ab humne kya kiya 
main thread se workload hata ke 3 different thread start kiya jiska kaam simply
kya hai 3 ek timpe pe hi dekhe task start kiya and 2 second ka pause leke 3no ne saath me execute kar liya 
now samjho maine ek aur print kar diya like print hi then according the execution order hum dekhe to usse kya karna chaiye simply
"""

"""aisa kyu hota hai simply hume main thread ko batana hota hai ki jab tak saare thread execute na 
ho jaate hai tab tak wait kare aur wo hum particulalry join ka use karke batate hai 
thread.join()"""

# t1.join()
# t2.join()
# t3.join()

print("hello ji")

"""asynchronous programming kya hoti hai 
ab imagine karo ki tum ek employee ho and you are very smart ab main idea kya hai 
suppose ek kaam karne me 2 second lage to kya tum un 2 second khaali baithe rahoge kya nhi na 
tum doosra task execute karna start kar doge and jab pehle task ka response aa jayega to simply us task ko continue kar loge 
jab ek task kisi awaited operation ka wait kar rha ho to event loop doosre eligible tasks ko progress karne ka mauka de sakta hai 
 python me hum commonly asyncio , async aur await ka use karte hai """

import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} completed")


"""agar hum async function ko jab call karte hai to hume coroutine object milta hai function turant execute nhi hota
ye asynchronous ke andar kisi awaitable operation ka wait karta hai. is wait ke dauraan eventloop doosre task kl run kar sakta hai

"""

asyncio.run(task("name"))