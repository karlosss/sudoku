from __future__ import print_function
import threading
import generator
from time import time
import gtk
import sys

zadani = [[],[],[]]
konec = False
start=time()

C = None
cislo = None


def generovani():
    global zadani
    while not konec:
        l = generator.generate(bf=False,limit=40)
        zadani[0].append(l)
        s = generator.generate(bf=False,limit=0)
        zadani[1].append(s)
        t = generator.generate(bf=True,limit=0)
        zadani[2].append(t)
        while len(zadani[0]) > 50 and not konec:
            pass

def gui():
    pass




t1 = threading.Thread(target=generovani)
t2 = threading.Thread(target=gui)

t1.start()
t2.start()

t1.join()
t2.join()


print("konec")
print(time()-start)

