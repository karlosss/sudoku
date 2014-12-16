import threading
from time import sleep

promenna = 0

def a():
    global promenna
    for i in range(30):
        sleep(0.3)
        promenna = promenna + 1
        print(promenna)

def b():
    global promenna
    for j in range(10000,10030,1):
        sleep(0.2)
        promenna = promenna + 1
        print(promenna)



t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)

t1.start()
t2.start()

t1.join()
t2.join()

print("")
print()
print(promenna)

