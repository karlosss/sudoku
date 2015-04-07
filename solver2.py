from __future__ import print_function
from copy import deepcopy
from time import time


def zkontrolovatVstup(sudoku):
    # predbezna kontrola vstupu; zkusi aplikovat nekolik prodecur, pokud kterakoli z nich vrati chybu,
    # cela funkce vrati False, jinak vrati True; kontrola je zde z duvodu, aby pri pozdejsim behu solveru
    # nevyskakovaly chyby.

    try:
        for i in range(0,9,1):
            # inicializace pole cisel, ktere se budou vyskytovat v i-tem radku, sloupci a ctverci; budeme kontrolovat,
            # zda v danem radku, sloupci i ctverci se kazde zadane cislo nachazi maximalne jednou; zaroven lze takto
            # nenapadne zjistit, zda uzivatel zadal dvourozmerne pole o rozmerech 9x9 (pokud zada vic, tak by to nemelo)
            # vadit, presahujici cisla se proste ignoruji

            dmI = divmod(i,3)
            # tohle je dobry trik, jak vsechny sety probehnout pouze dvema for-cykly, jednim inicializacnim a druhym,
            # ktery vykonava samotnou cinnost; pokud u cisel od 0 do 8 spocitame celociselny podil 3 a zbytek po deleni 3,
            # dostaneme sekvenci (0,0),(0,1),(0,2),(1,0)...(2,2), coz jsou vlastne souradnice ctvercu a nasledne cisel
            # ve ctvercich

            radek = []
            sloupec = []
            ctverec = []

            for j in range(0,9,1):
                # procesni cyklus, ktery naplni patricna pole cisly zadanymi v radku, sloupci a ctverci

                if sudoku[i][j] not in range(0,10,1):
                    return False
                # tato podminka zkontroluje, zda je v poli na danem miste cele cislo v rozsahu od 0 do 9 vcetne; krome
                # datoveho typu se takto da jednoduse zjistit i interval; pokud se tam cislo nevejde, test skonci
                # vysledkem, ze sudoku je chybne; behem behu dvou cyklu projdeme cele sudoku, takze vsechny pripadne
                # chyby na 100% odhalime

                dmJ = divmod(j,3)
                x = dmI[1]*3+dmJ[1]
                y = dmI[0]*3+dmJ[0]

                # zde opet pouzijeme figl, kterym projdeme ctverce v ramci dvou for-cyklu behajicich do deviti; ctverce
                # maji rozmer 3x3, takze staci souradnice ctverce vynasobit 3 a k nim pricist souradnice aktualne
                # testovaneho policka

                radek.append(sudoku[i][j])
                sloupec.append(sudoku[j][i])
                ctverec.append(sudoku[x][y])

                # do testovaneho setu pridame aktualne zjistene cislo

            for j in range(1,10,1):
                # druhy procesni cyklus, ktery provede samotny test, zda v nejakem setu neni zadano totozne cislo
                # vicekrat; funguje pro cisla od 1 do 9, takze prazdna mista - nuly - ingoruje; pokud zjisti vicenasobny
                # vyskyt, test vrati False

                if radek.count(j) > 1 or sloupec.count(j) > 1 or ctverec.count(j) > 1:
                    return False

        return True
        # pokud vse probehne v poradku, test vrati True, jinak vrati False

    except:
        return False




def inicializovatKandidaty(sudoku):
    # samotna inicializace je celkem nuda; proste a jednoduse, pro kazde policko se do sablony vyobrazene nize
    # vygeneruje seznam cisel od 1 do 9 v pripade, ze v nem neni zadane cislo; dalsi komentar asi neni potreba
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

