SuSol
======

Je tu trochu bordel, přes víkend tu snad uklidím

Changelog:

10. 2. - víceméně finální podoba GUI, je to v Qt a šlape to parádně. Z tréninkového režimu chybí dodělat pár věcí v záložce pomoc počítače (hint, kontrola, krokování postupu), jinak jeho konečná podoba je to, co je k vidění v současném demu (a také na screenshotu). V okně funguje vše až na hlavní menu (to v tom toolbaru nahoře).

TODO: 

- Soutěžní režim (víceméně vychází z toho co už je)
- Ukládání rozřešených sudoku a výsledků někam do databáze a následné filtrování a zobrazování těchto výsledků jako pořadí v programu, díky Kubovi a jeho lekcím SQL by to snad mohlo i fungovat (hotovo není vůbec)
- Režim zadávání, víceméně půjde o jedno dialogové okno, kde se buď ručně naklepe, nebo generátor vygeneruje nové sudoku, jestli zbyde čas, tak ještě zkusím tu OCR
- Dokumentace solveru, který bude použitelný pro developery (počet lidí co ho použijí: 0)
- Encyklopedie implementovaných strategií - viz níže
- Tooltipy - až někdy budu mít kocovinu, tak se do toho pustím :)

ALGORITMY:

- BruteForce solver je hotový, přidal jsem tam ještě heuristiku, čímž se celý proces zrychlil asi o 30% a nejhoršího času pro náhodně generované obtížné sudoku dosahoval něco málo přes 500ms

- Human solver je novinkou, má za úkol vyluštit sudoku bez použití tipování za pomoci "lidských" strategií - zatím implementovány strategie Naked Single, Hidden Single a Naked Pair (takže zatím beta jak prase, beta to asi bude i u maturity, na tomhle mám v plánu pracovat až na závěr)

- Generátor zatím funguje dost náhodně, výsledné sudoku je občas brutálně jednoduché, občas dá zabrat (200ms) i algoritmu. Asi by to chtělo nějak vylepšit, momentálně mě ale nenapadá jak.


<br><br><br><br>

![Screenshot](https://raw.githubusercontent.com/karlosss/sudoku/master/screenshot7.png)

Program je psaný v jazyce Python.


Karel Jílek
