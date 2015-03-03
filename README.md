SuSol
======

Tákže, vypadá to následovně:

Je to pořád ještě dost velké demo, ale, ačkoli je to s podivem, pár věcí to již zvládne.

Všechno, co je ještě neudělané, je označeno vyskakovacím oknem přímo v aplikaci.
Menu v menubaru nahoře zatím nefunguje, funguje akorát submenu přejít-home a SuSol-konec.
Tlačítko s nápovědou zatím neexistuje.

TODO (maximální priorita):
- všechno, kde je vyskakovací okýnko (až na load z obrázku)
- tooltipy a nápovědy
- hlášky statusbaru
- návod (asi HTML/XML, otevírání prohlížečem)
- databáze, systém ukládání výsledků

DALŠÍ TODO (priorita nahoře nejdůležitější):
- přepsat generátor
- vyrobit programátorskou dokumentaci solveru a generátoru
- napsat balíček do AUR pro archlinux (případně i další distribuce)
- load z obrázku a implementace dalších strategií



INSTALACE
- DEPENDENCIES: Knihovna Qt v systému, její API pro Python (PyQt4), Python 2.x (testováno 2.7)
- následně stáhnout celý projekt a rozbalit (všechny soubory sice nejsou nutné, ale nic se tím nezkazí...bohužel mi nefunguje gitignore na .pyc :( )
- Pythonem 2.x se pouští SuSol.py

![Screenshot](https://raw.githubusercontent.com/karlosss/sudoku/master/screenshot7.png)

Program je psaný v jazyce Python.


Karel Jílek
