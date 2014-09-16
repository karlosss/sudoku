from tkinter import *
from time import time
start = time()


raw = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,9,0,0,0,0,0],
[0,3,0,7,1,0,0,0,0],
[7,0,0,2,4,0,0,3,0],
[0,1,2,0,0,0,8,5,0],
[0,8,0,0,5,6,0,0,7],
[0,0,0,0,3,1,0,8,0],
[8,9,0,0,6,0,0,0,0],
[0,0,1,0,0,0,6,0,0]
]



final = []

for i in range(0,9,1):
    line = []
    for j in range(0,9,1):
        line.append(raw[j][i])
    final.append(line)

raw = final



candidates = {}


def stage1(cand):
    """vygenerovani kandidatu pro vsechny policka, podle zadani (zadane cislo uz ma jen jednoho kandidata)"""
    for i in range(0,9,1):
        for j in range(0,9,1):
            if raw[i][j] != 0:
                candidates[i,j] = [raw[i][j]]
            else:
                candidates[i,j] = [1,2,3,4,5,6,7,8,9]

    return cand






def stage2(cand):
    """vycisteni radku, sloupcu a ctvercu - zakladni pravidla sudoku"""
    for i in range(0,9,1):
        for j in range(0,9,1):
            if len(cand[i,j]) == 1: #pokud je nejake policko jednoznacne, tak...

                for k in range(0,9,1): #...vycisti sloupec od toho cisla...
                    if j == k: #ale nesmaz si to zadane :)
                        continue
                    try: #obcas tam to cislo uz chybi, tak mi nevyhazuj chyby
                        cand[i,k].remove(cand[i,j][0])
                    except:
                        pass

                for k in range(0,9,1): #...vycisti sloupec od toho cisla...
                    if i == k: #ale nesmaz si to zadane :)
                        continue
                    try: #obcas tam to cislo uz chybi, tak mi nevyhazuj chyby
                        cand[k,j].remove(cand[i,j][0])
                    except:
                        pass

                ctverec = zjisti_ctverec(i,j) #...zjisti, ve kterem ctverci se nachazi...
                for k in range(0,3,1):
                    for l in range(0,3,1):
                        if [k+(3*ctverec[0]),l+(3*ctverec[1])] == [i,j]:#...probehni vsechna cisla, ktera v tomto ctverci jsou...
                            continue
                        try:
                            cand[k+(3*ctverec[0]),l+(3*ctverec[1])].remove(cand[i,j][0]) #...a vyskrtej ty, ktere se shoduji
                        except:
                            pass


    return cand




def unikatni_cislo(cand):
    """strategie: policka 12, 12 a 125, je jasne, ve kterem bude petka"""
    for i in range(0,9,1): #sloupce
        vyskyt = [0,0,0,0,0,0,0,0,0]
        for j in range(0,9,1):
            for k in range(1,10,1):
                for l in range(0,len(cand[i,j]),1):
                    if cand[i,j][l] == k:
                        vyskyt[k-1] = vyskyt[k-1] + 1

        for m in range(0,9,1):
            if vyskyt[m] == 1:
                for n in range(0,9,1):
                    if m+1 in cand[i,n]:
                        cand[i,n] = [m+1]

    for i in range(0,9,1): #radky
        vyskyt = [0,0,0,0,0,0,0,0,0]
        for j in range(0,9,1):
            for k in range(1,10,1):
                for l in range(0,len(cand[j,i]),1):
                    if cand[j,i][l] == k:
                        vyskyt[k-1] = vyskyt[k-1] + 1

        for m in range(0,9,1):
            if vyskyt[m] == 1:
                for n in range(0,9,1):
                    if m+1 in cand[n,i]:
                        cand[n,i] = [m+1]

    for i in range(0,3,1):
        for j in range(0,3,1):
            vyskyt = [0,0,0,0,0,0,0,0,0]
            for k in range(0,3,1):
                for l in range(0,3,1):
                    for m in range(1,10,1):
                        for n in range(0,len(cand[i*3+k,j*3+l]),1):
                            if cand[i*3+k,j*3+l][n] == m:
                                vyskyt[m-1] = vyskyt[m-1] + 1

        for o in range(0,9,1):
            if vyskyt[o] == 1:
                for p in range(0,3,1):
                    for q in range(0,3,1):
                        if o+1 in cand[i*3+p,j*3+q]:
                            cand[i*3+p,j*3+q] = [o+1]




    return cand









def zjisti_ctverec(x,y):
    """zjisteni ctverce, ve kterem se dane cislo nachazi"""
    if x < 3:
        sx = 0
    if x >= 3 and x < 6:
        sx = 1
    if x >= 6:
        sx = 2
    if y < 3:
        sy = 0
    if y >= 3 and y < 6:
        sy = 1
    if y >= 6:
        sy = 2
    return [sx,sy]


def vykresli(cand):
    """vykresleni kandidatu pro kazde policko do tabulky"""
    global C
    for i in range(0,9,1):
        for j in range(0,9,1):
            C.create_text(i*80+10,j*80+10, anchor="nw", text=cand[i,j], font="arial 7")


candidates = stage1(candidates)
candidates = stage2(candidates)
candidates = stage2(candidates)
candidates = stage2(candidates)
candidates = stage2(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)
candidates = stage2(candidates)
candidates = unikatni_cislo(candidates)



okno = Tk()
okno.minsize(810,810)
okno.maxsize(810,810)
okno.resizable(0,0)

C = Canvas(okno, width=810, height=810, bg="#ffffff")
C.place(x=0,y=0)

for i in range(0,10,1):
    if i in (1,2,4,5,7,8):
        C.create_rectangle(5,i*80+5,726,i*80+6, outline="#aaaaaa")
    else:
        C.create_rectangle(5,i*80+5,726,i*80+6)

    if i in(1,2,4,5,7,8):
        C.create_rectangle(i*80+5,5,i*80+6,726, outline="#aaaaaa")
    else:
        C.create_rectangle(i*80+5,5,i*80+6,726)

vykresli(candidates)
print(time()-start)
okno.mainloop()