def generujKandidaty(kandidati,reseni):
    # tohle uz je trochu zajimavejsi; pro kazdy set zjisti vsechna cisla v nem zadana, potom se vrati k volnym polickum
    # tohoto setu a zjistena cisla odebere z kandidatu techto policek, takze vystupem funkce bude konecny seznam
    # kandidatu pro vsechna policka - zustanou jen ta cisla, ktera primo odporuji pravidlum sudoku

    for i in range(0,9,1):
        # opet dva for-cykly, inicializacni a procesni; na kontrolu ctvercu opet pouzijeme stejny figl, abychom se
        # vyhnuli dalsim for-cyklum, ktere by vyrazne zhorsily vypocetni cas

        dmI = divmod(i,3)
        odebratZradku = []
        odebratZsloupce = []
        odebratZctverce = []

        for j in range(0,9,1):
            dmJ = divmod(j,3)
            x = dmI[1]*3+dmJ[1]
            y = dmI[0]*3+dmJ[0]

            if reseni[i][j] != 0:
                odebratZradku.append(reseni[i][j])
            if reseni[j][i] != 0:
                odebratZsloupce.append(reseni[j][i])
            if reseni[x][y] != 0:
                odebratZctverce.append(reseni[x][y])

            # pokud najdeme v setu zadane cislo, poznamename si, ze jej budeme chtit odebrat

        for j in range(0,9,1):

            # zde projdeme vsechna policka v radku, sloupci a ctverci znovu a z jejich kandidatu odebereme patricna
            # cisla
            dmJ = divmod(j,3)
            x = dmI[1]*3+dmJ[1]
            y = dmI[0]*3+dmJ[0]

            for k in odebratZradku:
                if k in kandidati[i][j]:
                    kandidati[i][j].remove(k)

            # opet pouzivame figl; metoda remove() funguje tak, ze odebere prvek z pole pouze tehdy, pokud tam je;
            # v opacnem pripade se nestane nic, ani chybu nevyhodi; toho vyuzijeme tak, ze se z kandidatu kazdeho
            # policka pokusime s cistym svedomim odebrat vsechno

            for k in odebratZsloupce:
                if k in kandidati[j][i]:
                    kandidati[j][i].remove(k)

            for k in odebratZctverce:
                if k in kandidati[x][y]:
                    kandidati[x][y].remove(k)

    return kandidati




def nakedSingle(kandidati,reseni,logovatPostup=False):
    # strategie je detailne popsana v pruvodnim dokumentu, zde se budeme soustredit pouze na popis zdrojoveho kodu

    postup = []
    nemaReseni = False

    # krome vyreseni policka umi strategie v urcitych pripadech odhalit i neresitelne sudoku

    for i in range(0,9,1):
        for j in range(0,9,1):

            # projdeme vsechna policka v sudoku

            if len(kandidati[i][j]) == 1:

                # pokud zjistime, ze se v nejakem policku nachazi pouze jeden kandidat, tak ho vyplnime jako reseni
                # tohoto policka, zapiseme si postup (syntax je popsan v programatorske dokumentaci), policku vymazeme
                # kandidaty (kdyz uz jej mame vyresene, tak jeho kandidati jsou irelevantni) a vratime podle prani
                # uzivatele nejaka data

                reseni[i][j] = kandidati[i][j][0]
                postup = ["Naked Single",[i,j],kandidati[i][j][0]]
                kandidati[i][j] = []

                if logovatPostup:
                    return [kandidati,reseni,nemaReseni,postup]
                else:
                    return [kandidati,reseni,nemaReseni]

            elif len(kandidati[i][j]) == 0 and reseni[i][j] == 0:

                # pokud nahodou narazime na policko, ktere neni vyresene a nema zadneho legalniho kandidata, tak tuto
                # skutecnost oznamime

                nemaReseni = True
                if logovatPostup:
                    return [kandidati,reseni,nemaReseni,postup]
                else:
                    return [kandidati,reseni,nemaReseni]

    # a pokud nenajdeme zadne policko, ktere by melo jednoho nebo zadneho kandidata, potom byla strategie neuspesna
    # a vratime nezmenena vstupni data

    if logovatPostup:
        return [kandidati,reseni,nemaReseni,postup]
    else:
        return [kandidati,reseni,nemaReseni]

