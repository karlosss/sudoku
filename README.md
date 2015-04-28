# SuSol

Solver a generátor sudoku, implementovaný do aplikace pro všechny nadšence sudoku

- **Ukázka:** [screenshoty](https://github.com/karlosss/sudoku/blob/master/screenshoty)
- **Download:** aktuální release [zde](https://github.com/karlosss/sudoku/archive/SuSol.zip)
- **Dokumentace:** [popis algoritmů](https://github.com/karlosss/sudoku/blob/master/anotace.pdf) (pdf),  [programátorská dokumentace](https://github.com/karlosss/sudoku/blob/master/dokumentace.pdf) (pdf), [manuál](https://github.com/karlosss/sudoku/blob/master/man/manual.html) (html)
- **Repozitář:** [karlosss/sudoku](https://github.com/karlosss/sudoku) + [fork](http://github.com/gjkcz/sudoku) v archivu maturitních prací
- **Autor:** Karel Jílek
- **Maturitní práce 2014/15** na [GJK](https://github.com/gjkcz/gjkcz)

## Dokumentace pro uživatele
Aplikace, která dokáže vyřešit uživatelem zadané sudoku, poradit mu při řešení, nebo vygeneruje úplně nové a změří řešiteli čas.

Intuitivní ovládání vás (snad) dovede k cíli :). Kdyby ne, v aplikaci je odkaz na manuál.

Další informace [zde](https://github.com/karlosss/sudoku/blob/master/anotace.pdf).
### Instalace
- Na Linuxu nainstalovat balíčky "pyqt4-common", "python2-pyqt4" a "python2"
- Na Windows nainstalovat Python [zde](http://www.python.org/download/releases/2.7) a PyQt dle návodu [zde](http://riverbankcomputing.co.uk/software/pyqt/download)

### Spuštění
Pythonem spustit SuSol.py

## Dokumentace pro programátory
Algoritmy pro solver a generátor jsou poměrně variabilní, stačí pouze dodržet formu, kdy na vstup jde matice 9x9 představující sudoku (0 je prázdné políčko) a na výstup jde totožný datový typ stejného rozměru.

Implementované funkce jsou zdokumentovány [zde](https://github.com/karlosss/sudoku/blob/master/dokumentace.pdf).

### Development 
Zdrojové kódy (soubory.py) se dají otevřít ve vhodném IDE (osobně používám PyCharm) a editovat. Doporučuji zasahovat pouze do souborů "solver2.py" a "generator.py", ostatní jsou poměrně komplikované a hrozí nevratné narušení funkčnosti (mně už se to stalo, naštěstí máme git :) ). Vše se potom musí interpretovat Pythonem 2.x.

### Struktura kódu
Kód je rozdělený na solver, generátor a všechno ostatní (GUI, databáze a některé banální algoritmy dohromady - typicky například kontrola chyb v sudoku); některé funkce GUI jsou zvlášť v souboru misc.py

Další informace [zde](https://github.com/karlosss/sudoku/blob/master/dokumentace.pdf).

## Screenshoty, obrázky
Úvodní obrazovka
![Alt text](https://github.com/karlosss/sudoku/blob/master/screenshoty/screen1.png)

Zadávání sudoku
![Alt text](https://github.com/karlosss/sudoku/blob/master/screenshoty/screen2.png)

Řešení sudoku s použití podbarvování
![Alt text](https://github.com/karlosss/sudoku/blob/master/screenshoty/screen3.png)

Vyřešené sudoku s pomocí počítače
![Alt text](https://github.com/karlosss/sudoku/blob/master/screenshoty/screen4.png)

Výběr z databáze
![Alt text](https://github.com/karlosss/sudoku/blob/master/screenshoty/screen5.png)

