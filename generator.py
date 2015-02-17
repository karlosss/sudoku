from __future__ import print_function
import solver
import solver2
from random import randint
from copy import deepcopy

def vytvor_mrizku():
    sudoku = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]

    reseni = solver.solve(sudoku, mode=-1)
    return reseni[0]

def vyplnena_policka(sudoku):
    """vrati pozice vsech vyplnenych policek relativne k levemu hornimu rohu po radcich"""
    pozice = []

    for i in range(0,9,1):
        for j in range(0,9,1):
            if sudoku[i][j] != 0:
                pozice.append(i*9+j)

    return pozice


def odeber_cisla(sudoku, bf=False, limit=0, singlesol=True):
    sudoku = deepcopy(sudoku)

    nejdeOdebrat = False
    pocetOdebranych = 0

    while nejdeOdebrat == False:
        policka = vyplnena_policka(sudoku)

        odebrano = False
        rand = randint(0,len(policka)-1)
        initRand = rand

        # for i in sudoku:
        #     print(i)
        #
        # print("")
        # print("")
        # print("")
        # print("")


        while odebrano == False:
            policko = policka[rand]
            policko = divmod(policko,9)

            predchoziHodnota = sudoku[policko[0]][policko[1]]
            sudoku[policko[0]][policko[1]] = 0

            if not singlesol:
                pocetOdebranych = pocetOdebranych + 1
                if 81 - pocetOdebranych == limit:
                    return sudoku
                else:
                    break

            if bf:
                reseni = solver2.solvePC(sudoku, pocetReseni=2, bf=True)[0]
            else:
                reseni = solver2.solvePC(sudoku, pocetReseni=2, bf=False)[0]

            if len(reseni) == 1:
                odebrano = True
                pocetOdebranych = pocetOdebranych + 1
                if 81 - pocetOdebranych == limit:
                    #print("limit dosazen")
                    #print(81-pocetOdebranych)
                    nejdeOdebrat = True
                    break
            else:
                sudoku[policko[0]][policko[1]] = predchoziHodnota
                rand = rand + 1
                if rand == len(policka):
                    rand = 0

                if rand == initRand:
                    #print("limit nedosazen")
                    nejdeOdebrat = True
                    break

    print(81-pocetOdebranych)
    return sudoku

def generate(singlesol=True, bf=False, limit=0):
    sudoku = vytvor_mrizku()
    sudoku = odeber_cisla(sudoku,bf=bf,limit=limit,singlesol=singlesol)
    return sudoku