def hiddenSingle(kandidati,reseni,logovatPostup=False):
    # strategie je detailne popsana v pruvodnim dokumentu, zde se budeme soustredit pouze na popis zdrojoveho kodu

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

            # nacteme si vsechny kandidaty ze vsech policek daneho setu

            if reseni[i][j] != 0:
                zadanaCislaVradku.append(reseni[i][j])
            if reseni[j][i] != 0:
                zadanaCislaVsloupci.append(reseni[j][i])
            if reseni[x][y] != 0:
                zadanaCislaVctverci.append(reseni[x][y])

            # nacteme si vsechna zadana cisla v kazdem setu

        for k in range(1,10,1):

            # zde zacina samotne setreni; kazde cislo od 1 do 9 musi byt v kazdem setu bud zadano, nebo musi byt
            # v kandidatech alespon jednoho policka tohoto setu; pokud tomu tak neni, sudoku nema reseni

            if k not in zadanaCislaVradku+kandidatiVradku or k not in zadanaCislaVsloupci+kandidatiVsloupci or k not in zadanaCislaVctverci+kandidatiVctverci: #kdyz v nejakem setu cislo chybi uplne, tak sudoku nema reseni
                nemaReseni = True
                if logovatPostup:
                    return [kandidati,reseni,nemaReseni,postup]
                else:
                    return [kandidati,reseni,nemaReseni]

            if kandidatiVradku.count(k) == 1:

                # pokud se stane, ze je v kandidatech nejakeho setu (v tomto pripade radku) nejaky kandidat prave
                # jednou, potom zjistime, ve kterem policku se tento kandidat nechazi a dane cislo vyplnime jako reseni
                # tohoto policka; obdobnou proceduru pote provedeme i pro sloupce a ctverce

                for l in range(0,9,1):
                    if k in kandidati[i][l]:
                        reseni[i][l] = k
                        kandidati[i][l] = []
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
                        postup = ["Hidden Single",["c",i],[x,y],k]
                        if logovatPostup:
                            return [kandidati,reseni,nemaReseni,postup]
                        else:
                            return [kandidati,reseni,nemaReseni]


    # mame opet zadni vratka, pokud by strategie byla neuspesna

    if logovatPostup:
        return [kandidati,reseni,nemaReseni,postup]
    else:
        return [kandidati,reseni,nemaReseni]


def sudokuVyreseno(reseni):
    # test, zda je sudoku zcela vyplneno (neobsahuje nulu, nevyplnene policko)
    # provedeme tak, ze sloucime matici 9x9 do jednoho 81 prvku velkeho pole a jednoduse overime vyskyt nuly

    merged = []
    for i in reseni:
        merged = merged + i

    if 0 not in merged:
        return True
    else:
        return False

def najdiPolickoProTest(kandidati):

    # najdeme policko s nejmene kandidaty a vratime jeho souradnice; pokud je takovychto policek vice, potom vratime to,
    # ktere potkame jako prvni

    merged = []
    for i in kandidati:
        merged = merged + i

    # sloucime pole kandidatu vsech policek do jednoho pole

    for i in range(0,len(merged),1):
        merged[i] = len(merged[i])

    # nasledne kazde pole kandidatu nahradime celym cislem, oznacujici jeho delku; nyni tak mame pole 81 celych cisel

    try:
        # nyni najdeme policko, ktere ma minimalne dva kandidaty (abychom odfiltrovali jiz vyresena - ty pozname tak,
        # ze maji nula kandidatu; proto jsme je pri reseni strategiemi tak vehementne mazali); nasledne pozname puvodni
        # policko tak, ze vezmeme celociselny podil 9 a zbytek po deleni 9, cimz ziskame jeho souradnice

        policko = merged.index(min(filter(lambda x: x >= 2, merged)))
        policko = divmod(policko,9)
        return policko

    except ValueError:
        # ve vyjimecnych pripadech se muze stat, ze odpovidajici policko nenajdeme; to v pripade, ze je sudoku jiz
        # vyreseno; proto muzeme vratit jakekoli souradnice, na to uz se nikdo ptat nebude

        return [-1,-1]

