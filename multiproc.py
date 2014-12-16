import time
from multiprocessing import Process
from multiprocessing.sharedctypes import Value, Array
from ctypes import c_bool, c_int, c_wchar_p

def func():
    for i in range(100):
        time.sleep(0.01)
        v[0] += 1

def func2():
    for i in range(10000,100000,1000):
        time.sleep(0.03)
        print(i)
    print("ahoj!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    v[1] = 200
    for i in v:
        print i
    a = "lokalni promenna"
    print(a)
    print b.value
    print s.value



v = Array(c_int, [1,2,3,4,5])
b = Value(c_bool, True)
s = Value(c_wchar_p, "asdf")

p = Process(target=func)
p.start()
p2 = Process(target=func2)
p2.start()








