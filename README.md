SuSol
======

Changelog:

dne 14. 10. do GUI lze zapisovat sudoku pomocí klávesnice, vymyšleno jméno: SUdokuSOLver = SuSol

dne 9. 10. zahájena tvorba GUI, budoucnost webkamery zatím nejistá

dne 7. 10. přidán changelog


Sudoku solver, generátor, OCR, encyklopedie strategií a vůbec všechno možné :)
Současná verze je zatím pouze solverem, zato však se 100% úspěšností a časem v nejhorších případech okolo 400 ms, standardně však kolem 50 ms.

Algoritmus funguje následovně: vezme zadání a pro nevyplněná políčka vygeneruje všechny kandidáty, tj. čísla, která nejsou v témže řádku, sloupci ani čtverci zastoupena. Následně se podívá, zda v nějakém políčku není pouze jediný kandidát. Pokud ano, onen kandidát se prohlásí za řešení daného políčka a nakládá se s ním stejně, jako kdyby byl doplněn již v zadání. Následně se celý postup opakuje tak dlouho, dokud se tvoří nová řešení.

To, co ze zadání není na první pohled jednoznačné, se vyřeší ve druhém kroku - metodou BruteForce. Ta funguje na základě upraveného DFS algoritmu: jede se po řádcích zleva doprava do doby, než se najde první nejednoznačné políčko, tj. políčko s více než jedním kandidátem. Následně se do políčka doplní první možný kandidát a provede se test, zda někde nedošlo ke sporu. Pokud ne, políčko se dočasně prohlásí za správně vyplněné a přistoupí se k dalšímu nejbližšímu nejednoznačnému políčku, kde se opět provede to samé. V případě, že daný kandidát způsobí konflikt, dosadí se do políčka druhý možný kandidát a kontrola se opakuje. Pokud se stane, že všichni kandidáti daného políčka způsobují konflikty, předchozí políčko přestane být považováno za správné a zkusí se do něj dosadit následující kandidát v seznamu. 

Tímto způsobem mohou nastat dvě věci: Buď se všechna nejednoznačná políčka podaří vyplnit, čímž nalezneme řešení, nebo všichni kandidáti prvního políčka dříve či později působí konflikty, a tedy je dané sudoku neřešitelné.

Program počítá s open-source vývojem, při dodržení formy zápisu kandidátů lze kódovat vlastní strategie: pole kandidátů se oné funkci - strategii předá, ta si jej přepere a následně vyplivne upravený, zjednodušený seznam. Tak vyvíjejte, dostanete čokoládu :)


Program je psaný v jazyce Python.


Karel Jílek
