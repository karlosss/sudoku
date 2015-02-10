#encoding: utf8
from __future__ import unicode_literals

def sameChars(string):
    pole = []
    for i in string:
        if i in pole:
            return True
        else:
            pole.append(i)
    return False

def arr2str(array):
    string = ""
    for i in array:
        string = string + str(i)
    return string

def str2arr(string):
    arr = []
    for i in string:
        arr.append(int(i))
    return arr

def num2alpha(n):
    if n == 0:
        return "A"
    if n == 1:
        return "B"
    if n == 2:
        return "C"
    if n == 3:
        return "D"
    if n == 4:
        return "E"
    if n == 5:
        return "F"
    if n == 6:
        return "G"
    if n == 7:
        return "H"
    if n == 8:
        return "I"
    return False

def alpha2num(char):
    char = str(char)
    if char.lower() == "a":
        return 0
    if char.lower() == "b":
        return 1
    if char.lower() == "c":
        return 2
    if char.lower() == "d":
        return 3
    if char.lower() == "e":
        return 4
    if char.lower() == "f":
        return 5
    if char.lower() == "g":
        return 6
    if char.lower() == "h":
        return 7
    if char.lower() == "i":
        return 8
    return -1

def hms(integer):

    h = divmod(integer,3600)
    zbytek = h[1]
    h = h[0]
    m = divmod(zbytek,60)
    s = m[1]
    m = m[0]

    h = str(h)
    if m < 10:
        m = "0"+str(m)
    else:
        m = str(m)

    if s < 10:
        s = "0"+str(s)
    else:
        s = str(s)


    return "Čas: "+h+":"+m+":"+s

