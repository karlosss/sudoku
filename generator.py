from __future__ import print_function
import solver
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


def odeber_cisla(sudoku, bf=False, limit=0):

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

            if bf:
                reseni = solver.solve(sudoku, mode=2)
            else:
                reseni = solver.solve(sudoku, mode=2, bf=False)

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
                    #print(81-pocetOdebranych)
                    nejdeOdebrat = True
                    break

    return sudoku

lehke = []
stredneTezke = []
obtizne = []

zadani = vytvor_mrizku()

for i in range(300):
    lehkeApp = odeber_cisla(deepcopy(zadani), bf=False, limit=40)
    lehke.append(lehkeApp)
    stredneTezkeApp = odeber_cisla(deepcopy(zadani), bf=False, limit=0)
    stredneTezke.append(lehkeApp)
    obtizneApp = odeber_cisla(deepcopy(zadani), bf=True, limit=0)
    obtizne.append(lehkeApp)

print("hotovo")
# for i in lehke:
#     print()
#     print()
#     for j in i:
#         print(j)





