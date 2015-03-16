from __future__ import print_function
from copy import deepcopy
from time import time


def zkontrolovatVstup(sudoku):
    try:
        for i in range(0,9,1):
            dmI = divmod(i,3)
            radek = []
            sloupec = []
            ctverec = []
            for j in range(0,9,1):
                dmJ = divmod(j,3)
                x = dmI[1]*3+dmJ[1]
                y = dmI[0]*3+dmJ[0]
                radek.append(sudoku[i][j])
                sloupec.append(sudoku[j][i])
                ctverec.append(sudoku[x][y])

            for j in range(1,10,1):
                if radek.count(j) > 1 or sloupec.count(j) > 1 or ctverec.count(j) > 1:
                    return False
        return True
    except:
        return False




def inicializovatKandidaty(sudoku): #vygeneruje cisla 1-9 do kandidatu
    kandidati = [
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
            if sudoku[i][j] == 0:
                kandidati[i][j] = [1,2,3,4,5,6,7,8,9]

    return kandidati

def generujKandidaty(kandidati,reseni): #vygeneruje soubor kandidatu pro kazde policko v sudoku
    for i in range(0,9,1): #projde cele sudoku najednou po radcich, sloupcich i ctvercich; uklada si zadana cisla pro ten ktery set a nasledne tato cisla z kandidatu tohoto setu odebere
        dmI = divmod(i,3)
        odebratZradku = []
        odebratZsloupce = []
        odebratZctverce = []

        for j in range(0,9,1):
            dmJ = divmod(j,3)
            x = dmI[1]*3+dmJ[1]
            y = dmI[0]*3+dmJ[0]

            if reseni[i][j] != 0: #prochazeni radku
                odebratZradku.append(reseni[i][j])
            if reseni[j][i] != 0: #prochazeni sloupce
                odebratZsloupce.append(reseni[j][i])
            if reseni[x][y] != 0: #prochazeni ctverce
                odebratZctverce.append(reseni[x][y])

        for j in range(0,9,1):
            dmJ = divmod(j,3)
            x = dmI[1]*3+dmJ[1]
            y = dmI[0]*3+dmJ[0]

            for k in odebratZradku: #odebirani z radku
                if k in kandidati[i][j]:
                    kandidati[i][j].remove(k)

            for k in odebratZsloupce: #odebirani ze sloupce
                if k in kandidati[j][i]:
                    kandidati[j][i].remove(k)

            for k in odebratZctverce: #odebirani ze ctverce
                if k in kandidati[x][y]:
                    kandidati[x][y].remove(k)

    return kandidati




def nakedSingle(kandidati,reseni,logovatPostup=False): #pokud je v policku pouze jeden kandidat, tak je toto cislo oznaceno jako reseni pro dane policko

    postup = []

    for i in range(0,9,1):
        for j in range(0,9,1):
            if len(kandidati[i][j]) == 1:
                reseni[i][j] = kandidati[i][j][0]
                # print("last possibility: na pozici "+str(i)+","+str(j)+" doplnuji "+str(kandidati[i][j][0]))
                postup = ["Naked Single",[i,j],kandidati[i][j][0]]
                kandidati[i][j] = []
                if logovatPostup:
                    return [kandidati,reseni,postup]
                else:
                    return [kandidati,reseni]

    if logovatPostup:
        return [kandidati,reseni,postup]
    else:
        return [kandidati,reseni]

def hiddenSingle(kandidati,reseni,logovatPostup=False): #kdyz je v danem setu nejaky kandidat prave jednou, tak prave v tomto policku bude toto cislo jako reseni; zaroven umi detekovat neresitelnost v pripade, ze v nejakem setu nejake cislo uplne chybi

    postup = []

    nemaReseni = False
    for i in range(0,9,1):
        dmI = divmod(i,3)

        kandidatiVradku = []
        kandidatiVsloupci = []
        kandidatiVctverci = []

        zadanaCislaVradku = []
        zadanaCislaVsloupci = []
        zadanaCislaVctverci = []

        for j in range(0,9,1):
            dmJ = divmod(j,3)
            x = dmI[1]*3+dmJ[1]
            y = dmI[0]*3+dmJ[0]

            kandidatiVradku = kandidatiVradku+kandidati[i][j]
            kandidatiVsloupci = kandidatiVsloupci+kandidati[j][i]
            kandidatiVctverci = kandidatiVctverci+kandidati[x][y]

            if reseni[i][j] != 0:
                zadanaCislaVradku.append(reseni[i][j])
            if reseni[j][i] != 0:
                zadanaCislaVsloupci.append(reseni[j][i])
            if reseni[x][y] != 0:
                zadanaCislaVctverci.append(reseni[x][y])

        for k in range(1,10,1):
            if k not in zadanaCislaVradku+kandidatiVradku or k not in zadanaCislaVsloupci+kandidatiVsloupci or k not in zadanaCislaVctverci+kandidatiVctverci: #kdyz v nejakem setu cislo chybi uplne, tak sudoku nema reseni
                nemaReseni = True
                if logovatPostup:
                    return [kandidati,reseni,nemaReseni,postup]
                else:
                    return [kandidati,reseni,nemaReseni]

            if kandidatiVradku.count(k) == 1: #kdyz je v danem setu nejaky kandidat prave jednou, tak prave v tomto policku bude toto cislo jako reseni
                for l in range(0,9,1):
                    if k in kandidati[i][l]:
                        reseni[i][l] = k
                        kandidati[i][l] = []
                        # print("unique cand: na radku "+str(i)+" na pozici "+str(i)+","+str(l)+" doplnuji "+str(k))
                        postup = ["Hidden Single",["r",i],[i,l],k]
                        if logovatPostup:
                            return [kandidati,reseni,nemaReseni,postup]
                        else:
                            return [kandidati,reseni,nemaReseni]

            if kandidatiVsloupci.count(k) == 1:
                for l in range(0,9,1):
                    if k in kandidati[l][i]:
                        reseni[l][i] = k
                        kandidati[l][i] = []
                        # print("unique cand: ve sloupci "+str(i)+" na pozici "+str(l)+","+str(i)+" doplnuji "+str(k))
                        postup = ["Hidden Single",["s",i],[l,i],k]
                        if logovatPostup:
                            return [kandidati,reseni,nemaReseni,postup]
                        else:
                            return [kandidati,reseni,nemaReseni]

            if kandidatiVctverci.count(k) == 1:
                for l in range(0,9,1):
                    dmJ = divmod(l,3)
                    x = dmI[1]*3+dmJ[1]
                    y = dmI[0]*3+dmJ[0]
                    if k in kandidati[x][y]:
                        reseni[x][y] = k
                        kandidati[x][y] = []
                        # print("unique cand: ve ctverci "+str(i)+" na pozici "+str(x)+","+str(y)+" doplnuji "+str(k))
                        postup = ["Hidden Single",["c",i],[x,y],k]
                        if logovatPostup:
                            return [kandidati,reseni,nemaReseni,postup]
                        else:
                            return [kandidati,reseni,nemaReseni]

    if logovatPostup:
        return [kandidati,reseni,nemaReseni,postup]
    else:
        return [kandidati,reseni,nemaReseni]


def sudokuVyreseno(reseni): #test, zda je sudoku vyreseno (neobsahuje nulu)
    merged = []
    for i in reseni:
        merged = merged + i

    if 0 not in merged:
        return True
    else:
        return False

def najdiPolickoProTest(kandidati):
    merged = []
    for i in kandidati:
        merged = merged + i

    for i in range(0,len(merged),1):
        merged[i] = len(merged[i])

    try:
        policko = merged.index(min(filter(lambda x: x >= 2, merged)))
        policko = divmod(policko,9)
        return policko

    except ValueError: #kdyz neexistuje, tak vrat treba -1,-1, na to uz se nikdo ptat nebude
        return [-1,-1]

def bruteForce(reseni,pocetReseni):
    toReturn = []
    hloubka = 0
    cesta = [0]
    mezipamet = [deepcopy(reseni)]

    while True:
        kandidati = inicializovatKandidaty(reseni)
        kandidati = generujKandidaty(kandidati,reseni)
        policko = najdiPolickoProTest(kandidati)

        if sudokuVyreseno(reseni):
            toReturn.append(reseni)
            if len(toReturn) == pocetReseni:
                print("ukonceno predcasne")
                return toReturn

        while cesta[hloubka] > len(kandidati[policko[0]][policko[1]])-1: #CHYBA, snizuju hloubku
            del(mezipamet[hloubka])
            del(cesta[hloubka])
            hloubka = hloubka - 1

            if hloubka == -1:
                return toReturn

            reseni = mezipamet[hloubka]
            cesta[hloubka] = cesta[hloubka] + 1
            kandidati = inicializovatKandidaty(reseni)
            kandidati = generujKandidaty(kandidati,reseni)
            policko = najdiPolickoProTest(kandidati)

        reseni[policko[0]][policko[1]] = kandidati[policko[0]][policko[1]][cesta[hloubka]]
        kandidati = inicializovatKandidaty(reseni)
        kandidati = generujKandidaty(kandidati,reseni)

        sudokuBef = None
        candBef = None
        nemaReseni = False

        while sudokuBef != reseni or candBef != kandidati:
            while sudokuBef != reseni or candBef != kandidati:

                sudokuBef = deepcopy(reseni)
                candBef = deepcopy(kandidati)
                vysl = nakedSingle(kandidati,reseni)
                kandidati = vysl[0]
                reseni = vysl[1]
                kandidati = generujKandidaty(kandidati,reseni)

            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = hiddenSingle(kandidati,reseni)
            kandidati = vysl[0]
            reseni = vysl[1]
            nemaReseni = vysl[2]
            kandidati = generujKandidaty(kandidati,reseni)

        if not nemaReseni: #OK, jdu do vetsi hloubky
            hloubka = hloubka + 1
            mezipamet.append(deepcopy(reseni))
            cesta.append(0)
            continue

        else: #CHYBA, zkusim jine cislo ve stejne hloubce, pokud existuje (provede se na zacatku cyklu)
            reseni = mezipamet[hloubka]
            cesta[hloubka] = cesta[hloubka] + 1
            continue

    return toReturn

def solvePC(zad,pocetReseni=1,bf=True): #vraci pole: nulty prvek je pole reseni a prvni prvek je cas v milisekundach
    #################POVINNA HLAVICKA######################
    cas = time()
    zadani = deepcopy(zad)
    reseni = deepcopy(zadani)
    kandidati = inicializovatKandidaty(reseni)
    kandidati = generujKandidaty(kandidati,reseni)
    #################POVINNA HLAVICKA######################

    if not zkontrolovatVstup(zadani):
        return [[],(time()-cas)*1000]

    sudokuBef = None
    candBef = None
    nemaReseni = False

    while sudokuBef != reseni or candBef != kandidati:
        while sudokuBef != reseni or candBef != kandidati:

            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = nakedSingle(kandidati,reseni)
            kandidati = vysl[0]
            reseni = vysl[1]
            kandidati = generujKandidaty(kandidati,reseni)

        sudokuBef = deepcopy(reseni)
        candBef = deepcopy(kandidati)
        vysl = hiddenSingle(kandidati,reseni)
        kandidati = vysl[0]
        reseni = vysl[1]
        nemaReseni = vysl[2]
        kandidati = generujKandidaty(kandidati,reseni)

    if nemaReseni:
        return [[],(time()-cas)*1000]

    if not sudokuVyreseno(reseni) and bf:
        reseni = bruteForce(reseni,pocetReseni)
    else:
        reseni = [reseni]

    return [reseni,(time()-cas)*1000]

def solveHuman(zad,kandidati=None,naked_single=True,hidden_single=True):
    #################POVINNA HLAVICKA######################
    cas = time()
    zadani = deepcopy(zad)
    reseni = deepcopy(zadani)
    if kandidati == None:
        kandidati = inicializovatKandidaty(reseni)
        kandidati = generujKandidaty(kandidati,reseni)
    postup = []
    #################POVINNA HLAVICKA######################

    pokus = solvePC(zadani)
    if len(pokus[0]) == 0:
        return [[],(time()-cas)*1000,False,True] #nema reseni

    sudokuBef = None
    candBef = None
    nemaReseni = False

    while sudokuBef != reseni or candBef != kandidati:
        while sudokuBef != reseni or candBef != kandidati:
            if naked_single:
                sudokuBef = deepcopy(reseni)
                candBef = deepcopy(kandidati)
                vysl = nakedSingle(kandidati,reseni,logovatPostup=True)
                kandidati = vysl[0]
                reseni = vysl[1]
                if vysl[2] != []:
                    postup.append(vysl[2])
                    return [postup,(time()-cas),True,True]
                kandidati = generujKandidaty(kandidati,reseni)

        if hidden_single:
            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = hiddenSingle(kandidati,reseni,logovatPostup=True)
            kandidati = vysl[0]
            reseni = vysl[1]
            nemaReseni = vysl[2]
            if vysl[3] != []:
                postup.append(vysl[3])
                return [postup,(time()-cas),True,True]
            kandidati = generujKandidaty(kandidati,reseni)

        if nemaReseni:
            return [[],(time()-cas)*1000,False,True]

    if not sudokuVyreseno(reseni):
        return [postup,(time()-cas)*1000,True,False]

