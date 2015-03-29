from __future__ import print_function
from time import time
from copy import deepcopy
from random import shuffle
import sys
start = time()
logovatPostup = True
ukazatCas = True
postup = []
mapa = [[],[]]

# class Null:
#     def write(self,x):
#         pass

#sys.stdout = Null()

#syntax postupu:
#cand - vygenerovat vsechny kandidaty (ve vsech nevyplnenych polickach cisla 1 az 9 bez filtrace)

def generuj_mapu(cand):
    mapa = [
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None]]

    for i in range(0,9,1):
        for j in range(0,9,1):
            if len(cand[i][j]) == 1:
                mapa[i][j] = True
            else:
                mapa[i][j] = False

    return mapa


def kontrola_vstupu(vstup):
    """kontrola uzivatelskeho vstupu"""
    if len(vstup) != 9:
        return False
    for i in vstup:
        if len(i) != 9:
            return False
        for j in i:
            if j not in range(0,10,1):
                return False

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
                cand[j][i] = [template[j][i]]
    return cand

def pravidlova_zkouska(cand):
    global postup, mapa

    for i in range(0,9,1):
        vyskytRadek = [[],[],[],[],[],[],[],[],[]]
        vyskytSloupec = [[],[],[],[],[],[],[],[],[]]
        vyskytCtverec = [[],[],[],[],[],[],[],[],[]]
        removeRadek = []
        removeSloupec = []
        removeCtverec = []
        setKandidatuR = []
        setKandidatuS = []
        setKandidatuC = []
        dm = divmod(i,3)

        for j in range(0,9,1):
            if len(cand[i][j]) == 1: #odebrani kandidatu z radku, sloupcu a ctvercu primo dle zadani
                removeRadek.append(cand[i][j][0])
                if logovatPostup and mapa[i][j] == False:
                    postup.append("zadani;"+str(i)+","+str(j)+";"+str(cand[i][j][0]))
                    mapa[i][j] = True

            if len(cand[j][i]) == 1:
                removeSloupec.append(cand[j][i][0])
                if logovatPostup and mapa[j][i] == False:
                    postup.append("zadani;"+str(j)+","+str(i)+";"+str(cand[j][i][0]))
                    mapa[j][i] = True

            dm2 = divmod(j,3)
            x = dm[1]*3+dm2[1]
            y = dm[0]*3+dm2[0]
            if len(cand[x][y]) == 1:
                removeCtverec.append(cand[x][y][0])
                if logovatPostup and mapa[x][y] == False:
                    postup.append("zadani;"+str(x)+","+str(y)+";"+str(cand[x][y][0]))
                    mapa[x][y] = True

            for k in range(1,10,1):
                if k in cand[i][j] and k not in setKandidatuR:
                    setKandidatuR.append(k)
                if k in cand[j][i] and k not in setKandidatuS:
                    setKandidatuS.append(k)
                if k in cand[x][y] and k not in setKandidatuC:
                    setKandidatuC.append(k)

                if k in cand[i][j]:
                    vyskytRadek[k-1].append([i,j])
                if k in cand[j][i]:
                    vyskytSloupec[k-1].append([j,i])
                if k in cand[x][y]:
                    vyskytCtverec[k-1].append([x,y])

            setKandidatuC.sort()
            setKandidatuS.sort()
            setKandidatuR.sort()

        if setKandidatuC != [1,2,3,4,5,6,7,8,9] or setKandidatuR != [1,2,3,4,5,6,7,8,9] or setKandidatuS != [1,2,3,4,5,6,7,8,9]:
            return False

        for j in range(1,10,1):
            if removeRadek.count(j) > 1 or removeCtverec.count(j) > 1 or removeSloupec.count(j) > 1:
                return False

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


        for j in range(0,9,1):
            if len(vyskytRadek[j]) == 1 and mapa[vyskytRadek[j][0][0]][vyskytRadek[j][0][1]] == False:
                cand[vyskytRadek[j][0][0]][vyskytRadek[j][0][1]] = [j+1]
                mapa[vyskytRadek[j][0][0]][vyskytRadek[j][0][1]] = True
                if logovatPostup:
                    postup.append("uniqueCand;r"+str(i)+";"+str(vyskytRadek[j][0][0])+","+str(vyskytRadek[j][0][1])+";"+str(j+1))
                return cand

            if len(vyskytSloupec[j]) == 1 and mapa[vyskytSloupec[j][0][0]][vyskytSloupec[j][0][1]] == False:
                cand[vyskytSloupec[j][0][0]][vyskytSloupec[j][0][1]] = [j+1]
                mapa[vyskytSloupec[j][0][0]][vyskytSloupec[j][0][1]] = True
                if logovatPostup:
                    postup.append("uniqueCand;s"+str(i)+";"+str(vyskytSloupec[j][0][0])+","+str(vyskytSloupec[j][0][1])+";"+str(j+1))
                return cand

            if len(vyskytCtverec[j]) == 1 and mapa[vyskytCtverec[j][0][0]][vyskytCtverec[j][0][1]] == False:
                cand[vyskytCtverec[j][0][0]][vyskytCtverec[j][0][1]] = [j+1]
                mapa[vyskytCtverec[j][0][0]][vyskytCtverec[j][0][1]] = True
                if logovatPostup:
                    postup.append("uniqueCand;c"+str(i)+";"+str(vyskytCtverec[j][0][0])+","+str(vyskytCtverec[j][0][1])+";"+str(j+1))
                return cand

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
    global postup

    candBef = []
    while not candBef == cand:
        candBef = deepcopy(cand)
        cand = pravidlova_zkouska(cand)

        if cand == False:
            return False
    return cand

