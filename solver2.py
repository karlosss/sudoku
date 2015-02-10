from __future__ import print_function
from copy import deepcopy

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




def lastPossibility(kandidati,reseni): #pokud je v policku pouze jeden kandidat, tak je toto cislo oznaceno jako reseni pro dane policko

    for i in range(0,9,1):
        for j in range(0,9,1):
            if len(kandidati[i][j]) == 1:
                reseni[i][j] = kandidati[i][j][0]
                # print("last possibility: na pozici "+str(i)+","+str(j)+" doplnuji "+str(kandidati[i][j][0]))
                kandidati[i][j] = []
                return [kandidati,reseni]

    return [kandidati,reseni]

def uniqueCandInGroup(kandidati,reseni): #kdyz je v danem setu nejaky kandidat prave jednou, tak prave v tomto policku bude toto cislo jako reseni; zaroven umi detekovat neresitelnost v pripade, ze v nejakem setu nejake cislo uplne chybi
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
                return [kandidati,reseni,nemaReseni]

            if kandidatiVradku.count(k) == 1: #kdyz je v danem setu nejaky kandidat prave jednou, tak prave v tomto policku bude toto cislo jako reseni
                for l in range(0,9,1):
                    if k in kandidati[i][l]:
                        reseni[i][l] = k
                        kandidati[i][l] = []
                        # print("unique cand: na radku "+str(i)+" na pozici "+str(i)+","+str(l)+" doplnuji "+str(k))
                        return [kandidati,reseni,nemaReseni]

            if kandidatiVsloupci.count(k) == 1:
                for l in range(0,9,1):
                    if k in kandidati[l][i]:
                        reseni[l][i] = k
                        kandidati[l][i] = []
                        # print("unique cand: ve sloupci "+str(i)+" na pozici "+str(l)+","+str(i)+" doplnuji "+str(k))
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
                        return [kandidati,reseni,nemaReseni]

    return [kandidati,reseni,nemaReseni]

def nakedPair(kandidati,reseni):
    for i in range(0,9,1):
        dmI = divmod(i,3)



        for j in range(0,9,1):
            dmJ = divmod(j,3)
            x = dmI[1]*3+dmJ[1]
            y = dmI[0]*3+dmJ[0]

            if len(kandidati[i][j]) == 2:
                for k in range(0,9,1):
                    if k == j:
                        continue
                    if kandidati[i][j] == kandidati[i][k]:
                        for l in range(0,9,1):
                            if l != j and l != k:
                                for m in kandidati[i][j]:
                                    if m in kandidati[i][l]:
                                        kandidati[i][l].remove(m)
                                        print("naked pair: na radku "+str(i)+" se na pozicich "+str(i)+","+str(j)+" a "+str(i)+","+str(k)+" nachazi stejna dvojice kandidatu; proto z pozice "+str(i)+","+str(l)+" odebiram "+str(m))
                                        return [kandidati,reseni]

            if len(kandidati[j][i]) == 2:
                for k in range(0,9,1):
                    if k == j:
                        continue
                    if kandidati[j][i] == kandidati[k][i]:
                        for l in range(0,9,1):
                            if l != j and l != k:
                                for m in kandidati[j][i]:
                                    if m in kandidati[l][i]:
                                        kandidati[l][i].remove(m)
                                        print("naked pair: ve sloupci "+str(i)+" se na pozicich "+str(j)+","+str(i)+" a "+str(k)+","+str(i)+" nachazi stejna dvojice kandidatu; proto z pozice "+str(l)+","+str(i)+" odebiram "+str(m))
                                        return [kandidati,reseni]


            if len(kandidati[x][y]) == 2:
                for k in range(0,9,1):
                    dmJ = divmod(k,3)
                    x1 = dmI[1]*3+dmJ[1]
                    y1 = dmI[0]*3+dmJ[0]

                    if (x1,y1) == (x,y):
                        continue
                    if kandidati[x][y] == kandidati[x1][y1]:
                        for l in range(0,9,1):
                            if l != j and l != k:
                                for m in kandidati[x][y]:
                                    if m in kandidati[x1][y1]:
                                        kandidati[x1][y1].remove(m)
                                        print("naked pair: ve ctverci "+str(i)+" se na pozicich "+str(x)+","+str(y)+" a "+str(x1)+","+str(y1)+" nachazi stejna dvojice kandidatu; proto z pozice "+str(x1)+","+str(y1)+" odebiram "+str(m))
                                        return [kandidati,reseni]

    return [kandidati,reseni]






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
                vysl = lastPossibility(kandidati,reseni)
                kandidati = vysl[0]
                reseni = vysl[1]
                kandidati = generujKandidaty(kandidati,reseni)

            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = uniqueCandInGroup(kandidati,reseni)
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






def solvePC(zad,pocetReseni=1):
    #################POVINNA HLAVICKA######################
    zadani = deepcopy(zad)
    reseni = deepcopy(zadani)
    kandidati = inicializovatKandidaty(reseni)
    kandidati = generujKandidaty(kandidati,reseni)
    #################POVINNA HLAVICKA######################

    sudokuBef = None
    candBef = None
    nemaReseni = False

    while sudokuBef != reseni or candBef != kandidati:
        while sudokuBef != reseni or candBef != kandidati:

            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = lastPossibility(kandidati,reseni)
            kandidati = vysl[0]
            reseni = vysl[1]
            kandidati = generujKandidaty(kandidati,reseni)

        sudokuBef = deepcopy(reseni)
        candBef = deepcopy(kandidati)
        vysl = uniqueCandInGroup(kandidati,reseni)
        kandidati = vysl[0]
        reseni = vysl[1]
        nemaReseni = vysl[2]
        kandidati = generujKandidaty(kandidati,reseni)

    if nemaReseni:
        return False

    if not sudokuVyreseno(reseni):
        reseni = bruteForce(reseni,pocetReseni)

    return reseni

def solveHuman(zad):
    #################POVINNA HLAVICKA######################
    zadani = deepcopy(zad)
    reseni = deepcopy(zadani)
    kandidati = inicializovatKandidaty(reseni)
    kandidati = generujKandidaty(kandidati,reseni)
    #################POVINNA HLAVICKA######################

    sudokuBef = None
    candBef = None
    nemaReseni = False

    while sudokuBef != reseni or candBef != kandidati:
        while sudokuBef != reseni or candBef != kandidati:
            while sudokuBef != reseni or candBef != kandidati:

                sudokuBef = deepcopy(reseni)
                candBef = deepcopy(kandidati)
                vysl = lastPossibility(kandidati,reseni)
                kandidati = vysl[0]
                reseni = vysl[1]
                kandidati = generujKandidaty(kandidati,reseni)

            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = uniqueCandInGroup(kandidati,reseni)
            kandidati = vysl[0]
            reseni = vysl[1]
            nemaReseni = vysl[2]
            kandidati = generujKandidaty(kandidati,reseni)

        sudokuBef = deepcopy(reseni)
        candBef = deepcopy(kandidati)
        vysl = nakedPair(kandidati,reseni)
        kandidati = vysl[0]
        reseni = vysl[1]
        kandidati = generujKandidaty(kandidati,reseni)

        if nemaReseni:
            return False

    if not sudokuVyreseno(reseni):
        reseni = bruteForce(reseni)



    if reseni == False:
        print("nema reseni")

    else:
        for i in reseni:
            print(i)