def bruteForce(reseni,pocetReseni):
    # nejzajimavejsi a zaroven nejkomplikovanejsi cast celeho algoritmu; hrubou silou vyresi cele sudoku

    toReturn = [] # to, co budeme vracet
    hloubka = 0 # indikator hloubky
    cesta = [0] # indikator, kde jsme na te ktere krizovatce odbocili
    mezipamet = [deepcopy(reseni)] # nez zacneme cokoli delat, tak si ulozime vstupni sudoku, ktere je zarucene spravne

    while True:

        # a muzeme se pustit do reseni; cyklus hrube sily bude probihat do te doby, nez se sudoku vyresi, pripadne bude
        # jasne, ze nema reseni; to pozname tak, ze zjistime, ze vstupni sudoku je zarucene chybne, cimz dostaneme spor

        kandidati = inicializovatKandidaty(reseni)
        kandidati = generujKandidaty(kandidati,reseni)
        policko = najdiPolickoProTest(kandidati)

        # vygenerujeme kandidaty, a protoze se sudoku nejdrive resilo pomoci strategii, je jasne, ze logicky krok uz
        # vykonat nelze; proto najdeme vhodne policko, do ktereho zkusime doplnit nejake cislo

        if sudokuVyreseno(reseni):
            # jeste prednim ale zkusime, jestli nahodou nemame sudoku vyresene; v tom pripade si reseni zapiseme a dle
            # prani uzivatele bud hledame dalsi reseni, nebo vratime to, co mame

            toReturn.append(reseni)
            if len(toReturn) == pocetReseni:
                return toReturn

        while cesta[hloubka] > len(kandidati[policko[0]][policko[1]])-1:
            # tento while cyklus v podstate navazuje az na uplny konec hlavniho while cyklu, z duvodu spravne funkcnosti
            # se ale musi vykonat zde; proto by bylo dobre dojet az na konec, a potom se k tomuto cyklu pri cteni kodu
            # vratit

            # pokud jsme zjistili, ze v dane hloubce vsechny moznosti doplneni policka vedou do pasti, potom vznikla
            # chyba uz nekde drive; proto posledni sudoku prohlasene za spravne vymazeme, snizime hloubku o 1, obnovime
            # z mezipameti sudoku ulozene pro tuto hloubku a zkusime nasledujiciho kandidata v teto hloubce

            del(mezipamet[hloubka])
            del(cesta[hloubka])
            hloubka = hloubka - 1

            # pokud se dostaneme do hloubky -1, tak to znamena, ze uvodni sudoku je chybne, a tudiz dostaneme spor;
            # sudoku nema tudiz reseni

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

        # doplnime vybrane policko tim kandidatem, ktery je v seznamu kandidatu policka nejvice nalevo a zaroven zde
        # jeste nebyl; toto kontroluje promenna cesta[hloubka]

        # nyni zkusime sudoku resit dle strategii a prozatim se k nemu chovat, jako kdyby nebylo spravne; jelikoz je
        # strategie Naked Single casove mnohem lepsi nez Hidden Single, budeme ji preferovat; dokud se budou dit nejake
        # zmeny, budeme pouzivat pouze Naked Single; kdyz se potom setkame s neuspechem, pouzijeme jednou Hidden Single
        # a nasledne opet Naked Single, dokud se deji zmeny; kdyz uz ani jedna strategie nezabere, mame hotovo

        sudokuBef = None
        candBef = None
        nemaReseni = False
        nemaReseni2 = False

        while sudokuBef != reseni or candBef != kandidati:
            while sudokuBef != reseni or candBef != kandidati:

                sudokuBef = deepcopy(reseni)
                candBef = deepcopy(kandidati)
                vysl = nakedSingle(kandidati,reseni)
                kandidati = vysl[0]
                reseni = vysl[1]
                nemaReseni2 = vysl[2]
                kandidati = generujKandidaty(kandidati,reseni)

            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = hiddenSingle(kandidati,reseni)
            kandidati = vysl[0]
            reseni = vysl[1]
            nemaReseni = vysl[2]
            kandidati = generujKandidaty(kandidati,reseni)

        # zde jsme skoncili s logickym lustenim; pokud se stale zda, ze by sudoku mohlo mit reseni, prohlasime jej za
        # spravne; pro danou hloubku si jej ulozime do mezipameti, zvysime hloubku a budeme testovat opet od
        # prvniho kandidata nasledujiciho policka

        if nemaReseni == False and nemaReseni2 == False:
            hloubka = hloubka + 1
            mezipamet.append(deepcopy(reseni))
            cesta.append(0)
            continue

        # kdyz zjistime, ze doplnenim cisla jsme vytvorili chybu, tak si poznacime, ze zustaneme ve stejne hloubce,
        # akorat zkusime nasledujiciho kandidata

        else:
            reseni = mezipamet[hloubka]
            cesta[hloubka] = cesta[hloubka] + 1
            continue

    return toReturn