def brute_force(cand, mode):
    """BF vyresi vsechno :)"""
    hloubka = 0
    cesta = []
    mezipamet = []
    mezipamet.append(deepcopy(cand))
    cesta.append(0)
    iterace = 0
    reseni = []

    while True:
        iterace = iterace + 1
        uzel = najdi_uzel(cand)
        # print("")
        # print("iterace: "+str(iterace))
        # print("hloubka: "+str(hloubka))
        # print("cesta: "+str(cesta))
        # print("uzel: "+str(uzel))
        if cesta[hloubka] < len(cand[uzel[0]][uzel[1]]):
            cand[uzel[0]][uzel[1]] = [cand[uzel[0]][uzel[1]][cesta[hloubka]]]
        else:
            hloubka = hloubka - 1
            if hloubka == -1:
                # print("Sudoku nema reseni!")
                break
            cesta[hloubka] = cesta[hloubka] + 1
            cand = deepcopy(mezipamet[hloubka])
            del(cesta[hloubka+1])
            del(mezipamet[hloubka+1])
            # print("FAIL, vracim se zpatky a zkusim jine cislo.")
            continue
        cand = kontrola(cand)
        if cand == False:
            cand = deepcopy(mezipamet[hloubka])
            cesta[hloubka] = cesta[hloubka] + 1
            # print("FAIL, zkusim jine cislo.")
        else:
            uzel = najdi_uzel(cand)
            if uzel == False:
                reseni.append(transform_solution(cand))
                # print("reseni nalezeno!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(cand) #nebo hotovo a break pro 1. reseni
                cand = deepcopy(mezipamet[hloubka])
                cesta[hloubka] = cesta[hloubka] + 1
                if mode == len(reseni):
                    break
                else:
                    continue
                # elif mode == 0:
                #     continue
            hloubka = hloubka + 1
            mezipamet.append(deepcopy(cand))
            cesta.append(0)
            # print("OK, jdu hloubeji.")
    return reseni

def transform_solution(cand):
    output = []
    for i in range(0,9,1):
        output.append([])
        for j in range(0,9,1):
            output[i].append(cand[i][j][0])
    return output


def solve(raw, mode=0, bf=True, duration=False, logPostup=False):
    """Vyresi sudoku zadane jako dvojrozmerne pole, s prazdnymi misty oznaceymi nulou.
    Vraci pole dvojrozmernych poli vyreseneho sudoku (reseni muze byt i vic), do konzole vypisuje cas v sekundach potrebny k vyreseni.

    Argumenty: dvojrozmerne pole se zadanim, mode je cele cislo znacici pocet reseni, ktere ma solver najit (0 znamena vsechny).
    Kladne cislo znamena, ze bude nachazet reseni postupne, zaporne znamena, ze tyto bude nachazet nahodne."""
    global logovatPostup, ukazatCas, postup, mapa

    logovatPostup = logPostup
    ukazatCas = duration
    postup = []


    start = time()

    test = kontrola_vstupu(raw)
    if test == False:
        print("chybny vstup")
        print(time()-start)
        return []

    candidates = generate_candidates(raw)
    mapa = generuj_mapu(candidates)
    # for i in mapa:
    #     print(i)
    candidates = kontrola(candidates)
    if candidates == False:
        print("neresitelny vstup")
        print(time()-start)
        return []

    totLen = 0
    for i in range(0,9,1):
        for j in range(0,9,1):
            totLen = totLen + len(candidates[i][j])
    if totLen == 81:
        #print("vyreseno bez BF")
        for i in range(0,len(postup),1):
            print(i,postup[i])
        print(time()-start)
        return [transform_solution(candidates)]
    logovatPostup = False
    postup.append("BF")
    if bf:
        if mode < 0:
            for i in candidates:
                for j in i:
                    shuffle(j)
            mode = abs(mode)
        candidates = brute_force(candidates, mode)
        if candidates == False:
            print("po BF neresitelny vstup")
            print(time()-start)
            return []
        print(time()-start)
        for i in range(0,len(postup),1):
            print(i,postup[i])
        return candidates
    else:
        #print("bez BF neresitelne zadani")
        print(time()-start)
        return []