from __future__ import print_function
import solver
import solver2
from random import randint
from copy import deepcopy

def vyrobit_mrizku():
    mrizka = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

    mrizka = solver.solve(mrizka,mode=-1)

    return mrizka

def spocitat_plne(seznam):
    c = []
    for i in range(0,9,1):
        for j in range(0,9,1):
            if seznam[i][j] == True:
                c.append([i,j])

    return c

def generovat(mrizka):
    seznam_plnych = [
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True],
        [True,True,True,True,True,True,True,True,True]]

    while True:
        mrizkaBackup = deepcopy(mrizka)

        plne = spocitat_plne(seznam_plnych)
        rnd = randint(0,len(plne))
        nahodnaPlna = plne[rnd]

        #TODO




a = vyrobit_mrizku()
for i in a:
    for j in i:
        print(j)