def solvePC(zad,pocetReseni=1,bf=True):
    #################POVINNA HLAVICKA######################
    cas = time()
    zadani = deepcopy(zad)
    reseni = deepcopy(zadani)
    kandidati = inicializovatKandidaty(reseni)
    kandidati = generujKandidaty(kandidati,reseni)
    #################POVINNA HLAVICKA######################

    # nejdriv inicializujeme uvodni kandidaty a mereni casu, potom se pustime do reseni sudoku

    if not zkontrolovatVstup(zadani):
        return [[],(time()-cas)*1000]

    # pokud neprojde uvodnim testem, tak mame rychle hotovo; v opacnem pripade se pokusime vyresit nejdrive ciste logicky

    sudokuBef = None
    candBef = None
    nemaReseni = False
    nemaReseni2 = False

    while sudokuBef != reseni or candBef != kandidati:
        while sudokuBef != reseni or candBef != kandidati:

            sudokuBef = deepcopy(reseni)
            candBef = deepcopy(kandidati)
            vysl = nakedSingle(kandidati,reseni)
            kandidati = vysl[0]
            reseni = vysl[1]
            nemaReseni2 = vysl[2]
            kandidati = generujKandidaty(kandidati,reseni)

        sudokuBef = deepcopy(reseni)
        candBef = deepcopy(kandidati)
        vysl = hiddenSingle(kandidati,reseni)
        kandidati = vysl[0]
        reseni = vysl[1]
        nemaReseni = vysl[2]
        kandidati = generujKandidaty(kandidati,reseni)

    if nemaReseni or nemaReseni2:
        return [[],(time()-cas)*1000]

    # pokud zjistime, ze nema reseni, tak mame rychle hotovo

    if not sudokuVyreseno(reseni) and bf:
        reseni = bruteForce(reseni,pocetReseni)
    else:
        reseni = [reseni]

    # pokud si uzivatel preje resit hrubou silou, tak sudoku doresime, jinak jej vratime nedoresene; kazdopadne oznamime,
    # jak dlouho procedura bezela

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

    # mame opet uvodni inicializaci kandidatu, krome pripadu, kdy nam uzivatel sam nejaky seznam preda; taky zaceneme
    # merit cas

    pokus = solvePC(zadani)
    if len(pokus[0]) == 0:
        return [[],(time()-cas)*1000,False,True]

    # nejdrive zkusime, zda ma sudoku reseni, to je zakladni predpoklad pro to, abychom jej mohli vubec lustit; potom
    # najdeme pomoci strategii logicky krok a uzivateli dame k dispozici jeho popis; pokud zadny logicky krok nenajdeme,
    # vratime uzivateli nezmenene sudoku

    sudokuBef = None
    candBef = None
    nemaReseni = False
    nemaReseni2 = False

    while sudokuBef != reseni or candBef != kandidati:
        while sudokuBef != reseni or candBef != kandidati:
            if naked_single:
                sudokuBef = deepcopy(reseni)
                candBef = deepcopy(kandidati)
                vysl = nakedSingle(kandidati,reseni,logovatPostup=True)
                kandidati = vysl[0]
                reseni = vysl[1]
                nemaReseni2 = vysl[2]
                if vysl[3] != []:
                    postup.append(vysl[3])
                    return [postup,(time()-cas)*1000,True,True]
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

        if nemaReseni or nemaReseni2:
            return [[],(time()-cas)*1000,False,True]

    if not sudokuVyreseno(reseni):
        return [postup,(time()-cas)*1000,True,False]

