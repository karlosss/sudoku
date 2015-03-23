#coding: utf8

from __future__ import unicode_literals
import solver
import solver2
from random import randint

def vyrobit_mrizku():
    """
    vytvoří náhodně vyplněnou sudoku mřížku
    vrátí jedno náhodné řešení, jako argument předáváme prázdnou mřížku
    """
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

    mrizka = solver.solve(mrizka,mode=-1)[0]

    return mrizka

def generate(raw=None, singlesol=True,limit=0,bf=True):
    """
    funkce náhodně odebírá z vyplněné mřížky čísla a kontroluje jednoznačnost řešení

    parametry:
    dvourozměrné pole intů raw: pokud je vyplněn tento parametr, generátor použije tuto mřížku jako základ; jinak si vyrobí vlastní
    bool singlesol: pokud je True, funkce vrací pouze sudoku, co mají jedno řešení
    int limit: garantuje, že v sudoku zůstane alespoň tento počet vyplněných čísel; pokud je mimo interval od 0 do 80, bude ignorován
    bool bf: při testu jednoznačnosti se využije brutální síly; výsledné sudoku tak bude trochu těžší
    """
    if raw == None:
        raw = vyrobit_mrizku()

    k_odebrani = [] #vygenerování seznamu souřadnic všech čísel, které lze zkusit odebrat (na začátku všechny)
    for i in range(0,9,1):
        for j in range(0,9,1):
            k_odebrani.append([i,j])

    vyplneno = 81 #počet aktuálně vyplněných čísel, na začátku 81

    while len(k_odebrani) > 0: #dokud ještě lze odebírat čísla:

        rand = randint(0,len(k_odebrani)-1)
        cislo = raw[k_odebrani[rand][0]][k_odebrani[rand][1]] #náhodně vyber číslo, které odebereš, a zkus jej odebrat

        raw[k_odebrani[rand][0]][k_odebrani[rand][1]] = 0 #odeber jej
        vyplneno = vyplneno - 1 #počet vyplněných čísel klesne o 1

        if singlesol:
            if bf: #pokud chceme generovat jednoznačné sudoku za použití hrubé síly, tak postupuj následovně:
                if len(solver2.solvePC(raw,pocetReseni=2,bf=True)[0]) > 1: #pokud má dosud vytvořené sudoku více než jedno řešení, tak tam čerstvě odebrané číslo vrať
                    raw[k_odebrani[rand][0]][k_odebrani[rand][1]] = cislo
                    vyplneno = vyplneno + 1 #počet vyplněných čísel stoupne o 1
            else:
                sudoku = solver2.solvePC(raw,bf=False)[0][0] #pokud řešíme bez hrubé síly, tak zkusíme, zda lze sudoku pomocí strategií Naked Single a Hidden Single vyřešit až do konce
                if not solver2.sudokuVyreseno(sudoku): #když ne, tak tam opět čerstvě odebrané číslo vrátíme a počet vyplněných čísel stoupne o 1
                    raw[k_odebrani[rand][0]][k_odebrani[rand][1]] = cislo
                    vyplneno = vyplneno + 1


        if vyplneno == limit: #pokud již počet odebraných čísel dosáhl limitu, tak máme hotovo
            return raw

        del(k_odebrani[rand]) #pokud limit ještě nebyl dosažen, tak odstraň číslo ze seznamu odebratelných; buď jeho odebrání způsobuje, že sudoku přestane být jednoznačné, nebo je na jeho místě již prázdno

    return raw #když už nelze nic odebrat, tak je hotovo





