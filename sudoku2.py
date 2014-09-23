from tkinter import *
from time import time
from copy import deepcopy
start = time()

#druhy commit

raw = [
[0,0,0,0,5,8,2,3,7],
[0,0,0,0,0,0,1,0,0],
[3,0,0,0,1,0,0,0,8],
[0,0,2,7,4,0,0,0,0],
[4,0,8,5,2,9,6,0,1],
[0,0,0,0,6,3,4,0,0],
[2,0,0,0,8,0,0,0,6],
[0,0,1,0,0,0,0,0,0],
[9,6,7,2,3,0,0,0,0]
]

##raw = [
##[1,2,3,4,5,6,7,8,9],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0]
##]


def kontrola_vstupu(vstup):
    if len(vstup) != 9:
        print("neplatny vstup")
        exit()
    for i in vstup:
        if len(i) != 9:
            print("neplatny vstup")
            exit()
        for j in i:
            if j not in range(0,10,1):
                print("neplatny vstup")
                exit()

def generate_candidates(template):
    cand = [
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]]
    ]
    for i in range(0,9,1):
        for j in range(0,9,1):
            if template[j][i] == 0:
                cand[j][i] = [1,2,3,4,5,6,7,8,9]
            else:
                cand[j][i] = [raw[j][i]]
    return cand

def pravidlova_zkouska(cand):
    for i in range(0,9,1):
        removeRadek = []
        removeSloupec = []
        removeCtverec = []
        dm = divmod(i,3)

        for j in range(0,9,1):
            if len(cand[i][j]) == 1:
                removeRadek.append(cand[i][j][0])
            if len(cand[j][i]) == 1:
                removeSloupec.append(cand[j][i][0])

            dm2 = divmod(j,3)
            x = dm[1]*3+dm2[1]
            y = dm[0]*3+dm2[0]
            if len(cand[x][y]) == 1:
                removeCtverec.append(cand[x][y][0])

        for j in range(1,10,1):
            if removeRadek.count(j) > 1 or removeCtverec.count(j) > 1 or removeSloupec.count(j) > 1:
                if PrvniKontrola == False:
                    return False
                else:
                    print("sudoku nema reseni")
                    exit()


        for j in range(0,9,1):
            for kandidat in removeRadek:
                if kandidat in cand[i][j] and len(cand[i][j]) > 1:
                        cand[i][j].remove(kandidat)


            for kandidat in removeSloupec:
                if kandidat in cand[j][i] and len(cand[j][i]) > 1:
                        cand[j][i].remove(kandidat)

            dm2 = divmod(j,3)
            x = dm[1]*3+dm2[1]
            y = dm[0]*3+dm2[0]
            for kandidat in removeCtverec:
                if kandidat in cand[x][y] and len(cand[x][y]) > 1:
                        cand[x][y].remove(kandidat)


    return cand

def delka(pole):
    a = 0
    for i in pole:
        for j in i:
            a = a + len(j)
    return a


kontrola_vstupu(raw)
PrvniKontrola = True
candidates = generate_candidates(raw)
candBef = []

while not candBef == candidates:
    candBef = deepcopy(candidates)
    candidates = pravidlova_zkouska(candidates)



PrvniKontrola = False





print(time()-start)
#-----------------------------------------------------------------------------------------------------------------------------
def vykresli(cand):
    """vykresleni kandidatu pro kazde policko do tabulky"""
    global C
    for i in range(0,9,1):
        for j in range(0,9,1):
            C.create_text(i*80+10,j*80+10, anchor="nw", text=cand[j][i], font="arial 7")
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
okno.mainloop()