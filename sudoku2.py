from __future__ import print_function
from Tkinter import *
from time import time
from copy import deepcopy


start = time()

raw = [
[2,0,5,4,0,0,0,0,0],
[0,0,8,0,6,1,0,0,0],
[0,1,0,0,0,0,3,6,0],
[1,0,0,7,0,0,4,0,8],
[0,7,0,6,0,4,0,1,0],
[8,0,4,0,0,9,0,0,6],
[0,2,1,0,0,0,0,4,0],
[0,0,0,1,5,0,6,0,0],
[0,0,0,0,0,7,1,0,5]
]


def kontrola_vstupu(vstup):
    """kontrola uzivatelskeho vstupu"""
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
    """vygeneruje kandidaty pro nezadana policka"""
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
    """algoritmus kontroly pravidel sudoku"""
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

def najdi_uzel(cand):
    """Vrati nejblizsi nejednoznacny uzel k levemu hornimu rohu. Vrati false kdyz zadny neexistuje."""
    for i in range(0,9,1):
        for j in range(0,9,1):
            if len(cand[i][j]) > 1:
                return [i,j]
    return False

def kontrola(cand):
    """kontrola pravidel, dokud se deji zmeny"""
    candBef = []
    while not candBef == cand:
        candBef = deepcopy(cand)
        cand = pravidlova_zkouska(cand)
        if cand == False:
            return False
    return cand

def brute_force(cand):
    """BF vyresi vsechno :)"""
    hloubka = 0
    cesta = []
    mezipamet = []
    mezipamet.append(deepcopy(cand))
    cesta.append(0)
    iterace = 0

    while True:
        iterace = iterace + 1

        uzel = najdi_uzel(cand)

        print("")
        print("iterace: "+str(iterace))
        print("hloubka: "+str(hloubka))
        print("cesta: "+str(cesta))
        print("uzel: "+str(uzel))

        if uzel == False:
            print("Hotovo!")
            break
        if cesta[hloubka] < len(cand[uzel[0]][uzel[1]]):
            cand[uzel[0]][uzel[1]] = [cand[uzel[0]][uzel[1]][cesta[hloubka]]]
        else:
            hloubka = hloubka - 1
            if hloubka == -1:
                print("Sudoku nema reseni!")
                break
            cesta[hloubka] = cesta[hloubka] + 1
            cand = deepcopy(mezipamet[hloubka])
            del(cesta[hloubka+1])
            del(mezipamet[hloubka+1])
            print("FAIL, vracim se zpatky a zkusim jine cislo.")
            continue
        cand = kontrola(cand)
        if cand == False:
            cand = deepcopy(mezipamet[hloubka])
            cesta[hloubka] = cesta[hloubka] + 1
            print("FAIL, zkusim jine cislo.")
        else:
            hloubka = hloubka + 1
            mezipamet.append(deepcopy(cand))
            cesta.append(0)
            print("OK, jdu hloubeji.")
    return cand

kontrola_vstupu(raw)
PrvniKontrola = True
candidates = generate_candidates(raw)
candidates = kontrola(candidates)

PrvniKontrola = False
candidates = brute_force(candidates)

print()
print("Doba vypoctu "+str(1000*(time()-start))+" ms")
#-----------------------------------------------------------------------------------------------------------------------------
def vykresli(cand):
    """vykresleni kandidatu pro kazde policko do tabulky"""
    global C
    for i in range(0,9,1):
        for j in range(0,9,1):
            C.create_text(i*80+10,j*80+10, anchor="nw", text=cand[j][i], font="arial 30")


okno = Tk()
okno.minsize(1400,810)
okno.maxsize(1400,810)
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