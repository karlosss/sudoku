#coding: utf8

from __future__ import print_function, unicode_literals
from PyQt4 import QtGui, QtCore
from misc import *
from copy import deepcopy
from time import time, localtime, strftime
from sqlite3 import connect
import sys
import solver2
import generator2

db = connect("data.db")
uzivatel = ""

def todo():
    QtGui.QMessageBox.critical(None,"TODO","TODO")


class VysledkyDialog(QtGui.QDialog):

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)

        painter.setPen(QtGui.QColor("#000000"))
        painter.setBrush(QtGui.QColor("#ffffff"))

        painter.drawRect(130,220,250,250)
        for i in range(1,9,1):
            painter.drawLine(130,220+i*250/9,380,220+i*250/9)
            painter.drawLine(130+i*250/9,220,130+i*250/9,470)

        pismo = QtGui.QFont(okno.pismoCeleAplikace)
        pismo.setPixelSize(20)
        painter.setFont(pismo)

        for i in range(0,9,1):
            for j in range(0,9,1):
                if self.aktivniSudoku[j][i] != 0:
                    painter.drawText(130+(i+0.4)*250/9,220+(j+0.85)*250/9,str(self.aktivniSudoku[j][i]))


        painter.setBrush(QtGui.QColor("#000000"))
        for i in range(0,4,1):
            painter.drawRect(130,220+250*i/3,250,2)
            painter.drawRect(130+250*i/3,220,2,250)


        painter.end()

    def acceptDialog(self):
        self.close()
        okno.zadani = deepcopy(self.aktivniSudoku)
        okno.zadaniBackup = deepcopy(self.aktivniSudoku)
        okno.zobrazElementy("reseni")
        okno.update()

    def rejectDialog(self):
        self.close()
        okno.update()

    def vybranRadek(self):
        try:
            cisloRadku = self.tabulka.currentItem().row()
            aktivniID = self.tabulka.item(cisloRadku,0).text()
        except AttributeError:
            aktivniID = 1
        sudoku_z_db = string2sudoku(DB2list(db.execute("SELECT zadani FROM sudoku_soutez WHERE id="+str(aktivniID)))[0])

        for i in range(0,9,1):
            self.aktivniSudoku[i] = deepcopy(sudoku_z_db[i])

        self.update()

    def __init__(self,level):
        super(VysledkyDialog,self).__init__()

        seznam_z_db = wideDB2list(db.execute("SELECT id,cas,uzivatel,obtiznost,datum FROM sudoku_soutez WHERE obtiznost='"+"gen. ("+level+")' ORDER BY cas"))
        db.commit()

        self.aktivniSudoku = [
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

        self.resize(500,500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Výsledky")

        self.tabulka = QtGui.QTableWidget(self)
        self.tabulka.setMinimumWidth(500)
        self.tabulka.setFixedHeight(200)
        self.tabulka.setColumnCount(5)
        self.tabulka.setColumnWidth(0,92)
        self.tabulka.setColumnWidth(1,92)
        self.tabulka.setColumnWidth(2,92)
        self.tabulka.setColumnWidth(3,92)
        self.tabulka.setColumnWidth(4,92)
        self.tabulka.setRowCount(len(seznam_z_db))
        self.tabulka.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabulka.setHorizontalHeaderLabels(["#","Čas","Uživatel","Obtížnost","Datum"])
        self.tabulka.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabulka.setSortingEnabled(True)
        self.tabulka.itemSelectionChanged.connect(self.vybranRadek)
        self.tabulka.cellDoubleClicked.connect(self.acceptDialog)
        self.tabulka.selectRow(0)

        for i in range(0,len(seznam_z_db),1):
            for j in range(0,5,1):
                self.tabulka.setItem(i, j, QtGui.QTableWidgetItem(unicode(seznam_z_db[i][j])))

        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Close,parent=self)
        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)
        tlacitka.move(400,475)

        self.resitStejne = QtGui.QPushButton(self)
        self.resitStejne.setText("Otevřít sudoku v tréninkovém režimu")
        self.resitStejne.move(10,475)
        self.resitStejne.clicked.connect(self.acceptDialog)



class LoadFromDBDialog(QtGui.QDialog):

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)

        painter.setPen(QtGui.QColor("#000000"))
        painter.setBrush(QtGui.QColor("#ffffff"))

        painter.drawRect(130,220,250,250)
        for i in range(1,9,1):
            painter.drawLine(130,220+i*250/9,380,220+i*250/9)
            painter.drawLine(130+i*250/9,220,130+i*250/9,470)

        pismo = QtGui.QFont(okno.pismoCeleAplikace)
        pismo.setPixelSize(20)
        painter.setFont(pismo)

        for i in range(0,9,1):
            for j in range(0,9,1):
                if self.aktivniSudoku[j][i] != 0:
                    painter.drawText(130+(i+0.4)*250/9,220+(j+0.85)*250/9,str(self.aktivniSudoku[j][i]))


        painter.setBrush(QtGui.QColor("#000000"))
        for i in range(0,4,1):
            painter.drawRect(130,220+250*i/3,250,2)
            painter.drawRect(130+250*i/3,220,2,250)


        painter.end()

    def acceptDialog(self):
        self.close()
        okno.zadani = deepcopy(self.aktivniSudoku)
        okno.zadaniBackup = deepcopy(self.aktivniSudoku)
        okno.update()

    def rejectDialog(self):
        self.close()
        okno.update()

    def vybranRadek(self):
        try:
            cisloRadku = self.tabulka.currentItem().row()
            aktivniID = self.tabulka.item(cisloRadku,0).text()
        except AttributeError:
            aktivniID = 1
        sudoku_z_db = string2sudoku(DB2list(db.execute("SELECT zadani FROM sudoku_zadani WHERE id="+str(aktivniID)))[0])

        for i in range(0,9,1):
            self.aktivniSudoku[i] = deepcopy(sudoku_z_db[i])

        self.update()

    def __init__(self):
        super(LoadFromDBDialog,self).__init__()

        seznam_z_db = wideDB2list(db.execute("SELECT id,datum,uzivatel,identifikator,puvod FROM sudoku_zadani"))
        db.commit()

        self.aktivniSudoku = [
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

        self.resize(500,500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Načíst z databáze")

        self.tabulka = QtGui.QTableWidget(self)
        self.tabulka.setMinimumWidth(500)
        self.tabulka.setFixedHeight(200)
        self.tabulka.setColumnCount(5)
        self.tabulka.setColumnWidth(0,92)
        self.tabulka.setColumnWidth(1,92)
        self.tabulka.setColumnWidth(2,92)
        self.tabulka.setColumnWidth(3,92)
        self.tabulka.setColumnWidth(4,92)
        self.tabulka.setRowCount(len(seznam_z_db))
        self.tabulka.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabulka.setHorizontalHeaderLabels(["#","Datum","Uživatel","Identifikátor","Původ"])
        self.tabulka.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabulka.setSortingEnabled(True)
        self.tabulka.itemSelectionChanged.connect(self.vybranRadek)
        self.tabulka.cellDoubleClicked.connect(self.acceptDialog)
        self.tabulka.selectRow(0)

        for i in range(0,len(seznam_z_db),1):
            for j in range(0,5,1):
                self.tabulka.setItem(i, j, QtGui.QTableWidgetItem(unicode(seznam_z_db[i][j])))

        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel,parent=self)
        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)
        tlacitka.move(330,475)

class LoadFromDBDialog2(QtGui.QDialog):

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)

        painter.setPen(QtGui.QColor("#000000"))
        painter.setBrush(QtGui.QColor("#ffffff"))

        painter.drawRect(130,220,250,250)
        for i in range(1,9,1):
            painter.drawLine(130,220+i*250/9,380,220+i*250/9)
            painter.drawLine(130+i*250/9,220,130+i*250/9,470)

        pismo = QtGui.QFont(okno.pismoCeleAplikace)
        pismo.setPixelSize(20)
        painter.setFont(pismo)

        for i in range(0,9,1):
            for j in range(0,9,1):
                if self.aktivniSudoku[j][i] != 0:
                    painter.setPen(QtGui.QColor("#000000"))
                    painter.drawText(130+(i+0.4)*250/9,220+(j+0.85)*250/9,str(self.aktivniSudoku[j][i]))
                if self.predtimDoplneno[j][i] != 0:
                    painter.setPen(QtGui.QColor("#0000ff"))
                    painter.drawText(130+(i+0.4)*250/9,220+(j+0.85)*250/9,str(self.predtimDoplneno[j][i]))

        painter.setPen(QtGui.QColor("#000000"))


        painter.setBrush(QtGui.QColor("#000000"))
        for i in range(0,4,1):
            painter.drawRect(130,220+250*i/3,250,2)
            painter.drawRect(130+250*i/3,220,2,250)


        painter.end()

    def acceptDialog(self):
        self.close()
        try:
            cisloRadku = self.tabulka.currentItem().row()
            aktivniID = self.tabulka.item(cisloRadku,0).text()
        except AttributeError:
            aktivniID = 1

        load = wideDB2list(db.execute("SELECT zadani,doplneno,kandidati,barvy,akronymy,poznamky,cas FROM sudoku_rozreseno WHERE id="+str(aktivniID)))[0]

        okno.zadani = string2sudoku(load[0])
        okno.reseni = string2sudoku(load[1])
        okno.kandidati = string2cand(load[2])
        okno.barvy = string2cand(load[3])
        okno.akronymy = string2note(load[4])
        okno.poznamky = string2note(load[5])
        okno.time = string2time(load[6])
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.zobrazElementy("reseni")
        okno.update()

    def rejectDialog(self):
        self.close()
        okno.update()

    def vybranRadek(self):
        try:
            cisloRadku = self.tabulka.currentItem().row()
            aktivniID = self.tabulka.item(cisloRadku,0).text()
        except AttributeError:
            aktivniID = 1

        sudoku_z_db = string2sudoku(DB2list(db.execute("SELECT zadani FROM sudoku_rozreseno WHERE id="+str(aktivniID)))[0])
        reseni_z_db = string2sudoku(DB2list(db.execute("SELECT doplneno FROM sudoku_rozreseno WHERE id="+str(aktivniID)))[0])

        for i in range(0,9,1):
            self.aktivniSudoku[i] = deepcopy(sudoku_z_db[i])
            self.predtimDoplneno[i] = deepcopy(reseni_z_db[i])

        self.update()

    def __init__(self):
        super(LoadFromDBDialog2,self).__init__()

        seznam_z_db = wideDB2list(db.execute("SELECT id,datum,uzivatel,identifikator FROM sudoku_rozreseno WHERE uzivatel='"+unicode(okno.uzivatel)+"'"))
        db.commit()

        pole = []

        for i in range(0,len(seznam_z_db),1):
            zadani = wideDB2list(db.execute("SELECT zadani FROM sudoku_rozreseno WHERE id="+str(seznam_z_db[i][0])))[0][0]
            reseni = wideDB2list(db.execute("SELECT doplneno FROM sudoku_rozreseno WHERE id="+str(seznam_z_db[i][0])))[0][0]
            db.commit()
            pole.append([])

            zadano = 81-zadani.count("0")
            k_reseni = 81-zadano
            reseno = reseni.count("1")+reseni.count("2")+reseni.count("3")+reseni.count("4")+reseni.count("5")+reseni.count("6")+reseni.count("7")+reseni.count("8")+reseni.count("9")
            pomer = str(reseno)+"/"+str(k_reseni)+" ("+str(100*reseno/k_reseni)+"%)"

            pole[i].append(seznam_z_db[i][0])
            pole[i].append(seznam_z_db[i][1])
            pole[i].append(seznam_z_db[i][2])
            pole[i].append(seznam_z_db[i][3])
            pole[i].append(pomer)

        self.aktivniSudoku = [
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

        self.predtimDoplneno = [
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

        self.resize(500,500)
        self.setFixedSize(500,500)
        self.setWindowTitle("Moje sudoku")

        self.tabulka = QtGui.QTableWidget(self)
        self.tabulka.setMinimumWidth(500)
        self.tabulka.setFixedHeight(200)
        self.tabulka.setColumnCount(5)
        self.tabulka.setColumnWidth(0,92)
        self.tabulka.setColumnWidth(1,92)
        self.tabulka.setColumnWidth(2,92)
        self.tabulka.setColumnWidth(3,92)
        self.tabulka.setColumnWidth(4,92)
        self.tabulka.setRowCount(len(seznam_z_db))
        self.tabulka.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabulka.setHorizontalHeaderLabels(["#","Datum","Uživatel","Identifikátor","Doplněno"])
        self.tabulka.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabulka.setSortingEnabled(True)
        self.tabulka.itemSelectionChanged.connect(self.vybranRadek)
        self.tabulka.cellDoubleClicked.connect(self.acceptDialog)
        self.tabulka.selectRow(0)

        for i in range(0,len(seznam_z_db),1):
            for j in range(0,5,1):
                self.tabulka.setItem(i, j, QtGui.QTableWidgetItem(unicode(pole[i][j])))


        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel,parent=self)
        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)
        tlacitka.move(330,475)

class DBInsertDialog(QtGui.QDialog):

    def acceptDialog(self):
        identifikator = unicode(self.entry.text())
        db.execute("INSERT INTO sudoku_zadani VALUES(NULL,'"+unicode(identifikator)+"','"+unicode(okno.uzivatel)+"','"+unicode(okno.puvod)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()

    def rejectDialog(self):
        self.close()
        okno.reject1 = True

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.acceptDialog()
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.rejectDialog()

    def __init__(self):
        super(DBInsertDialog,self).__init__()

        self.setWindowTitle("Uložit do databáze")
        self.resize(300,300)

        self.label = QtGui.QLabel(self)
        self.label.setText("Identifikátor:")
        self.label.move(50,50)

        self.entry = QtGui.QLineEdit(self)
        self.entry.setMinimumWidth(200)
        self.entry.move(50,100)
        self.entry.setFocus()

        self.label2 =QtGui.QLabel(self)
        self.label2.setText("Hint: Toto sudoku se nenachází v databázi. Pro pokračování musí být uloženo, aby k němu potom bylo možno v budoucnosti přistupovat.")
        self.label2.setWordWrap(True)
        self.label2.move(50,150)

        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel,parent=self)
        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)
        tlacitka.move(60,260)

class DBInsertDialog2(QtGui.QDialog):

    def acceptDialog(self):
        identifikator = unicode(self.entry.text())
        db.execute("INSERT INTO sudoku_rozreseno VALUES(NULL,'"+unicode(okno.uzivatel)+"','"+unicode(identifikator)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(sudoku2string(okno.reseni))+"','"+unicode(cand2string(okno.kandidati))+"','"+unicode(cand2string(okno.barvy))+"','"+unicode(note2string(okno.akronymy))+"','"+unicode(note2string(okno.poznamky))+"','"+unicode(okno.cas.text()[5:])+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()

    def rejectDialog(self):
        self.close()
        okno.reject1 = True

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.acceptDialog()
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.rejectDialog()

    def __init__(self):
        super(DBInsertDialog2,self).__init__()

        self.setWindowTitle("Uložit do databáze")
        self.resize(300,300)

        self.label = QtGui.QLabel(self)
        self.label.setText("Identifikátor:")
        self.label.move(50,50)

        self.entry = QtGui.QLineEdit(self)
        self.entry.setMinimumWidth(200)
        self.entry.move(50,100)
        self.entry.setFocus()

        self.label2 =QtGui.QLabel(self)
        self.label2.setText("Hint: Uložte si rozřešené sudoku, abyste jej mohli kdykoli dokončit. Sudoku naleznete v záložce \"Moje sudoku\" pod svým uživatelským jménem.")
        self.label2.setWordWrap(True)
        self.label2.move(50,150)

        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel,parent=self)
        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)
        tlacitka.move(60,260)

class UserSelectDialog(QtGui.QDialog):

    def acceptDialog(self):
        global uzivatel
        self.zabit = False

        if self.rb1.isChecked():
            uzivatel = unicode(self.entry.text())
            seznam_v_db = DB2list(db.execute("SELECT * FROM uzivatele").fetchall())
            if uzivatel in seznam_v_db:
                QtGui.QMessageBox.critical(None,"Chyba","Toto uživatelské jméno již existuje. Zvol si jiné.")
                return False
            db.execute("INSERT INTO uzivatele VALUES ('"+unicode(uzivatel)+"')")
            db.execute("INSERT INTO settings VALUES ('"+unicode(uzivatel)+"','#8888ff','#88ff88','#ff8888','#ffff88','#ff88ff','#88ffff','#880088','#888800','#008888','#ffbbbb','#0000ff','#888888','Arial','1','0','"+unicode(QtGui.QStyleFactory.keys()[0])+"')")

        elif self.rb2.isChecked():
            uzivatel = self.combobox.currentText()
        db.commit()
        try:
            okno.fetchSettings()
        except NameError:
            pass
        self.close()

    def rejectDialog(self):
        exit()

    def closeEvent(self, QCloseEvent):
        if self.zabit:
            exit()

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()

        if key == QtCore.Qt.Key_Return:
            self.acceptDialog()


    def click2(self):
        self.entry.setDisabled(True)
        self.combobox.setDisabled(False)
        self.rb1.setFocus()
        self.combobox.setFocus()


    def click1(self):
        self.entry.setDisabled(False)
        self.combobox.setDisabled(True)
        self.rb2.setFocus()
        self.entry.setFocus()

    def __init__(self):
        super(UserSelectDialog,self).__init__()

        self.zabit = True

        self.resize(300,300)
        self.setWindowTitle("SuSol - Zvolit uživatele")

        self.rb1 = QtGui.QRadioButton(self)
        self.rb1.setText("Založit nového")
        self.rb1.move(0,150)
        self.rb1.clicked.connect(self.click1)

        self.rb2 = QtGui.QRadioButton(self)
        self.rb2.setText("Vybrat existujícího")
        self.rb2.setChecked(True)
        self.rb2.clicked.connect(self.click2)

        self.combobox = QtGui.QComboBox(self)
        seznam_v_db = DB2list(db.execute("SELECT * FROM uzivatele").fetchall())
        for i in range(0,len(seznam_v_db),1):
            self.combobox.addItem(seznam_v_db[i])
        self.combobox.move(50,50)
        self.combobox.setMinimumWidth(200)

        self.entry = QtGui.QLineEdit(self)
        self.entry.move(50,200)
        self.entry.setMinimumWidth(200)
        self.entry.setDisabled(True)

        self.combobox.setFocus()

        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel,parent=self)
        tlacitka.move(115,260)

        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)

class UserSelectDialog2(QtGui.QDialog):

    def acceptDialog(self):
        self.zabit = True
        if self.rb1.isChecked():
            okno.uzivatel = unicode(self.entry.text())
            seznam_v_db = DB2list(db.execute("SELECT * FROM uzivatele").fetchall())
            if okno.uzivatel in seznam_v_db:
                QtGui.QMessageBox.critical(None,"Chyba","Toto uživatelské jméno již existuje. Zvol si jiné.")
                return False
            db.execute("INSERT INTO uzivatele VALUES ('"+unicode(okno.uzivatel)+"')")
            db.execute("INSERT INTO settings VALUES ('"+unicode(okno.uzivatel)+"','#8888ff','#88ff88','#ff8888','#ffff88','#ff88ff','#88ffff','#880088','#888800','#008888','#ffbbbb','#0000ff','#888888','Arial','1','0','"+unicode(QtGui.QStyleFactory.keys()[0])+"')")
        elif self.rb2.isChecked():
            okno.uzivatel = self.combobox.currentText()
        okno.mainMenu4.setTitle("&Uživatel: "+okno.uzivatel)

        db.commit()
        okno.fetchSettings()
        self.close()
        okno.update()

    def rejectDialog(self):
        self.close()
        okno.update()

    def click2(self):
        self.entry.setDisabled(True)
        self.combobox.setDisabled(False)
        self.rb1.setFocus()
        self.combobox.setFocus()


    def click1(self):
        self.entry.setDisabled(False)
        self.combobox.setDisabled(True)
        self.rb2.setFocus()
        self.entry.setFocus()

    def __init__(self):
        super(UserSelectDialog2,self).__init__()

        self.resize(300,300)
        self.setWindowTitle("Zvolit uživatele")

        self.rb1 = QtGui.QRadioButton(self)
        self.rb1.setText("Založit nového")
        self.rb1.move(0,150)
        self.rb1.clicked.connect(self.click1)

        self.rb2 = QtGui.QRadioButton(self)
        self.rb2.setText("Vybrat existujícího")
        self.rb2.setChecked(True)
        self.rb2.clicked.connect(self.click2)

        self.combobox = QtGui.QComboBox(self)
        seznam_v_db = DB2list(db.execute("SELECT * FROM uzivatele").fetchall())
        for i in range(0,len(seznam_v_db),1):
            self.combobox.addItem(seznam_v_db[i])
        self.combobox.move(50,50)
        self.combobox.setMinimumWidth(200)

        self.entry = QtGui.QLineEdit(self)
        self.entry.move(50,200)
        self.entry.setMinimumWidth(200)
        self.entry.setDisabled(True)

        self.combobox.setFocus()

        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel,parent=self)
        tlacitka.move(115,260)

        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)

class ShortNoteDialog(QtGui.QDialog):

    def setTitle(self,title):
        self.setWindowTitle(title)

    def setDefaultText(self,text):
        self.editShortNoteTB.setText(unicode(text))

    def acceptDialog(self):
        self.signal = True
        self.obsah = unicode(self.editShortNoteTB.text())
        if len(self.obsah) > 8:
            warn = QtGui.QMessageBox.warning(None,"Varování","Akronym nemůže být delší než 8 znaků.")
            self.obsah = ""
        elif "|" in self.obsah:
            warn = QtGui.QMessageBox.warning(None,"Varování","Akronym obsahuje nepovolený znak: |")
            self.obsah = ""
        else:
            self.close()

    def rejectDialog(self):
        self.close()

    def __init__(self):
        super(ShortNoteDialog, self).__init__()

        self.obsah = ""
        self.signal = False

        self.resize(250,50)
        layout = QtGui.QVBoxLayout(self)
        self.editShortNoteTB = QtGui.QLineEdit()
        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)

        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)

        layout.addWidget(self.editShortNoteTB)
        layout.addWidget(tlacitka)

class LongNoteDialog(QtGui.QDialog):

    def setTitle(self,title):
        self.setWindowTitle(title)

    def setDefaultText(self,text):
        self.editLongNoteTB.setText(text)

    def acceptDialog(self):
        self.signal = True
        self.obsah = unicode(self.editLongNoteTB.toPlainText())
        if "|" in self.obsah:
            warn = QtGui.QMessageBox.warning(None,"Varování","Poznámka obsahuje nepovolený znak: |")
            self.obsah = ""
        else:
            self.close()

    def rejectDialog(self):
        self.close()

    def __init__(self):
        super(LongNoteDialog,self).__init__()

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Return"),self,self.acceptDialog)

        self.obsah = ""
        self.signal = False

        self.resize(250,250)
        layout = QtGui.QVBoxLayout(self)
        self.editLongNoteTB = QtGui.QTextEdit()
        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)

        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.rejectDialog)

        layout.addWidget(self.editLongNoteTB)
        layout.addWidget(tlacitka)

class RemoveColorDialog(QtGui.QDialog):

    def click1(self):
        self.color1.setText("x")
        self.color1.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click2(self):
        self.color2.setText("x")
        self.color2.setChecked(True)
        self.color1.setText("")
        self.color1.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click3(self):
        self.color3.setText("x")
        self.color3.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color1.setText("")
        self.color1.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click4(self):
        self.color4.setText("x")
        self.color4.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color1.setText("")
        self.color1.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click5(self):
        self.color5.setText("x")
        self.color5.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color1.setText("")
        self.color1.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click6(self):
        self.color6.setText("x")
        self.color6.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color1.setText("")
        self.color1.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click7(self):
        self.color7.setText("x")
        self.color7.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color1.setText("")
        self.color1.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click8(self):
        self.color8.setText("x")
        self.color8.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color1.setText("")
        self.color1.setChecked(False)
        self.color9.setText("")
        self.color9.setChecked(False)

    def click9(self):
        self.color9.setText("x")
        self.color9.setChecked(True)
        self.color2.setText("")
        self.color2.setChecked(False)
        self.color3.setText("")
        self.color3.setChecked(False)
        self.color4.setText("")
        self.color4.setChecked(False)
        self.color5.setText("")
        self.color5.setChecked(False)
        self.color6.setText("")
        self.color6.setChecked(False)
        self.color7.setText("")
        self.color7.setChecked(False)
        self.color8.setText("")
        self.color8.setChecked(False)
        self.color1.setText("")
        self.color1.setChecked(False)

    def provest1(self):
        obsah = unicode(self.entry.text())

        if len(obsah) != 2:
            warn = QtGui.QMessageBox.warning(None,"Varování","Neplatné souřadnice políčka.")
            return False
        pism = alpha2num(obsah[0])
        if pism == -1:
            warn = QtGui.QMessageBox.warning(None,"Varování","Neplatné souřadnice políčka.")
            return False
        cis = obsah[1]
        if cis not in ("1","2","3","4","5","6","7","8","9"):
            warn = QtGui.QMessageBox.warning(None,"Varování","Neplatné souřadnice políčka.")
            return False

        cis = int(cis)

        okno.barvy[pism][cis-1] = [0,0,0,0,0,0,0,0,0]
        okno.upravitWidgety()
        okno.update()

    def provest2(self):
        if self.color1.isChecked():
            click = 0
        elif self.color2.isChecked():
            click = 1
        elif self.color3.isChecked():
            click = 2
        elif self.color4.isChecked():
            click = 3
        elif self.color5.isChecked():
            click = 4
        elif self.color6.isChecked():
            click = 5
        elif self.color7.isChecked():
            click = 6
        elif self.color8.isChecked():
            click = 7
        elif self.color9.isChecked():
            click = 8

        for i in range(0,9,1):
            for j in range(0,9,1):
                okno.barvy[i][j][click] = 0

        okno.upravitWidgety()
        okno.update()


    def __init__(self):
        super(RemoveColorDialog,self).__init__()

        self.resize(300,250)
        self.setWindowTitle("Odstranit barvu")
        layout = QtGui.QGridLayout(self)

        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Close)
        tlacitka.rejected.connect(self.close)

        text1 = QtGui.QLabel()
        text1.setText("Odstranit všechny barvy z políčka")
        self.entry = QtGui.QLineEdit()
        self.entry.setMaximumWidth(40)
        self.entry.setMaxLength(2)
        self.entry.setText(num2alpha(okno.curY)+str(okno.curX+1))
        btn1 = QtGui.QPushButton()
        btn1.setText("Provést")
        btn1.clicked.connect(self.provest1)

        text2 = QtGui.QLabel()
        text2.setText("Odstranit barvu ze všech políček")
        btn2 = QtGui.QPushButton()
        btn2.setText("Provést")
        btn2.clicked.connect(self.provest2)

        self.color1 = QtGui.QPushButton()
        self.color1.setStyleSheet("background-color: "+okno.barvyBarev[0]+"; color: #000000")
        self.color1.setMaximumWidth(20)
        self.color1.setCheckable(True)
        self.color1.setChecked(True)
        self.color1.setText("x")
        self.color1.clicked.connect(self.click1)
        self.color2 = QtGui.QPushButton()
        self.color2.setStyleSheet("background-color: "+okno.barvyBarev[1]+"; color: #000000")
        self.color2.setMaximumWidth(20)
        self.color2.setCheckable(True)
        self.color2.clicked.connect(self.click2)
        self.color3 = QtGui.QPushButton()
        self.color3.setStyleSheet("background-color: "+okno.barvyBarev[2]+"; color: #000000")
        self.color3.setMaximumWidth(20)
        self.color3.setCheckable(True)
        self.color3.clicked.connect(self.click3)
        self.color4 = QtGui.QPushButton()
        self.color4.setStyleSheet("background-color: "+okno.barvyBarev[3]+"; color: #000000")
        self.color4.setMaximumWidth(20)
        self.color4.setCheckable(True)
        self.color4.clicked.connect(self.click4)
        self.color5 = QtGui.QPushButton()
        self.color5.setStyleSheet("background-color: "+okno.barvyBarev[4]+"; color: #000000")
        self.color5.setMaximumWidth(20)
        self.color5.setCheckable(True)
        self.color5.clicked.connect(self.click5)
        self.color6 = QtGui.QPushButton()
        self.color6.setStyleSheet("background-color: "+okno.barvyBarev[5]+"; color: #000000")
        self.color6.setMaximumWidth(20)
        self.color6.setCheckable(True)
        self.color6.clicked.connect(self.click6)
        self.color7 = QtGui.QPushButton()
        self.color7.setStyleSheet("background-color: "+okno.barvyBarev[6]+"; color: #000000")
        self.color7.setMaximumWidth(20)
        self.color7.setCheckable(True)
        self.color7.clicked.connect(self.click7)
        self.color8 = QtGui.QPushButton()
        self.color8.setStyleSheet("background-color: "+okno.barvyBarev[7]+"; color: #000000")
        self.color8.setMaximumWidth(20)
        self.color8.setCheckable(True)
        self.color8.clicked.connect(self.click8)
        self.color9 = QtGui.QPushButton()
        self.color9.setStyleSheet("background-color: "+okno.barvyBarev[8]+"; color: #000000")
        self.color9.setMaximumWidth(20)
        self.color9.setCheckable(True)
        self.color9.clicked.connect(self.click9)


        layout.addWidget(text1,0,0,1,9)
        layout.addWidget(self.entry,0,9,1,1)
        layout.addWidget(btn1,1,9,1,1)
        layout.addWidget(text2,2,0,1,9)
        layout.addWidget(self.color1,3,0)
        layout.addWidget(self.color2,3,1)
        layout.addWidget(self.color3,3,2)
        layout.addWidget(self.color4,3,3)
        layout.addWidget(self.color5,3,4)
        layout.addWidget(self.color6,3,5)
        layout.addWidget(self.color7,3,6)
        layout.addWidget(self.color8,3,7)
        layout.addWidget(self.color9,3,8)
        layout.addWidget(btn2,3,9)
        layout.addWidget(QtGui.QWidget(),4,0)
        layout.addWidget(tlacitka,30,0,1,10)

class ColorSettingsDialog(QtGui.QDialog):

    def click1(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[0] = barva
            self.but1.setStyleSheet("background-color: "+self.tempColors[0])
            self.update()

    def click2(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[1] = barva
            self.but2.setStyleSheet("background-color: "+self.tempColors[1])
            self.update()

    def click3(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[2] = barva
            self.but3.setStyleSheet("background-color: "+self.tempColors[2])
            self.update()

    def click4(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[3] = barva
            self.but4.setStyleSheet("background-color: "+self.tempColors[3])
            self.update()

    def click5(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[4] = barva
            self.but5.setStyleSheet("background-color: "+self.tempColors[4])
            self.update()

    def click6(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[5] = barva
            self.but6.setStyleSheet("background-color: "+self.tempColors[5])
            self.update()

    def click7(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[6] = barva
            self.but7.setStyleSheet("background-color: "+self.tempColors[6])
            self.update()

    def click8(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[7] = barva
            self.but8.setStyleSheet("background-color: "+self.tempColors[7])
            self.update()

    def click9(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempColors[8] = barva
            self.but9.setStyleSheet("background-color: "+self.tempColors[8])
            self.update()

    def click10(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempCursor = barva
            self.but10.setStyleSheet("background-color: "+self.tempCursor)
            self.update()

    def click13(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempDoplneno = barva
            self.but10.setStyleSheet("background-color: "+self.tempDoplneno)
            self.update()

    def click11(self):
        self.tempColors = ["#8888ff","#88ff88","#ff8888","#ffff88","#ff88ff","#88ffff","#880088","#888800","#008888"]
        self.but1.setStyleSheet("background-color: "+self.tempColors[0])
        self.but2.setStyleSheet("background-color: "+self.tempColors[1])
        self.but3.setStyleSheet("background-color: "+self.tempColors[2])
        self.but4.setStyleSheet("background-color: "+self.tempColors[3])
        self.but5.setStyleSheet("background-color: "+self.tempColors[4])
        self.but6.setStyleSheet("background-color: "+self.tempColors[5])
        self.but7.setStyleSheet("background-color: "+self.tempColors[6])
        self.but8.setStyleSheet("background-color: "+self.tempColors[7])
        self.but9.setStyleSheet("background-color: "+self.tempColors[8])
        self.update()

    def click12(self):
        pismo = QtGui.QFontDialog()
        self.font,ok = pismo.getFont()
        self.font = unicode(self.font.key())

        if ok:
            self.font = self.font[:self.font.index(",")]
            self.but12.setText("Nastavit písmo v aplikaci (aktivní: "+self.font+")")

    def click14(self):
        barva = QtGui.QColorDialog.getColor()
        if barva.isValid():
            barva = barva.name()
            self.tempSouradniceColor = barva
            self.but14.setStyleSheet("background-color: "+self.tempSouradniceColor)

    def click15(self):
        self.tempDoplneno = "#0000ff"
        self.tempSouradniceColor = "#888888"
        self.tempSouradnice = True
        self.tempCursor = "#ffbbbb"
        self.font = "Arial"

        self.but10.setStyleSheet("background-color: "+self.tempCursor)
        self.cbox2.setChecked(self.tempSouradnice)
        self.but14.setStyleSheet("background-color: "+self.tempSouradniceColor)
        self.but13.setStyleSheet("background-color: "+self.tempDoplneno)
        self.but12.setText("Změnit písmo v aplikaci (aktivní: Arial)")

    def click16(self):
        self.combobox.setCurrentIndex(0)
        self.styl = QtGui.QStyleFactory.keys()[0]









    def toggle(self):
        if self.cbox.isChecked():
            self.tempAutoColor = True
        else:
            self.tempAutoColor = False

    def toggle2(self):
        self.tempSouradnice = self.cbox2.isChecked()

    def zmenStyl(self,x):
        self.styl = self.combobox.currentText()

    def applyDialog(self,x):
        try:
            if x.text() != "Apply":
                return False
        except AttributeError:
            pass

        db.execute("UPDATE settings SET barva1='"+unicode(self.tempColors[0])+"',barva2='"+unicode(self.tempColors[1])+"',barva3='"+unicode(self.tempColors[2])+"',barva4='"+unicode(self.tempColors[3])+"',barva5='"+unicode(self.tempColors[4])+"',barva6='"+unicode(self.tempColors[5])+"',barva7='"+unicode(self.tempColors[6])+"',barva8='"+unicode(self.tempColors[7])+"',barva9='"+unicode(self.tempColors[8])+"',kurzor='"+unicode(self.tempCursor)+"',doplneno='"+unicode(self.tempDoplneno)+"',souradnice='"+unicode(self.tempSouradniceColor)+"',font='"+unicode(self.font)+"',cbsouradnice='"+unicode(int(self.tempSouradnice))+"',cbkandidati='"+unicode(int(self.tempAutoColor))+"',styl='"+unicode(self.styl)+"' WHERE uzivatel='"+unicode(okno.uzivatel)+"'")
        db.commit()

        okno.barvyBarev = deepcopy(self.tempColors)
        okno.barvaKurzoru = self.tempCursor
        okno.autoColor = self.tempAutoColor
        okno.pismoCeleAplikace = self.font
        okno.barvaDoplnenychCisel = self.tempDoplneno
        okno.zobrazitSouradnice = self.tempSouradnice
        okno.barvaSouradnicPolicek = self.tempSouradniceColor
        app.setStyle(QtGui.QStyleFactory.create(self.styl))
        try:
            okno.upravitWidgety()
        except AttributeError:
            pass

        okno.tabs.hide()
        if okno.rezim == "na_cas":
            okno.tabsNaCas()
        elif okno.rezim == "zadavani":
            okno.tabsZadavani()
        elif okno.rezim == "reseni":
            okno.tabsReseni()



        okno.fetchSettings()
        okno.update()

    def acceptDialog(self):
        self.applyDialog(None)
        self.close()

    def __init__(self):
        super(ColorSettingsDialog, self).__init__()

        self.styl = okno.styl

        self.font = okno.pismoCeleAplikace
        self.tempDoplneno = okno.barvaDoplnenychCisel

        self.tempColors = deepcopy(okno.barvyBarev)
        self.tempCursor = okno.barvaKurzoru
        self.tempSouradniceColor = okno.barvaSouradnicPolicek

        self.setWindowTitle("Nastavení")
        self.resize(400,500)

        self.cbox = QtGui.QCheckBox()
        self.cbox.setText("Automaticky zabarvovat dle kandidátů")
        self.cbox.toggled.connect(self.toggle)
        self.cbox.setChecked(okno.autoColor)
        self.tempAutoColor = self.cbox.isChecked()

        self.but1 = QtGui.QPushButton()
        self.but1.setStyleSheet("color: #000000; background-color: "+self.tempColors[0])
        self.but1.setText("Změnit barvu 1")
        self.but1.clicked.connect(self.click1)
        self.but2 = QtGui.QPushButton()
        self.but2.setStyleSheet("color: #000000; background-color: "+self.tempColors[1])
        self.but2.setText("Změnit barvu 2")
        self.but2.clicked.connect(self.click2)
        self.but3 = QtGui.QPushButton()
        self.but3.setStyleSheet("color: #000000; background-color: "+self.tempColors[2])
        self.but3.setText("Změnit barvu 3")
        self.but3.clicked.connect(self.click3)
        self.but4 = QtGui.QPushButton()
        self.but4.setStyleSheet("color: #000000; background-color: "+self.tempColors[3])
        self.but4.setText("Změnit barvu 4")
        self.but4.clicked.connect(self.click4)
        self.but5 = QtGui.QPushButton()
        self.but5.setStyleSheet("color: #000000; background-color: "+self.tempColors[4])
        self.but5.setText("Změnit barvu 5")
        self.but5.clicked.connect(self.click5)
        self.but6 = QtGui.QPushButton()
        self.but6.setStyleSheet("color: #000000; background-color: "+self.tempColors[5])
        self.but6.setText("Změnit barvu 6")
        self.but6.clicked.connect(self.click6)
        self.but7 = QtGui.QPushButton()
        self.but7.setStyleSheet("color: #000000; background-color: "+self.tempColors[6])
        self.but7.setText("Změnit barvu 7")
        self.but7.clicked.connect(self.click7)
        self.but8 = QtGui.QPushButton()
        self.but8.setStyleSheet("color: #000000; background-color: "+self.tempColors[7])
        self.but8.setText("Změnit barvu 8")
        self.but8.clicked.connect(self.click8)
        self.but9 = QtGui.QPushButton()
        self.but9.setStyleSheet("color: #000000; background-color: "+self.tempColors[8])
        self.but9.setText("Změnit barvu 9")
        self.but9.clicked.connect(self.click9)
        self.but11 = QtGui.QPushButton()
        self.but11.setText("Obnovit výchozí")
        self.but11.clicked.connect(self.click11)


        self.but10 = QtGui.QPushButton()
        self.but10.setStyleSheet("color: #000000; background-color: "+self.tempCursor)
        self.but10.setText("Změnit barvu kurzoru")
        self.but10.clicked.connect(self.click10)
        self.but12 = QtGui.QPushButton()
        self.but12.setText("Změnit písmo v aplikaci (aktivní: "+okno.pismoCeleAplikace+")")
        self.but12.clicked.connect(self.click12)
        self.but13 = QtGui.QPushButton()
        self.but13.setStyleSheet("color: #000000; background-color: "+self.tempDoplneno)
        self.but13.setText("Změnit barvu doplněných čísel")
        self.but13.clicked.connect(self.click13)
        self.but14 = QtGui.QPushButton()
        self.but14.setStyleSheet("color: #000000; background-color: "+self.tempSouradniceColor)
        self.but14.setText("Změnit barvu souřadnic políček")
        self.but14.clicked.connect(self.click14)
        self.cbox2 = QtGui.QCheckBox()
        self.cbox2.setText("Zobrazovat souřadnice políček")
        self.cbox2.setChecked(okno.zobrazitSouradnice)
        self.cbox2.toggled.connect(self.toggle2)
        self.tempSouradnice = self.cbox2.isChecked()
        self.but15 = QtGui.QPushButton()
        self.but15.setText("Obnovit výchozí")
        self.but15.clicked.connect(self.click15)
        self.but16 = QtGui.QPushButton()
        self.but16.setText("Obnovit výchozí")
        self.but16.clicked.connect(self.click16)

        self.combobox = QtGui.QComboBox()
        for i in QtGui.QStyleFactory.keys():
            self.combobox.addItem(i)
        self.combobox.activated.connect(self.zmenStyl)

        for i in range(0,len(QtGui.QStyleFactory.keys()),1):
            if QtGui.QStyleFactory.keys()[i] == self.styl:
                self.combobox.setCurrentIndex(i)
                break

        label = QtGui.QLabel()
        label.setWordWrap(True)
        label.setText("Styl aplikace:")



        line = QtGui.QFrame()
        line.setFrameShape(QtGui.QFrame.HLine)
        line.setFrameShadow(QtGui.QFrame.Sunken)

        line2 = QtGui.QFrame()
        line2.setFrameShape(QtGui.QFrame.HLine)
        line2.setFrameShadow(QtGui.QFrame.Sunken)

        line3 = QtGui.QFrame()
        line3.setFrameShape(QtGui.QFrame.HLine)
        line3.setFrameShadow(QtGui.QFrame.Sunken)

        line4 = QtGui.QFrame()
        line4.setFrameShape(QtGui.QFrame.HLine)
        line4.setFrameShadow(QtGui.QFrame.Sunken)

        line5 = QtGui.QFrame()
        line5.setFrameShape(QtGui.QFrame.HLine)
        line5.setFrameShadow(QtGui.QFrame.Sunken)

        line6 = QtGui.QFrame()
        line6.setFrameShape(QtGui.QFrame.HLine)
        line6.setFrameShadow(QtGui.QFrame.Sunken)

        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel,parent=self)
        buttons.rejected.connect(self.close)
        buttons.accepted.connect(self.acceptDialog)
        buttons.clicked.connect(self.applyDialog)
        buttons.move(140,470)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.cbox)
        layout.addWidget(line)
        layout.addWidget(self.but1)
        layout.addWidget(self.but2)
        layout.addWidget(self.but3)
        layout.addWidget(self.but4)
        layout.addWidget(self.but5)
        layout.addWidget(self.but6)
        layout.addWidget(self.but7)
        layout.addWidget(self.but8)
        layout.addWidget(self.but9)
        layout.addWidget(line2)
        layout.addWidget(self.but11)

        layout2 = QtGui.QVBoxLayout()
        layout2.addWidget(self.cbox2)
        layout2.addWidget(line5)
        layout2.addWidget(self.but10)
        layout2.addWidget(self.but13)
        layout2.addWidget(self.but14)
        layout2.addWidget(line4)
        layout2.addWidget(self.but12)
        layout2.addWidget(line3)
        layout2.addWidget(self.but15)

        layout3 = QtGui.QVBoxLayout()
        layout3.addWidget(label)
        layout3.addWidget(self.combobox)
        layout3.addWidget(line6)
        layout3.addWidget(self.but16)
        layout3.addWidget(QtGui.QWidget())

        self.zalozky = QtGui.QTabWidget(self)
        self.zalozky.setFixedWidth(400)
        self.tab1 = QtGui.QWidget()
        self.tab1.setLayout(layout)
        self.tab2 = QtGui.QWidget()
        self.tab2.setLayout(layout2)
        self.tab3 = QtGui.QWidget()
        self.tab3.setLayout(layout3)
        self.zalozky.addTab(self.tab1,"Zabarvování políček")
        self.zalozky.addTab(self.tab2,"Vzhled")
        self.zalozky.addTab(self.tab3,"Styl aplikace")


class TimeSetDialog(QtGui.QDialog):

    def acceptDialog(self):
        okno.time = 3600*self.hodiny.value()+60*self.minuty.value()+self.sekundy.value()
        okno.timeBackup = 3600*self.hodiny.value()+60*self.minuty.value()+self.sekundy.value()
        okno.cas.setText(hms(okno.time))
        okno.upravitWidgety()
        okno.update()
        self.close()

    def __init__(self):
        super(TimeSetDialog,self).__init__()

        self.setWindowTitle("Nastavit čas")
        self.resize(300,150)

        self.hodiny = QtGui.QSpinBox()
        self.minuty = QtGui.QSpinBox()
        self.minuty.setRange(0,59)
        self.sekundy = QtGui.QSpinBox()
        self.sekundy.setRange(0,59)

        h = okno.time // 3600
        m = (okno.time-h*3600) // 60
        s = okno.time-h*3600-m*60

        self.hodiny.setValue(h)
        self.minuty.setValue(m)
        self.sekundy.setValue(s)

        cas = QtGui.QLabel("Čas:")
        d1 = QtGui.QLabel("  :  ")
        d2 = QtGui.QLabel("  :  ")

        layout = QtGui.QGridLayout(self)
        tlacitka = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)

        tlacitka.accepted.connect(self.acceptDialog)
        tlacitka.rejected.connect(self.close)

        layout.addWidget(cas,0,0)
        layout.addWidget(self.hodiny,0,1)
        layout.addWidget(d1,0,2)
        layout.addWidget(self.minuty,0,3)
        layout.addWidget(d2,0,4)
        layout.addWidget(self.sekundy,0,5)
        layout.addWidget(tlacitka,1,3,1,6)

class GeneratorDialog(QtGui.QDialog):

    def lehkeClick(self):
        okno.zadani = generator2.generate(limit=40,bf=False)
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (lehké)"
        db.execute("INSERT INTO sudoku_zadani VALUES(NULL,'"+unicode("_tréninkové")+"','"+unicode(okno.uzivatel)+"','"+unicode(okno.puvod)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()
        okno.zobrazElementy("reseni")

    def stredniClick(self):
        okno.zadani = generator2.generate(bf=False)
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (střední)"
        db.execute("INSERT INTO sudoku_zadani VALUES(NULL,'"+unicode("_tréninkové")+"','"+unicode(okno.uzivatel)+"','"+unicode(okno.puvod)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()
        okno.zobrazElementy("reseni")

    def tezkeClick(self):
        okno.zadani = generator2.generate()
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (těžké)"
        db.execute("INSERT INTO sudoku_zadani VALUES(NULL,'"+unicode("_tréninkové")+"','"+unicode(okno.uzivatel)+"','"+unicode(okno.puvod)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()
        okno.zobrazElementy("reseni")

    def vlastniClick(self):
        okno.zadaniBackup = deepcopy(okno.zadani)
        self.close()
        okno.zobrazElementy("reseni")

    def __init__(self):
        super(GeneratorDialog,self).__init__()

        self.setWindowTitle("Vygenerovat")
        self.resize(600,300)

        pismo = QtGui.QFont(okno.pismoCeleAplikace)
        pismo.setPixelSize(25)

        layout = QtGui.QGridLayout(self)
        obtiznost = QtGui.QLabel("Vygeneruji nové sudoku. Zvol si obtížnost:")
        obtiznost.setFont(pismo)

        self.lehke = QtGui.QPushButton()
        self.lehke.setText("Lehké")
        self.lehke.setFont(pismo)
        self.lehke.setMinimumWidth(150)
        self.lehke.setMinimumHeight(150)
        self.lehke.setMaximumWidth(150)
        self.lehke.setMaximumHeight(150)
        self.lehke.clicked.connect(self.lehkeClick)

        self.stredni = QtGui.QPushButton()
        self.stredni.setText("Střední")
        self.stredni.setFont(pismo)
        self.stredni.setMinimumWidth(150)
        self.stredni.setMinimumHeight(150)
        self.stredni.setMaximumWidth(150)
        self.stredni.setMaximumHeight(150)
        self.stredni.clicked.connect(self.stredniClick)

        self.tezke = QtGui.QPushButton()
        self.tezke.setText("Těžké")
        self.tezke.setFont(pismo)
        self.tezke.setMinimumWidth(150)
        self.tezke.setMinimumHeight(150)
        self.tezke.setMaximumWidth(150)
        self.tezke.setMaximumHeight(150)
        self.tezke.clicked.connect(self.tezkeClick)

        self.vlastni = QtGui.QPushButton()
        self.vlastni.setText("Vlastní")
        self.vlastni.setFont(pismo)
        self.vlastni.setMinimumWidth(150)
        self.vlastni.setMinimumHeight(150)
        self.vlastni.setMaximumWidth(150)
        self.vlastni.setMaximumHeight(150)
        self.vlastni.clicked.connect(self.vlastniClick)


        layout.addWidget(obtiznost,0,0,1,3)
        layout.addWidget(QtGui.QWidget(),1,0)
        layout.addWidget(QtGui.QWidget(),2,0)
        layout.addWidget(QtGui.QWidget(),3,0)
        layout.addWidget(QtGui.QWidget(),4,0)
        layout.addWidget(self.lehke,5,0)
        layout.addWidget(self.stredni,5,1)
        layout.addWidget(self.tezke,5,2)
        layout.addWidget(self.vlastni,5,3)

class GeneratorDialog2(QtGui.QDialog):

    def lehkeClick(self):
        okno.zadani = generator2.generate(limit=40,bf=False)
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (lehké)"
        db.execute("INSERT INTO sudoku_zadani VALUES(NULL,'"+unicode("_soutěžní")+"','"+unicode(okno.uzivatel)+"','"+unicode(okno.puvod)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()
        okno.zobrazElementy("na_cas")


    def stredniClick(self):
        okno.zadani = generator2.generate(bf=False)
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (střední)"
        db.execute("INSERT INTO sudoku_zadani VALUES(NULL,'"+unicode("_soutěžní")+"','"+unicode(okno.uzivatel)+"','"+unicode(okno.puvod)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()
        okno.zobrazElementy("na_cas")

    def tezkeClick(self):
        okno.zadani = generator2.generate()
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (těžké)"
        db.execute("INSERT INTO sudoku_zadani VALUES(NULL,'"+unicode("_soutěžní")+"','"+unicode(okno.uzivatel)+"','"+unicode(okno.puvod)+"','"+unicode(sudoku2string(okno.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
        db.commit()
        self.close()
        okno.zobrazElementy("na_cas")

    def vlastniClick(self):
        print("vlastni")

    def __init__(self):
        super(GeneratorDialog2,self).__init__()

        self.setWindowTitle("Vygenerovat")
        self.resize(600,300)

        pismo = QtGui.QFont(okno.pismoCeleAplikace)
        pismo.setPixelSize(25)

        layout = QtGui.QGridLayout(self)
        obtiznost = QtGui.QLabel("Vygeneruji nové sudoku. Zvol si obtížnost:")
        obtiznost.setFont(pismo)

        self.lehke = QtGui.QPushButton()
        self.lehke.setText("Lehké")
        self.lehke.setFont(pismo)
        self.lehke.setMinimumWidth(150)
        self.lehke.setMinimumHeight(150)
        self.lehke.setMaximumWidth(150)
        self.lehke.setMaximumHeight(150)
        self.lehke.clicked.connect(self.lehkeClick)

        self.stredni = QtGui.QPushButton()
        self.stredni.setText("Střední")
        self.stredni.setFont(pismo)
        self.stredni.setMinimumWidth(150)
        self.stredni.setMinimumHeight(150)
        self.stredni.setMaximumWidth(150)
        self.stredni.setMaximumHeight(150)
        self.stredni.clicked.connect(self.stredniClick)

        self.tezke = QtGui.QPushButton()
        self.tezke.setText("Těžké")
        self.tezke.setFont(pismo)
        self.tezke.setMinimumWidth(150)
        self.tezke.setMinimumHeight(150)
        self.tezke.setMaximumWidth(150)
        self.tezke.setMaximumHeight(150)
        self.tezke.clicked.connect(self.tezkeClick)

        self.vlastni = QtGui.QPushButton()
        self.vlastni.setText("Vlastní")
        self.vlastni.setFont(pismo)
        self.vlastni.setMinimumWidth(150)
        self.vlastni.setMinimumHeight(150)
        self.vlastni.setMaximumWidth(150)
        self.vlastni.setMaximumHeight(150)
        self.vlastni.clicked.connect(self.vlastniClick)


        layout.addWidget(obtiznost,0,0,1,3)
        layout.addWidget(QtGui.QWidget(),1,0)
        layout.addWidget(QtGui.QWidget(),2,0)
        layout.addWidget(QtGui.QWidget(),3,0)
        layout.addWidget(QtGui.QWidget(),4,0)
        layout.addWidget(self.lehke,5,0)
        layout.addWidget(self.stredni,5,1)
        layout.addWidget(self.tezke,5,2)
        layout.addWidget(self.vlastni,5,3)

class GeneratorDialog3(QtGui.QDialog):

    def lehkeClick(self):
        okno.zadani = generator2.generate(limit=40,bf=False)
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (lehké)"
        self.close()

    def stredniClick(self):
        okno.zadani = generator2.generate(bf=False)
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (střední)"
        self.close()

    def tezkeClick(self):
        okno.zadani = generator2.generate()
        okno.zadaniBackup = deepcopy(okno.zadani)
        okno.puvod = "gen. (těžké)"
        self.close()

    def vlastniClick(self):
        todo()

    def __init__(self):
        super(GeneratorDialog3,self).__init__()

        self.setWindowTitle("Vygenerovat")
        self.resize(600,300)

        pismo = QtGui.QFont(okno.pismoCeleAplikace)
        pismo.setPixelSize(25)

        layout = QtGui.QGridLayout(self)
        obtiznost = QtGui.QLabel("Vygeneruji nové sudoku. Zvol si obtížnost:")
        obtiznost.setFont(pismo)

        self.lehke = QtGui.QPushButton()
        self.lehke.setText("Lehké")
        self.lehke.setFont(pismo)
        self.lehke.setMinimumWidth(150)
        self.lehke.setMinimumHeight(150)
        self.lehke.setMaximumWidth(150)
        self.lehke.setMaximumHeight(150)
        self.lehke.clicked.connect(self.lehkeClick)

        self.stredni = QtGui.QPushButton()
        self.stredni.setText("Střední")
        self.stredni.setFont(pismo)
        self.stredni.setMinimumWidth(150)
        self.stredni.setMinimumHeight(150)
        self.stredni.setMaximumWidth(150)
        self.stredni.setMaximumHeight(150)
        self.stredni.clicked.connect(self.stredniClick)

        self.tezke = QtGui.QPushButton()
        self.tezke.setText("Těžké")
        self.tezke.setFont(pismo)
        self.tezke.setMinimumWidth(150)
        self.tezke.setMinimumHeight(150)
        self.tezke.setMaximumWidth(150)
        self.tezke.setMaximumHeight(150)
        self.tezke.clicked.connect(self.tezkeClick)

        self.vlastni = QtGui.QPushButton()
        self.vlastni.setText("Vlastní")
        self.vlastni.setFont(pismo)
        self.vlastni.setMinimumWidth(150)
        self.vlastni.setMinimumHeight(150)
        self.vlastni.setMaximumWidth(150)
        self.vlastni.setMaximumHeight(150)
        self.vlastni.clicked.connect(self.vlastniClick)


        layout.addWidget(obtiznost,0,0,1,3)
        layout.addWidget(QtGui.QWidget(),1,0)
        layout.addWidget(QtGui.QWidget(),2,0)
        layout.addWidget(QtGui.QWidget(),3,0)
        layout.addWidget(QtGui.QWidget(),4,0)
        layout.addWidget(self.lehke,5,0)
        layout.addWidget(self.stredni,5,1)
        layout.addWidget(self.tezke,5,2)
        layout.addWidget(self.vlastni,5,3)

class JineMetodyDialog(QtGui.QDialog):
    def zadatRucne(self):
        okno.zobrazElementy("zadavani")
        okno.puvod = "zadat ručně"
        okno.zadani = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        self.close()

    def databazeClick(self):
        self.close()
        dialog = LoadFromDBDialog()
        dialog.exec_()

    def generatorClick(self):
        self.close()
        dialog = GeneratorDialog3()
        dialog.exec_()

    def __init__(self):
        super(JineMetodyDialog, self).__init__()

        self.setWindowTitle("Metody zadávání")
        self.resize(450,300)

        pismo = QtGui.QFont(okno.pismoCeleAplikace)
        pismo.setPixelSize(25)

        layout = QtGui.QGridLayout(self)
        obtiznost = QtGui.QLabel("Vyber metodu zadávání:")
        obtiznost.setFont(pismo)

        self.generator = QtGui.QPushButton()
        self.generator.setText("Vygenerovat")
        self.generator.setFont(pismo)
        self.generator.setMinimumWidth(150)
        self.generator.setMinimumHeight(150)
        self.generator.setMaximumWidth(150)
        self.generator.setMaximumHeight(150)
        self.generator.clicked.connect(self.generatorClick)

        self.databaze = QtGui.QPushButton()
        self.databaze.setText("Z databáze")
        self.databaze.setFont(pismo)
        self.databaze.setMinimumWidth(150)
        self.databaze.setMinimumHeight(150)
        self.databaze.setMaximumWidth(150)
        self.databaze.setMaximumHeight(150)
        self.databaze.clicked.connect(self.databazeClick)

        self.klavesnice = QtGui.QPushButton()
        self.klavesnice.setText("Zadat ručně")
        self.klavesnice.setFont(pismo)
        self.klavesnice.setMinimumWidth(150)
        self.klavesnice.setMinimumHeight(150)
        self.klavesnice.setMaximumWidth(150)
        self.klavesnice.setMaximumHeight(150)
        self.klavesnice.clicked.connect(self.zadatRucne)


        layout.addWidget(obtiznost,0,0,1,3)
        layout.addWidget(QtGui.QWidget(),1,0)
        layout.addWidget(QtGui.QWidget(),2,0)
        layout.addWidget(QtGui.QWidget(),3,0)
        layout.addWidget(QtGui.QWidget(),4,0)
        # layout.addWidget(self.lehke,5,0)
        layout.addWidget(self.generator,5,1)
        layout.addWidget(self.databaze,5,2)
        layout.addWidget(self.klavesnice,5,3)

class SuSol(QtGui.QMainWindow):

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.ukecanejBanner.move(15,self.frameGeometry().height()-60)
        if self.frameGeometry().width()-30 > 1:
            self.ukecanejBanner.setMinimumWidth(self.frameGeometry().width()-30)
            self.ukecanejBanner.setMaximumWidth(self.frameGeometry().width()-30)
        else:
            self.ukecanejBanner.setMinimumWidth(1)
            self.ukecanejBanner.setMaximumWidth(1)



        if self.rezim in ("welcome_screen"):
            vyska = self.frameGeometry().height()
            sirka = self.frameGeometry().width()

            pismo1 = QtGui.QFont(self.pismoCeleAplikace)
            pismo1.setPixelSize(vyska/5)
            painter.setFont(pismo1)
            fm = QtGui.QFontMetrics(pismo1)
            sirkaTextu = fm.width("SuSol")
            painter.drawText(sirka/2-sirkaTextu/2,vyska/5+vyska/40,"SuSol")

            pismo2 = QtGui.QFont(self.pismoCeleAplikace)
            if vyska/35 > 1:
                pismo2.setPixelSize(vyska/35)
            else:
                pismo2.setPixelSize(1)
            painter.setFont(pismo2)
            fm = QtGui.QFontMetrics(pismo2)
            sirkaTextu = fm.width("Když nemůžeš vyřešit sudoku v novinách, tak ti s tím pomohu")

            while sirkaTextu+(self.frameGeometry().width()/2-sirkaTextu/2)+self.welcomeButton2.width() > self.frameGeometry().width():
                if pismo2.pixelSize() > 1:
                    pismo2.setPixelSize(pismo2.pixelSize()-1)
                else:
                    break
                painter.setFont(pismo2)
                fm = QtGui.QFontMetrics(pismo2)
                sirkaTextu = fm.width("Když nemůžeš vyřešit sudoku v novinách, tak ti s tím pomohu")

            painter.drawText(sirka/2-sirkaTextu/2,vyska/3+vyska/40,"Vítej, člověče!")
            painter.drawText(sirka/2-sirkaTextu/2,vyska/2.2+vyska/20,"Pokud si chceš vyřešit sudoku na čas, klikni")
            painter.drawText(sirka/2-sirkaTextu/2,vyska/2.2+vyska/20*2,"Když nemůžeš vyřešit sudoku v novinách, tak ti s tím pomohu")
            painter.drawText(sirka/2-sirkaTextu/2,vyska/2.2+vyska/20*3,"Když si chceš jen tak potrénovat, tak klikni")
            painter.drawText(sirka/2-sirkaTextu/2,vyska/2.2+vyska/20*4,"Chceš-li si přečíst návod, klikni")
            painter.drawText(sirka/2-sirkaTextu/2,vyska/2.2+vyska/20*5,"Kdyby něco, v menu nahoře je tlačítko s nápovědou.")
            painter.drawText(sirka/2-sirkaTextu/2,vyska/1.2,"Bav se!")

            self.welcomeButton1.resize(fm.width("ahoj"),pismo2.pixelSize())
            self.welcomeButton2.resize(fm.width("ahoj"),pismo2.pixelSize())
            self.welcomeButton3.resize(fm.width("ahoj"),pismo2.pixelSize())
            self.welcomeButton4.resize(fm.width("ahoj"),pismo2.pixelSize())
            sirkaTextu1 = fm.width("Pokud si chceš vyřešit sudoku na čas, klikni ")
            sirkaTextu2 = fm.width("Když nemůžeš vyřešit sudoku v novinách, tak ti s tím pomohu ")
            sirkaTextu3 = fm.width("Když si chceš jen tak potrénovat, tak klikni ")
            sirkaTextu4 = fm.width("Chceš-li si přečíst návod, klikni ")
            self.welcomeButton1.move(sirka/2-sirkaTextu/2+sirkaTextu1,vyska/2.2+vyska/20-self.welcomeButton1.height()+pismo2.pixelSize()/5)
            self.welcomeButton2.move(sirka/2-sirkaTextu/2+sirkaTextu2,vyska/2.2+vyska/20*2-self.welcomeButton2.height()+pismo2.pixelSize()/5)
            self.welcomeButton3.move(sirka/2-sirkaTextu/2+sirkaTextu3,vyska/2.2+vyska/20*3-self.welcomeButton3.height()+pismo2.pixelSize()/5)
            self.welcomeButton4.move(sirka/2-sirkaTextu/2+sirkaTextu4,vyska/2.2+vyska/20*4-self.welcomeButton4.height()+pismo2.pixelSize()/5)







        if self.rezim in ("reseni","na_cas","zadavani"):
            #painter.begin(self)
            Xpos = 10
            Ypos = 30
            margin = 0
            bottom = 80
            right = 300
            strongLineWidthDivisor = 150
            menuMargin = 10

            self.Xpos = Xpos
            self.Ypos = Ypos
            self.margin = margin
            self.bottom = bottom
            self.right = right

            squareSize = min((self.frameGeometry().height()-Ypos-2*margin-bottom)/9,(self.frameGeometry().width()-Xpos-2*margin-right)/9)
            hranice = Xpos-margin+9*squareSize+2*margin+menuMargin

            self.tabs.move(hranice,Ypos+margin)
            if self.frameGeometry().height()-80-Ypos-margin > 480:
                a = 480
            else:
                a = self.frameGeometry().height()-80-Ypos-margin

            self.tabs.resize(280,a)

            if squareSize < 0:
                squareSize = 0

            if Ypos+bottom+2*margin+9*squareSize < self.frameGeometry().height():
                Ypos = Ypos + (self.frameGeometry().height()-(Ypos+bottom+2*margin+9*squareSize))/2
                self.Ypos = Ypos
            painter.setPen(QtGui.QColor("#000000"))
            painter.setBrush(QtGui.QColor("#ffffff"))

            painter.drawRect(Xpos-margin,Ypos-margin,9*squareSize+2*margin,9*squareSize+2*margin)

            for i in range(0,9,1): #ctverecky, barvy a kurzor
                for j in range(0,9,1):

                    painter.setBrush(QtGui.QColor("#ffffff"))
                    painter.drawRect(i*squareSize+Xpos,j*squareSize+Ypos,squareSize,squareSize)

                    if self.rezim not in ("zadavani"):
                        pocetBarev = 0
                        pozice = []
                        for k in range(0,9,1):
                            if self.barvy[j][i][k]*self.zobrazitBarvu[k] == 1:
                                pocetBarev = pocetBarev + 1
                                pozice.append(k)

                        for k in range(0,pocetBarev,1):
                            try:
                                sirka = squareSize/pocetBarev
                            except ZeroDivisionError:
                                break

                            addOn = 0
                            if k == pocetBarev-1:
                                addOn = squareSize-(k+1)*sirka

                            painter.setBrush(QtGui.QColor(self.barvyBarev[pozice[k]]))

                            painter.drawRect(i*squareSize+Xpos+k*sirka,j*squareSize+Ypos,sirka+addOn,squareSize)


                        if self.chyby[j][i] == 1:
                            painter.setBrush(QtGui.QColor(self.barvaChyby))
                            painter.drawRect(i*squareSize+Xpos,j*squareSize+Ypos,squareSize,squareSize)

                        if self.indikace1[j][i] == 1:
                            painter.setBrush(QtGui.QColor("#888833"))
                            painter.drawRect(i*squareSize+Xpos,j*squareSize+Ypos,squareSize,squareSize)

                        if self.indikace3[j][i] == 1:
                            painter.setBrush(QtGui.QColor("#00aa00"))
                            painter.drawRect(i*squareSize+Xpos,j*squareSize+Ypos,squareSize,squareSize)


                    if self.curX == i and self.curY == j and self.candMode == False:
                        painter.setBrush(QtGui.QColor(self.barvaKurzoru))
                        painter.drawRect(i*squareSize+Xpos,(j+1)*squareSize+Ypos,squareSize,-squareSize*0.7)




            if self.candMode: #kurzor na kandidaty
                painter.setBrush(QtGui.QColor(self.barvaKurzoru))
                painter.drawRect(self.curX*squareSize+Xpos,self.curY*squareSize+Ypos,squareSize,squareSize*0.35)
                painter.setBrush(QtGui.QColor("#ffffff"))

            for i in range(0,4,1):
                painter.setPen(QtGui.QColor("#000000"))
                painter.setBrush(QtGui.QColor("#000000"))
                painter.drawRect(i*squareSize*3+Xpos,Ypos,min(self.frameGeometry().width(),self.frameGeometry().height())//strongLineWidthDivisor,9*squareSize+min(self.frameGeometry().width(),self.frameGeometry().height())//strongLineWidthDivisor)
                painter.drawRect(Xpos,i*squareSize*3+Ypos,9*squareSize+min(self.frameGeometry().width(),self.frameGeometry().height())//strongLineWidthDivisor,min(self.frameGeometry().width(),self.frameGeometry().height())//strongLineWidthDivisor)


            pismo = QtGui.QFont(self.pismoCeleAplikace)
            pismo.setWeight(100)
            velikost = 0.7*squareSize
            if velikost < 1:
                velikost = 1
            pismo.setPixelSize(velikost)

            pismo2 = QtGui.QFont(self.pismoCeleAplikace)
            pismo2.setWeight(100)
            velikost = 0.7*squareSize
            if velikost < 1:
                velikost = 1
            pismo2.setPixelSize(velikost)

            pismo3 = QtGui.QFont(self.pismoCeleAplikace)
            velikost = 0.15*squareSize
            if velikost < 1:
                velikost = 1
            pismo3.setPixelSize(velikost)

            pismo4 = QtGui.QFont(self.pismoCeleAplikace)
            velikost = 0.18*squareSize
            if velikost < 1:
                velikost = 1
            pismo4.setPixelSize(velikost)

            pismo5 = QtGui.QFont(self.pismoCeleAplikace)
            velikost = 0.12*squareSize
            if velikost < 1:
                velikost = 1
            pismo5.setPixelSize(velikost)

            pismo6 = QtGui.QFont(self.pismoCeleAplikace)
            velikost = 0.3*squareSize
            if velikost < 1:
                velikost = 1
            pismo6.setPixelSize(velikost)

            for i in range(0,9,1): #cisla ze zadani, cisla z reseni, cisla souradnic policka
                for j in range(0,9,1):
                    if self.zadani[j][i] != 0:
                        painter.setFont(pismo)
                        painter.setPen(QtGui.QColor("#000000"))

                        x = i*squareSize+Xpos+squareSize/2.85
                        y = j*squareSize+Ypos+0.9*squareSize

                        painter.drawText(x,y,str(self.zadani[j][i]))
                    if self.reseni[i][j] != 0 and self.zadani[i][j] == 0 and self.rezim not in ("zadavani"):
                        painter.setFont(pismo2)
                        painter.setPen(QtGui.QColor(self.barvaDoplnenychCisel))

                        x = j*squareSize+Xpos+squareSize/2.85
                        y = i*squareSize+Ypos+0.9*squareSize

                        painter.drawText(x,y,str(self.reseni[i][j]))

                    if self.poznamky[i][j] != "" and self.rezim not in ("zadavani"):
                        x = j*squareSize+Xpos+0.8*squareSize
                        y = i*squareSize+Ypos+0.8*squareSize

                        painter.setFont(pismo6)
                        painter.setPen(QtGui.QColor("#000000"))
                        painter.drawText(x,y,"*")

                    if self.zobrazitSouradnice:
                        painter.setPen(QtGui.QColor(self.barvaSouradnicPolicek))
                        painter.setFont(pismo3)

                        x = j*squareSize+Xpos+squareSize/2.85+squareSize*0.45
                        y = i*squareSize+Ypos+0.9*squareSize
                        painter.drawText(x,y,num2alpha(i)+str(j+1))

                    if self.rezim in ("zadavani"):
                        continue

                    painter.setPen(QtGui.QColor("#000000"))
                    painter.setFont(pismo4)

                    x = j*squareSize+Xpos+0.12*squareSize
                    y = i*squareSize+Ypos+0.9*squareSize-squareSize*0.62

                    painter.drawText(x,y,arr2str(self.kandidati[i][j]))

                    painter.setFont(pismo5)

                    x = j*squareSize+Xpos+0.08*squareSize
                    y = i*squareSize+Ypos+0.9*squareSize+squareSize*0.07

                    painter.drawText(x,y,self.akronymy[i][j])

        painter.end()
        if self.resized:
            self.resized = False
            self.update()


    def resizeEvent(self, QResizeEvent):
        self.resized = True

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()

        if self.rezim in ("reseni","na_cas","zadavani"):
            squareSize = min((self.frameGeometry().height()-self.Ypos-2*self.margin-self.bottom)/9,(self.frameGeometry().width()-self.Xpos-2*self.margin-self.right)/9)

            if (x-self.Xpos)//squareSize >= 0 and (x-self.Xpos)//squareSize < 9 and (y-self.Ypos)//squareSize >= 0 and (y-self.Ypos)//squareSize < 9:
                self.curX = (x-self.Xpos)//squareSize
                self.curY = (y-self.Ypos)//squareSize
                self.chyby[self.curY][self.curX] = 0
                self.indikace1[self.curY][self.curX] = 0
                self.indikace3[self.curY][self.curX] = 0
                string = "ABCDEFGHI"
                self.poleLabel.setText(string[self.curY]+str(self.curX+1))

            self.upravitWidgety()
            self.update()

    def keyPressEvent(self, event):
        key = event.key()

        if self.rezim in ("zadavani","reseni","na_cas"):
            if key == QtCore.Qt.Key_Left: #pohyb sipkami
                self.curX = self.curX - 1
            elif key == QtCore.Qt.Key_Right:
                self.curX = self.curX + 1
            elif key == QtCore.Qt.Key_Up:
                self.curY = self.curY - 1
            elif key == QtCore.Qt.Key_Down:
                self.curY = self.curY + 1

            elif key == QtCore.Qt.Key_1:
                self.doplnCislo(1)
            elif key == QtCore.Qt.Key_2:
                self.doplnCislo(2)
            elif key == QtCore.Qt.Key_3:
                self.doplnCislo(3)
            elif key == QtCore.Qt.Key_4:
                self.doplnCislo(4)
            elif key == QtCore.Qt.Key_5:
                self.doplnCislo(5)
            elif key == QtCore.Qt.Key_6:
                self.doplnCislo(6)
            elif key == QtCore.Qt.Key_7:
                self.doplnCislo(7)
            elif key == QtCore.Qt.Key_8:
                self.doplnCislo(8)
            elif key == QtCore.Qt.Key_9:
                self.doplnCislo(9)

            if self.rezim in ("zadavani","reseni","na_cas"):
                if key == QtCore.Qt.Key_Delete:
                    self.doplnCislo(0)

            if self.rezim in ("reseni","na_cas"):
                if key == QtCore.Qt.Key_Tab:
                    if self.candMode == False:
                        self.candMode = True
                    else:
                        self.candMode = False
                elif key == QtCore.Qt.Key_Delete:
                    if self.candMode == False:
                        self.doplnCislo(0)
                    else:
                        self.smazKandidaty()


            if key == QtCore.Qt.Key_Space and self.rezim in ("reseni"):
                self.startstop()


            self.curX = divmod(self.curX,9)[1]
            self.curY = divmod(self.curY,9)[1]
            self.chyby[self.curY][self.curX] = 0
            self.indikace3[self.curY][self.curX] = 0
            self.indikace1[self.curY][self.curX] = 0
            string = "ABCDEFGHI"
            self.poleLabel.setText(string[self.curY]+str(self.curX+1))
            self.upravitWidgety()
            self.update()


    def startstop(self):
        if not self.casBezi:
            self.casBezi = True
            self.casStartStop.setStyleSheet("background-color: #008800; color: #ffffff")
            self.timestamp = time()
            self.a2.setEnabled(False)
            self.a3.setEnabled(False)
            self.timer.start(1000)
        else:
            self.casBezi = False
            self.casStartStop.setStyleSheet("background-color: #ff0000; color: #ffffff")
            self.timer.stop()
            self.timeBackup = self.time
            self.a2.setEnabled(True)
            self.a3.setEnabled(True)

    def pricitat_cas(self):
        self.time = int(time())-int(self.timestamp)+self.timeBackup
        self.cas.setText(hms(self.time))
        return self.casBezi

    def vynulovat(self):
        self.time = 0
        self.timeBackup = 0
        self.cas.setText("Čas: 0:00:00")
        self.update()

    def nastavitCas(self):
        dialog = TimeSetDialog()
        dialog.exec_()


    def doplnCislo(self,cislo):
        if self.rezim in ("zadavani"):
            self.zadani[self.curY][self.curX] = cislo
            self.puvod = "zadat ručně"
            self.update()
        if self.rezim in ("reseni","na_cas"):
            if self.candMode == False:
                if self.zadani[self.curY][self.curX] == 0:
                    self.reseni[self.curY][self.curX] = cislo
            else:
                if cislo in self.kandidati[self.curY][self.curX]:
                    self.kandidati[self.curY][self.curX].remove(cislo)
                    if self.autoColor:
                        self.barvy[self.curY][self.curX][cislo-1] = 0
                        print(self.barvy)
                else:
                    self.kandidati[self.curY][self.curX].append(cislo)
                    self.kandidati[self.curY][self.curX].sort()
                    if self.autoColor:
                        self.barvy[self.curY][self.curX][cislo-1] = 1
            self.upravitWidgety()
            self.update()

        if self.rezim in ("na_cas") and solver2.sudokuVyreseno(self.doplneno):
            if len(solver2.solvePC(self.doplneno)[0]) == 1:
                self.startstop()
                db.execute("INSERT INTO sudoku_soutez VALUES(NULL,'"+unicode(self.cas.text()[5:])+"','"+unicode(self.uzivatel)+"','"+unicode(self.puvod)[7:-1]+"','"+unicode(sudoku2string(self.zadani))+"','"+unicode(strftime("%Y-%m-%d %H:%M:%S", localtime()))+"')")
                db.commit()
                QtGui.QMessageBox.information(None,"Info","Sudoku úspěšně vyřešeno! Stisknutím OK se vrátíte na úvodní obrazovku.")
                okno.zobrazElementy("welcome_screen")





    def smazKandidaty(self):
        self.kandidati[self.curY][self.curX]= []
        if self.autoColor:
            self.barvy[self.curY][self.curX] = [0,0,0,0,0,0,0,0,0]

        self.update()

    def quit(self):
        self.close()

    def click1(self,x):
        if x:
            self.color1.setText("x")
            self.barvy[self.curY][self.curX][0] = 1
        else:
            self.color1.setText("")
            self.barvy[self.curY][self.curX][0] = 0
        self.update()

    def click2(self,x):
        if x:
            self.color2.setText("x")
            self.barvy[self.curY][self.curX][1] = 1
        else:
            self.color2.setText("")
            self.barvy[self.curY][self.curX][1] = 0
        self.update()

    def click3(self,x):
        if x:
            self.color3.setText("x")
            self.barvy[self.curY][self.curX][2] = 1
        else:
            self.color3.setText("")
            self.barvy[self.curY][self.curX][2] = 0
        self.update()

    def click4(self,x):
        if x:
            self.color4.setText("x")
            self.barvy[self.curY][self.curX][3] = 1
        else:
            self.color4.setText("")
            self.barvy[self.curY][self.curX][3] = 0
        self.update()

    def click5(self,x):
        if x:
            self.color5.setText("x")
            self.barvy[self.curY][self.curX][4] = 1
        else:
            self.color5.setText("")
            self.barvy[self.curY][self.curX][4] = 0
        self.update()

    def click6(self,x):
        if x:
            self.color6.setText("x")
            self.barvy[self.curY][self.curX][5] = 1
        else:
            self.color6.setText("")
            self.barvy[self.curY][self.curX][5] = 0
        self.update()

    def click7(self,x):
        if x:
            self.color7.setText("x")
            self.barvy[self.curY][self.curX][6] = 1
        else:
            self.color7.setText("")
            self.barvy[self.curY][self.curX][6] = 0
        self.update()

    def click8(self,x):
        if x:
            self.color8.setText("x")
            self.barvy[self.curY][self.curX][7] = 1
        else:
            self.color8.setText("")
            self.barvy[self.curY][self.curX][7] = 0
        self.update()

    def click9(self,x):
        if x:
            self.color9.setText("x")
            self.barvy[self.curY][self.curX][8] = 1
        else:
            self.color9.setText("")
            self.barvy[self.curY][self.curX][8] = 0
        self.update()



    def colorChange1(self):
        if self.color1check1.isChecked():
            self.zobrazitBarvu[0] = 1
        else:
            self.zobrazitBarvu[0] = 0
        self.update()

    def colorChange2(self):
        if self.color1check2.isChecked():
            self.zobrazitBarvu[1] = 1
        else:
            self.zobrazitBarvu[1] = 0
        self.update()

    def colorChange3(self):
        if self.color1check3.isChecked():
            self.zobrazitBarvu[2] = 1
        else:
            self.zobrazitBarvu[2] = 0
        self.update()

    def colorChange4(self):
        if self.color1check4.isChecked():
            self.zobrazitBarvu[3] = 1
        else:
            self.zobrazitBarvu[3] = 0
        self.update()

    def colorChange5(self):
        if self.color1check5.isChecked():
            self.zobrazitBarvu[4] = 1
        else:
            self.zobrazitBarvu[4] = 0
        self.update()

    def colorChange6(self):
        if self.color1check6.isChecked():
            self.zobrazitBarvu[5] = 1
        else:
            self.zobrazitBarvu[5] = 0
        self.update()

    def colorChange7(self):
        if self.color1check7.isChecked():
            self.zobrazitBarvu[6] = 1
        else:
            self.zobrazitBarvu[6] = 0
        self.update()

    def colorChange8(self):
        if self.color1check8.isChecked():
            self.zobrazitBarvu[7] = 1
        else:
            self.zobrazitBarvu[7] = 0
        self.update()

    def colorChange9(self):
        if self.color1check9.isChecked():
            self.zobrazitBarvu[8] = 1
        else:
            self.zobrazitBarvu[8] = 0
        self.update()


    def upravitWidgety(self): #nastavi widgety pri presunu na nove policko

        for i in range(0,9,1):
            for j in range(0,9,1):
                self.doplneno[i][j] = self.zadani[i][j]+self.reseni[i][j]


        self.mainNumber.setCurrentIndex(self.zadani[self.curY][self.curX]+self.reseni[self.curY][self.curX])
        if self.rezim != "zadavani":
            if self.zadani[self.curY][self.curX] != 0:
                self.mainNumber.setDisabled(True)
            else:
                self.mainNumber.setDisabled(False)

        self.shortNoteTB.setText(self.akronymy[self.curY][self.curX])
        self.longNoteTB.setText(self.poznamky[self.curY][self.curX])

        if 1 in self.kandidati[self.curY][self.curX]:
            self.cand1.setChecked(True)
        else:
            self.cand1.setChecked(False)
        if 2 in self.kandidati[self.curY][self.curX]:
            self.cand2.setChecked(True)
        else:
            self.cand2.setChecked(False)
        if 3 in self.kandidati[self.curY][self.curX]:
            self.cand3.setChecked(True)
        else:
            self.cand3.setChecked(False)
        if 4 in self.kandidati[self.curY][self.curX]:
            self.cand4.setChecked(True)
        else:
            self.cand4.setChecked(False)
        if 5 in self.kandidati[self.curY][self.curX]:
            self.cand5.setChecked(True)
        else:
            self.cand5.setChecked(False)
        if 6 in self.kandidati[self.curY][self.curX]:
            self.cand6.setChecked(True)
        else:
            self.cand6.setChecked(False)
        if 7 in self.kandidati[self.curY][self.curX]:
            self.cand7.setChecked(True)
        else:
            self.cand7.setChecked(False)
        if 8 in self.kandidati[self.curY][self.curX]:
            self.cand8.setChecked(True)
        else:
            self.cand8.setChecked(False)
        if 9 in self.kandidati[self.curY][self.curX]:
            self.cand9.setChecked(True)
        else:
            self.cand9.setChecked(False)

        if self.barvy[self.curY][self.curX][0] == 1:
            self.color1.setChecked(True)
            self.color1.setText("x")
        else:
            self.color1.setChecked(False)
            self.color1.setText("")
        if self.barvy[self.curY][self.curX][1] == 1:
            self.color2.setChecked(True)
            self.color2.setText("x")
        else:
            self.color2.setChecked(False)
            self.color2.setText("")
        if self.barvy[self.curY][self.curX][2] == 1:
            self.color3.setChecked(True)
            self.color3.setText("x")
        else:
            self.color3.setChecked(False)
            self.color3.setText("")
        if self.barvy[self.curY][self.curX][3] == 1:
            self.color4.setChecked(True)
            self.color4.setText("x")
        else:
            self.color4.setChecked(False)
            self.color4.setText("")
        if self.barvy[self.curY][self.curX][4] == 1:
            self.color5.setChecked(True)
            self.color5.setText("x")
        else:
            self.color5.setChecked(False)
            self.color5.setText("")
        if self.barvy[self.curY][self.curX][5] == 1:
            self.color6.setChecked(True)
            self.color6.setText("x")
        else:
            self.color6.setChecked(False)
            self.color6.setText("")
        if self.barvy[self.curY][self.curX][6] == 1:
            self.color7.setChecked(True)
            self.color7.setText("x")
        else:
            self.color7.setChecked(False)
            self.color7.setText("")
        if self.barvy[self.curY][self.curX][7] == 1:
            self.color8.setChecked(True)
            self.color8.setText("x")
        else:
            self.color8.setChecked(False)
            self.color8.setText("")
        if self.barvy[self.curY][self.curX][8] == 1:
            self.color9.setChecked(True)
            self.color9.setText("x")
        else:
            self.color9.setChecked(False)
            self.color9.setText("")

        self.color1.setStyleSheet("background-color: "+self.barvyBarev[0])
        self.color2.setStyleSheet("background-color: "+self.barvyBarev[1])
        self.color3.setStyleSheet("background-color: "+self.barvyBarev[2])
        self.color4.setStyleSheet("background-color: "+self.barvyBarev[3])
        self.color5.setStyleSheet("background-color: "+self.barvyBarev[4])
        self.color6.setStyleSheet("background-color: "+self.barvyBarev[5])
        self.color7.setStyleSheet("background-color: "+self.barvyBarev[6])
        self.color8.setStyleSheet("background-color: "+self.barvyBarev[7])
        self.color9.setStyleSheet("background-color: "+self.barvyBarev[8])

    def mainNumberChosen(self,cislo):
        self.reseni[self.curY][self.curX] = cislo
        self.upravitWidgety()
        self.update()

    def candChange1(self):
        if self.cand1.isChecked() and 1 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(1)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][0] = 1
        if not self.cand1.isChecked() and 1 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(1)
            if self.autoColor:
                self.barvy[self.curY][self.curX][0] = 0

        self.upravitWidgety()
        self.update()

    def candChange2(self):
        if self.cand2.isChecked() and 2 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(2)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][1] = 1
        if not self.cand2.isChecked() and 2 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(2)
            if self.autoColor:
                self.barvy[self.curY][self.curX][1] = 0

        self.upravitWidgety()
        self.update()

    def candChange3(self):
        if self.cand3.isChecked() and 3 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(3)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][2] = 1
        if not self.cand3.isChecked() and 3 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(3)
            if self.autoColor:
                self.barvy[self.curY][self.curX][2] = 0

        self.upravitWidgety()
        self.update()

    def candChange4(self):
        if self.cand4.isChecked() and 4 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(4)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][3] = 1
        if not self.cand4.isChecked() and 4 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(4)
            if self.autoColor:
                self.barvy[self.curY][self.curX][3] = 0

        self.upravitWidgety()
        self.update()

    def candChange5(self):
        if self.cand5.isChecked() and 5 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(5)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][4] = 1
        if not self.cand5.isChecked() and 5 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(5)
            if self.autoColor:
                self.barvy[self.curY][self.curX][4] = 0

        self.upravitWidgety()
        self.update()

    def candChange6(self):
        if self.cand6.isChecked() and 6 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(6)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][5] = 1
        if not self.cand6.isChecked() and 6 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(6)
            if self.autoColor:
                self.barvy[self.curY][self.curX][5] = 0

        self.upravitWidgety()
        self.update()

    def candChange7(self):
        if self.cand7.isChecked() and 7 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(7)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][6] = 1
        if not self.cand7.isChecked() and 7 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(7)
            if self.autoColor:
                self.barvy[self.curY][self.curX][6] = 0

        self.upravitWidgety()
        self.update()

    def candChange8(self):
        if self.cand8.isChecked() and 8 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(8)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][7] = 1

        if not self.cand8.isChecked() and 8 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(8)
            if self.autoColor:
                self.barvy[self.curY][self.curX][7] = 0

        self.upravitWidgety()
        self.update()

    def candChange9(self):
        if self.cand9.isChecked() and 9 not in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].append(9)
            self.kandidati[self.curY][self.curX].sort()
            if self.autoColor:
                self.barvy[self.curY][self.curX][8] = 1
        if not self.cand9.isChecked() and 9 in self.kandidati[self.curY][self.curX]:
            self.kandidati[self.curY][self.curX].remove(9)
            if self.autoColor:
                self.barvy[self.curY][self.curX][8] = 0

        self.upravitWidgety()
        self.update()

    def obnovit(self):
        self.setFocus()

    def editLongNote(self):
        dialog = LongNoteDialog()
        dialog.setTitle("Poznámka "+num2alpha(self.curY)+str(self.curX+1))
        dialog.setDefaultText(self.poznamky[self.curY][self.curX])
        dialog.exec_()

        if dialog.signal:
            self.poznamky[self.curY][self.curX] = dialog.obsah

        self.upravitWidgety()
        self.setFocus()

    def editShortNote(self):
        dialog = ShortNoteDialog()
        dialog.setTitle("Akronym "+num2alpha(self.curY)+str(self.curX+1))
        dialog.setDefaultText(self.akronymy[self.curY][self.curX])
        dialog.exec_()

        if dialog.signal:
            self.akronymy[self.curY][self.curX] = dialog.obsah

        self.upravitWidgety()
        self.setFocus()

    def vygenerovatKandidaty(self):
        self.kandidati = solver2.inicializovatKandidaty(self.doplneno)
        self.kandidati = solver2.generujKandidaty(self.kandidati,self.doplneno)
        if self.autoColor:
            self.zabarvitDleKandidatuClick()
        self.upravitWidgety()
        self.update()

    def vyresit(self):
        self.odstranitIndikatory()
        temp = solver2.solvePC(self.doplneno)
        if len(temp[0]) == 0:
            self.ukazatChyby()
            QtGui.QMessageBox.warning(None,"Varování","Sudoku obsahuje chyby. Nejdříve je opravte ("+str(int(temp[1]))+" ms).")
        else:
            self.doplneno = deepcopy(temp[0][0])
            for i in range(0,9,1):
                for j in range(0,9,1):
                    self.reseni[i][j] = self.doplneno[i][j]-self.zadani[i][j]
                    if self.reseni[i][j] < 0:
                        self.reseni[i][j] = 0

            self.akronymy = [
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""]]

            self.poznamky = [
                ["","","","","","","","",""],
                ["","","","","","","","",""],
                ["","","","","","","","",""],
                ["","","","","","","","",""],
                ["","","","","","","","",""],
                ["","","","","","","","",""],
                ["","","","","","","","",""],
                ["","","","","","","","",""],
                ["","","","","","","","",""]]

            self.chyby = [
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

            self.barvy = [
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
                [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]]

            self.kandidati = [
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]]]

            self.upravitWidgety()
            self.update()
            QtGui.QMessageBox.information(None,"Info","Vyřešeno bez chyb ("+str(int(temp[1]))+" ms).")

    def odstranitBarvuClick(self):
        dialog = RemoveColorDialog()
        dialog.exec_()

    def nastaveniBarevClick(self):
        dialog = ColorSettingsDialog()
        dialog.exec_()

    def zabarvitDleKandidatuClick(self):
        for i in range(0,9,1):
            for j in range(0,9,1):
                for k in range(0,9,1):
                    if k+1 in self.kandidati[i][j]:
                        self.barvy[i][j][k] = 1
                    else:
                        self.barvy[i][j][k] = 0

        self.upravitWidgety()
        self.update()

    def restartovatClick(self):

        otazka = QtGui.QMessageBox.question(None,"Dotaz","Opravdu chcete sudoku restartovat? Všechny neuložené změny budou ztraceny!",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
        if otazka == QtGui.QMessageBox.Ok:
            self.reset()


    def reset(self):
        if self.casBezi:
            self.startstop()
            self.time = 0
            self.timeBackup = 0
            self.cas.setText("Čas: 0:00:00")


        self.zadani = deepcopy(self.zadaniBackup)

        self.reseni = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

        self.chyby = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

        self.indikace1 = [
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

        self.indikace2 = [
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

        self.indikace3 = [
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

        self.doplneno = [
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

        self.akronymy = [
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""]]

        self.poznamky = [
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""]]

        self.barvy = [
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]]


        self.zobrazitBarvu = [1,1,1,1,1,1,1,1,1]

        self.kandidati = [
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]]]

        self.upravitWidgety()
        self.update()

    def zkontrolovat(self):
        self.odstranitIndikatory()
        temp = solver2.solvePC(self.doplneno)
        if len(temp[0]) == 0:
            QtGui.QMessageBox.warning(None,"Varování","Sudoku obsahuje chyby ("+str(int(temp[1]))+" ms).")
            self.ukecanejBanner.setText("<b><font color='#ff0000'>Sudoku obsahuje chyby.</b></font>")
        else:
            QtGui.QMessageBox.information(None,"Info","Sudoku je bez chyb ("+str(int(temp[1]))+" ms).")
            self.ukecanejBanner.setText("Sudoku je bez chyb.")

    def odstranitIndikatory(self):
        self.indikace1 = [
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
        self.indikace2 = [
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
        self.indikace3 = [
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
        self.chyby = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]

    def ukazatChyby(self):
        self.odstranitIndikatory()
        bezchyby = True
        temp = solver2.solvePC(self.zadani,pocetReseni=2)

        if len(temp[0]) > 1:
            self.ukecanejBanner.setText("<b><font color='#ff0000'>Sudoku nemá jednoznačné řešení, tato funkce není k dispozici.</b></font>")
            self.update()
            return False
        elif len(temp[0]) == 0:
            self.ukecanejBanner.setText("<b><font color='#ff0000'>Sudoku nemá řešení, tato funkce není k dispozici.</b></font>")
            self.update()
            return False

        for i in range(0,9,1):
            for j in range(0,9,1):
                if self.doplneno[i][j] != temp[0][0][i][j] and self.doplneno[i][j] != 0:
                    self.chyby[i][j] = 1
                    bezchyby = False

        if bezchyby:
            QtGui.QMessageBox.information(None,"Info","Sudoku je bez chyb ("+str(int(temp[1]))+" ms).")
            self.ukecanejBanner.setText("Sudoku je bez chyb.")
            self.update()
        else:
            self.ukecanejBanner.setText("<b><font color='#ff0000'>Sudoku obsahuje chyby.</b></font>")
            self.update()

    def poraditStrategii(self):
        self.odstranitIndikatory()
        if solver2.sudokuVyreseno(self.doplneno) and len(solver2.solvePC(self.doplneno)[0]) > 0:
            QtGui.QMessageBox.information(None,"Info","Sudoku je již vyřešeno.")
            self.ukecanejBanner.setText("Sudoku je již vyřešeno.")
            return False

        kroky = solver2.solveHuman(self.doplneno)
        if len(kroky[0]) == 0 and len(solver2.solvePC(self.doplneno)[0]) == 0:
            QtGui.QMessageBox.warning(None,"Varování","Sudoku obsahuje chyby. Nejprve je opravte.")
            self.ukazatChyby()
        elif len(kroky[0]) == 0:
            QtGui.QMessageBox.information(None,"Info","Sudoku nelze za pomoci implementovaných strategií vyřešit.")
        else:
            QtGui.QMessageBox.information(None,"Info","Použij "+kroky[0][0][0]+".")
            self.ukecanejBanner.setText("Použij <b>"+kroky[0][0][0]+"</b>.")


    def ukazatKrok(self):
        self.odstranitIndikatory()
        if solver2.sudokuVyreseno(self.doplneno) and len(solver2.solvePC(self.doplneno)[0]) > 0:
            QtGui.QMessageBox.information(None,"Info","Sudoku je již vyřešeno.")
            self.ukecanejBanner.setText("Sudoku je již vyřešeno.")
            return False

        self.odstranitIndikatory()

        kroky = solver2.solveHuman(self.doplneno)
        if len(kroky[0]) == 0 and len(solver2.solvePC(self.doplneno)[0]) == 0:
            QtGui.QMessageBox.warning(None,"Varování","Sudoku obsahuje chyby. Nejprve je opravte.")
            self.ukazatChyby()
        else:
            if len(kroky[0]) == 0:
                QtGui.QMessageBox.information(None,"Info","Sudoku nelze za pomoci implementovaných strategií vyřešit.")
                return False

            if kroky[0][0][0] == "Hidden Single":
                if kroky[0][0][1][0] == "r":
                    kde = "V <font color='#888833'><b>řádku "+num2alpha(kroky[0][0][1][1])+"</font> "
                    self.indikace1[kroky[0][0][1][1]] = [1,1,1,1,1,1,1,1,1]
                elif kroky[0][0][1][0] == "s":
                    kde =  "Ve <font color='#888833'><b>sloupci "+str(kroky[0][0][1][1]+1)+"</font> "
                    for i in range(0,9,1):
                        self.indikace1[i][kroky[0][0][1][1]] = 1
                elif kroky[0][0][1][0] == "c":
                    kde = "V <font color='#888833'><b>"+dekodovatCtverec(kroky[0][0][1][1])+" čtverci</font></b> "
                    for i in range(0,3,1):
                        for j in range(0,3,1):
                            addI = divmod(kroky[0][0][1][1],3)[0]
                            addJ = divmod(kroky[0][0][1][1],3)[1]
                            self.indikace1[j+3*addJ][i+3*addI] = 1
                self.ukecanejBanner.setText("<b>Hidden Single:</b> "+kde+"může být číslo <b>"+str(kroky[0][0][3])+"</b> pouze na políčku <b><font color='#00aa00'>"+num2alpha(kroky[0][0][2][0])+str(kroky[0][0][2][1]+1)+"</b></font>. Proto jej tam můžeme dopsat.")

                self.indikace3[kroky[0][0][2][0]][kroky[0][0][2][1]] = 1

            elif kroky[0][0][0] == "Naked Single":
                self.ukecanejBanner.setText("<b>Naked Single:</b> Na políčku <b><font color='#00aa00'>"+num2alpha(kroky[0][0][1][0])+str(kroky[0][0][1][1]+1)+"</b></font> může být pouze číslo <b>"+str(kroky[0][0][2])+"</b>. Proto jej tam můžeme dopsat.")
                self.indikace3[kroky[0][0][1][0]][kroky[0][0][1][1]] = 1

        self.update()

    def vzdatSe(self):
        otazka = QtGui.QMessageBox.question(None,"Dotaz","Opravdu se chcete vzdát? Sudoku budete moci dokončit s pomocí počítače.",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
        if otazka == QtGui.QMessageBox.Ok:
            self.rezim = "reseni"
            self.hideAll()
            self.setWindowTitle("SuSol - Trénink")
            self.tabsReseni()
            self.casBezi = True
            self.casStartStop.setStyleSheet("background-color: #008800")


    def ulozitClick(self):
        dialog = DBInsertDialog2()
        dialog.exec_()

    def tabsReseni(self):
        self.tabs = QtGui.QTabWidget(self)
        self.tabs.setFocusPolicy(QtCore.Qt.NoFocus)
        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(20)

        self.mainNumber = QtGui.QComboBox()
        self.mainNumber.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainNumber.setMinimumHeight(30)
        self.mainNumber.addItem("nic")
        self.mainNumber.addItem("1")
        self.mainNumber.addItem("2")
        self.mainNumber.addItem("3")
        self.mainNumber.addItem("4")
        self.mainNumber.addItem("5")
        self.mainNumber.addItem("6")
        self.mainNumber.addItem("7")
        self.mainNumber.addItem("8")
        self.mainNumber.addItem("9")
        self.mainNumber.activated.connect(self.mainNumberChosen)

        self.mainNumberLabel = QtGui.QLabel()
        self.mainNumberLabel.setText("Číslo")
        self.mainNumberLabel.setFont(pismo)
        self.mainNumberLabel.setMinimumHeight(30)
        self.mainNumberLabel.setMinimumWidth(80)


        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(15)

        self.candLabel = QtGui.QLabel()
        self.candLabel.setText("Kandidáti")
        self.candLabel.setFont(pismo)
        self.candLabel.setMinimumHeight(30)
        self.candLabel.setMinimumWidth(80)

        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(15)

        self.colorLabel = QtGui.QLabel()
        self.colorLabel.setText("Barvy")
        self.colorLabel.setFont(pismo)
        self.colorLabel.setMinimumHeight(30)
        self.colorLabel.setMinimumWidth(80)

        self.cand1 = QtGui.QCheckBox("1")
        self.cand1.setMinimumHeight(30)
        self.cand1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand1.stateChanged.connect(self.candChange1)
        self.cand2 = QtGui.QCheckBox("2")
        self.cand2.setMinimumHeight(30)
        self.cand2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand2.stateChanged.connect(self.candChange2)
        self.cand3 = QtGui.QCheckBox("3")
        self.cand3.setMinimumHeight(30)
        self.cand3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand3.stateChanged.connect(self.candChange3)
        self.cand4 = QtGui.QCheckBox("4")
        self.cand4.setMinimumHeight(30)
        self.cand4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand4.stateChanged.connect(self.candChange4)
        self.cand5 = QtGui.QCheckBox("5")
        self.cand5.setMinimumHeight(30)
        self.cand5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand5.stateChanged.connect(self.candChange5)
        self.cand6 = QtGui.QCheckBox("6")
        self.cand6.setMinimumHeight(30)
        self.cand6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand6.stateChanged.connect(self.candChange6)
        self.cand7 = QtGui.QCheckBox("7")
        self.cand7.setMinimumHeight(30)
        self.cand7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand7.stateChanged.connect(self.candChange7)
        self.cand8 = QtGui.QCheckBox("8")
        self.cand8.setMinimumHeight(30)
        self.cand8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand8.stateChanged.connect(self.candChange8)
        self.cand9 = QtGui.QCheckBox("9")
        self.cand9.setMinimumHeight(30)
        self.cand9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand9.stateChanged.connect(self.candChange9)

        self.color1 = QtGui.QPushButton()
        self.color1.setStyleSheet("background-color: "+self.barvyBarev[0]+"; color: #000000")
        self.color1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1.setMaximumWidth(20)
        self.color1.setCheckable(True)
        self.color1.clicked.connect(self.click1)
        self.color2 = QtGui.QPushButton()
        self.color2.setStyleSheet("background-color: "+self.barvyBarev[1]+"; color: #000000")
        self.color2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color2.setMaximumWidth(20)
        self.color2.setCheckable(True)
        self.color2.clicked.connect(self.click2)
        self.color3 = QtGui.QPushButton()
        self.color3.setStyleSheet("background-color: "+self.barvyBarev[2]+"; color: #000000")
        self.color3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color3.setMaximumWidth(20)
        self.color3.setCheckable(True)
        self.color3.clicked.connect(self.click3)
        self.color4 = QtGui.QPushButton()
        self.color4.setStyleSheet("background-color: "+self.barvyBarev[3]+"; color: #000000")
        self.color4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color4.setMaximumWidth(20)
        self.color4.setCheckable(True)
        self.color4.clicked.connect(self.click4)
        self.color5 = QtGui.QPushButton()
        self.color5.setStyleSheet("background-color: "+self.barvyBarev[4]+"; color: #000000")
        self.color5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color5.setMaximumWidth(20)
        self.color5.setCheckable(True)
        self.color5.clicked.connect(self.click5)
        self.color6 = QtGui.QPushButton()
        self.color6.setStyleSheet("background-color: "+self.barvyBarev[5]+"; color: #000000")
        self.color6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color6.setMaximumWidth(20)
        self.color6.setCheckable(True)
        self.color6.clicked.connect(self.click6)
        self.color7 = QtGui.QPushButton()
        self.color7.setStyleSheet("background-color: "+self.barvyBarev[6]+"; color: #000000")
        self.color7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color7.setMaximumWidth(20)
        self.color7.setCheckable(True)
        self.color7.clicked.connect(self.click7)
        self.color8 = QtGui.QPushButton()
        self.color8.setStyleSheet("background-color: "+self.barvyBarev[7]+"; color: #000000")
        self.color8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color8.setMaximumWidth(20)
        self.color8.setCheckable(True)
        self.color8.clicked.connect(self.click8)
        self.color9 = QtGui.QPushButton()
        self.color9.setStyleSheet("background-color: "+self.barvyBarev[8]+"; color: #000000")
        self.color9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color9.setMaximumWidth(20)
        self.color9.setCheckable(True)
        self.color9.clicked.connect(self.click9)

        self.color1check1 = QtGui.QCheckBox()
        self.color1check1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check1.setChecked(True)
        self.color1check1.stateChanged.connect(self.colorChange1)
        self.color1check2 = QtGui.QCheckBox()
        self.color1check2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check2.setChecked(True)
        self.color1check2.stateChanged.connect(self.colorChange2)
        self.color1check3 = QtGui.QCheckBox()
        self.color1check3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check3.setChecked(True)
        self.color1check3.stateChanged.connect(self.colorChange3)
        self.color1check4 = QtGui.QCheckBox()
        self.color1check4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check4.setChecked(True)
        self.color1check4.stateChanged.connect(self.colorChange4)
        self.color1check5 = QtGui.QCheckBox()
        self.color1check5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check5.setChecked(True)
        self.color1check5.stateChanged.connect(self.colorChange5)
        self.color1check6 = QtGui.QCheckBox()
        self.color1check6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check6.setChecked(True)
        self.color1check6.stateChanged.connect(self.colorChange6)
        self.color1check7 = QtGui.QCheckBox()
        self.color1check7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check7.setChecked(True)
        self.color1check7.stateChanged.connect(self.colorChange7)
        self.color1check8 = QtGui.QCheckBox()
        self.color1check8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check8.setChecked(True)
        self.color1check8.stateChanged.connect(self.colorChange8)
        self.color1check9 = QtGui.QCheckBox()
        self.color1check9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check9.setChecked(True)
        self.color1check9.stateChanged.connect(self.colorChange9)

        self.shortNoteLabel = QtGui.QLabel()
        self.shortNoteLabel.setText("Akronym")
        self.shortNoteLabel.setFont(pismo)

        self.shortNoteBtn = QtGui.QPushButton()
        self.shortNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shortNoteBtn.setText("&Editovat")
        self.shortNoteBtn.clicked.connect(self.editShortNote)

        self.shortNoteTB = QtGui.QLineEdit()
        self.shortNoteTB.setDisabled(True)
        self.shortNoteTB.setStyleSheet("background-color: #ffffff")

        self.longNoteLabel = QtGui.QLabel()
        self.longNoteLabel.setText("Poznámka")
        self.longNoteLabel.setFont(pismo)
        self.longNoteLabel.setMinimumWidth(80)

        self.longNoteBtn = QtGui.QPushButton()
        self.longNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.longNoteBtn.setText("E&ditovat")
        self.longNoteBtn.clicked.connect(self.editLongNote)

        self.longNoteTB = QtGui.QTextEdit()
        self.longNoteTB.setDisabled(True)

        self.cas = QtGui.QLabel()
        self.cas.setText(hms(self.time))
        self.cas.setFont(pismo)

        self.casMenu = QtGui.QMenu()
        self.a1 = self.casMenu.addAction("Start/Stop\tSpace",self.startstop)
        self.a2 = self.casMenu.addAction("Vynulovat",self.vynulovat)
        self.a3 = self.casMenu.addAction("Nastavit...",self.nastavitCas)
        self.casMenu.setFocusPolicy(QtCore.Qt.NoFocus)


        self.casStartStop = QtGui.QPushButton()
        self.casStartStop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.casStartStop.setStyleSheet("background-color: #ff0000; color: #ffffff")
        self.casStartStop.setText("&Možnosti")
        self.casStartStop.setMenu(self.casMenu)


        self.odstranitBarvu = QtGui.QPushButton()
        self.odstranitBarvu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.odstranitBarvu.setText("&Odstranit barvu...")
        self.odstranitBarvu.clicked.connect(self.odstranitBarvuClick)

        self.ulozitBtn = QtGui.QPushButton()
        self.ulozitBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ulozitBtn.setText("&Uložit")
        self.ulozitBtn.clicked.connect(self.ulozitClick)

        self.zabarvitDleKandidatu = QtGui.QPushButton()
        self.zabarvitDleKandidatu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zabarvitDleKandidatu.setText("&Zabarvit dle kandidátů")
        self.zabarvitDleKandidatu.clicked.connect(self.zabarvitDleKandidatuClick)

        self.restartovatBtn = QtGui.QPushButton()
        self.restartovatBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.restartovatBtn.setText("&Restartovat")
        self.restartovatBtn.clicked.connect(self.restartovatClick)

        self.vygenerovatKandidatyBtn = QtGui.QPushButton()
        self.vygenerovatKandidatyBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vygenerovatKandidatyBtn.setText("Vygenerovat kandidáty")
        self.vygenerovatKandidatyBtn.clicked.connect(self.vygenerovatKandidaty)

        self.vyresitBtn = QtGui.QPushButton()
        self.vyresitBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vyresitBtn.setText("Vyřešit")
        self.vyresitBtn.clicked.connect(self.vyresit)

        self.zkontrolovatBtn = QtGui.QPushButton()
        self.zkontrolovatBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zkontrolovatBtn.setText("Zkontrolovat")
        self.zkontrolovatBtn.clicked.connect(self.zkontrolovat)

        self.ukazatChybyBtn = QtGui.QPushButton()
        self.ukazatChybyBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ukazatChybyBtn.setText("Ukázat chyby")
        self.ukazatChybyBtn.clicked.connect(self.ukazatChyby)

        self.poraditStrategiiBtn = QtGui.QPushButton()
        self.poraditStrategiiBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.poraditStrategiiBtn.setText("Poradit strategii")
        self.poraditStrategiiBtn.clicked.connect(self.poraditStrategii)

        self.ukazatKrokBtn = QtGui.QPushButton()
        self.ukazatKrokBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ukazatKrokBtn.setText("Ukázat krok")
        self.ukazatKrokBtn.clicked.connect(self.ukazatKrok)



        self.poleLabel = QtGui.QLabel("ABCDEFGHI"[self.curY]+str(self.curX+1))
        self.poleLabel.setStyleSheet("color: red")
        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(20)
        pismo.setBold(True)
        self.poleLabel.setFont(pismo)

        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()

        vBoxlayout = QtGui.QGridLayout()

        vBoxlayout.addWidget(self.poleLabel,0,0)
        vBoxlayout.addWidget(self.cas,0,1,1,4)
        vBoxlayout.addWidget(self.casStartStop,0,4,1,5)
        vBoxlayout.addWidget(self.mainNumber,1,1,1,10)
        vBoxlayout.addWidget(self.mainNumberLabel,1,0)
        vBoxlayout.addWidget(self.candLabel,2,0)
        vBoxlayout.addWidget(self.colorLabel,2,2,1,2)
        vBoxlayout.addWidget(self.cand1,3,0)
        vBoxlayout.addWidget(self.cand2,4,0)
        vBoxlayout.addWidget(self.cand3,5,0)
        vBoxlayout.addWidget(self.cand4,6,0)
        vBoxlayout.addWidget(self.cand5,7,0)
        vBoxlayout.addWidget(self.cand6,8,0)
        vBoxlayout.addWidget(self.cand7,9,0)
        vBoxlayout.addWidget(self.cand8,10,0)
        vBoxlayout.addWidget(self.cand9,11,0)
        vBoxlayout.addWidget(self.color1,3,2)
        vBoxlayout.addWidget(self.color2,4,2)
        vBoxlayout.addWidget(self.color3,5,2)
        vBoxlayout.addWidget(self.color4,6,2)
        vBoxlayout.addWidget(self.color5,7,2)
        vBoxlayout.addWidget(self.color6,8,2)
        vBoxlayout.addWidget(self.color7,9,2)
        vBoxlayout.addWidget(self.color8,10,2)
        vBoxlayout.addWidget(self.color9,11,2)
        vBoxlayout.addWidget(self.color1check1,3,3)
        vBoxlayout.addWidget(self.color1check2,4,3)
        vBoxlayout.addWidget(self.color1check3,5,3)
        vBoxlayout.addWidget(self.color1check4,6,3)
        vBoxlayout.addWidget(self.color1check5,7,3)
        vBoxlayout.addWidget(self.color1check6,8,3)
        vBoxlayout.addWidget(self.color1check7,9,3)
        vBoxlayout.addWidget(self.color1check8,10,3)
        vBoxlayout.addWidget(self.color1check9,11,3)
        vBoxlayout.addWidget(self.shortNoteLabel,2,4)
        vBoxlayout.addWidget(self.shortNoteBtn,3,4)
        vBoxlayout.addWidget(self.shortNoteTB,4,4,1,7)
        vBoxlayout.addWidget(self.longNoteLabel,5,4)
        vBoxlayout.addWidget(self.longNoteBtn,6,4)
        vBoxlayout.addWidget(self.longNoteTB,7,4,6,7)
        vBoxlayout.addWidget(self.odstranitBarvu,14,0,1,11)
        vBoxlayout.addWidget(self.zabarvitDleKandidatu,13,0,1,11)
        vBoxlayout.addWidget(self.ulozitBtn,15,0,1,11)
        vBoxlayout.addWidget(self.restartovatBtn,16,0,1,11)
        self.tab1.setLayout(vBoxlayout)

        vBoxlayout = QtGui.QGridLayout()
        vBoxlayout.addWidget(self.vygenerovatKandidatyBtn)
        vBoxlayout.addWidget(self.zkontrolovatBtn)
        vBoxlayout.addWidget(self.ukazatChybyBtn)
        vBoxlayout.addWidget(self.poraditStrategiiBtn)
        vBoxlayout.addWidget(self.ukazatKrokBtn)
        vBoxlayout.addWidget(self.vyresitBtn)
        self.tab2.setLayout(vBoxlayout)

        self.tabs.addTab(self.tab1,"Řešení")
        self.tabs.addTab(self.tab2,"Pomoc počítače")
        self.tabs.show()

        self.upravitWidgety()
        self.setFocus()

    def tabsNaCas(self):
        self.tabs = QtGui.QTabWidget(self)
        self.tabs.setFocusPolicy(QtCore.Qt.NoFocus)
        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(20)

        self.mainNumber = QtGui.QComboBox()
        self.mainNumber.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainNumber.setMinimumHeight(30)
        self.mainNumber.addItem("nic")
        self.mainNumber.addItem("1")
        self.mainNumber.addItem("2")
        self.mainNumber.addItem("3")
        self.mainNumber.addItem("4")
        self.mainNumber.addItem("5")
        self.mainNumber.addItem("6")
        self.mainNumber.addItem("7")
        self.mainNumber.addItem("8")
        self.mainNumber.addItem("9")
        self.mainNumber.activated.connect(self.mainNumberChosen)

        self.mainNumberLabel = QtGui.QLabel()
        self.mainNumberLabel.setText("Číslo")
        self.mainNumberLabel.setFont(pismo)
        self.mainNumberLabel.setMinimumHeight(30)
        self.mainNumberLabel.setMinimumWidth(80)


        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(15)

        self.candLabel = QtGui.QLabel()
        self.candLabel.setText("Kandidáti")
        self.candLabel.setFont(pismo)
        self.candLabel.setMinimumHeight(30)
        self.candLabel.setMinimumWidth(80)

        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(15)

        self.colorLabel = QtGui.QLabel()
        self.colorLabel.setText("Barvy")
        self.colorLabel.setFont(pismo)
        self.colorLabel.setMinimumHeight(30)
        self.colorLabel.setMinimumWidth(80)

        self.cand1 = QtGui.QCheckBox("1")
        self.cand1.setMinimumHeight(30)
        self.cand1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand1.stateChanged.connect(self.candChange1)
        self.cand2 = QtGui.QCheckBox("2")
        self.cand2.setMinimumHeight(30)
        self.cand2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand2.stateChanged.connect(self.candChange2)
        self.cand3 = QtGui.QCheckBox("3")
        self.cand3.setMinimumHeight(30)
        self.cand3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand3.stateChanged.connect(self.candChange3)
        self.cand4 = QtGui.QCheckBox("4")
        self.cand4.setMinimumHeight(30)
        self.cand4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand4.stateChanged.connect(self.candChange4)
        self.cand5 = QtGui.QCheckBox("5")
        self.cand5.setMinimumHeight(30)
        self.cand5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand5.stateChanged.connect(self.candChange5)
        self.cand6 = QtGui.QCheckBox("6")
        self.cand6.setMinimumHeight(30)
        self.cand6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand6.stateChanged.connect(self.candChange6)
        self.cand7 = QtGui.QCheckBox("7")
        self.cand7.setMinimumHeight(30)
        self.cand7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand7.stateChanged.connect(self.candChange7)
        self.cand8 = QtGui.QCheckBox("8")
        self.cand8.setMinimumHeight(30)
        self.cand8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand8.stateChanged.connect(self.candChange8)
        self.cand9 = QtGui.QCheckBox("9")
        self.cand9.setMinimumHeight(30)
        self.cand9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand9.stateChanged.connect(self.candChange9)

        self.color1 = QtGui.QPushButton()
        self.color1.setStyleSheet("background-color: "+self.barvyBarev[0]+"; color: #000000")
        self.color1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1.setMaximumWidth(20)
        self.color1.setCheckable(True)
        self.color1.clicked.connect(self.click1)
        self.color2 = QtGui.QPushButton()
        self.color2.setStyleSheet("background-color: "+self.barvyBarev[1]+"; color: #000000")
        self.color2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color2.setMaximumWidth(20)
        self.color2.setCheckable(True)
        self.color2.clicked.connect(self.click2)
        self.color3 = QtGui.QPushButton()
        self.color3.setStyleSheet("background-color: "+self.barvyBarev[2]+"; color: #000000")
        self.color3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color3.setMaximumWidth(20)
        self.color3.setCheckable(True)
        self.color3.clicked.connect(self.click3)
        self.color4 = QtGui.QPushButton()
        self.color4.setStyleSheet("background-color: "+self.barvyBarev[3]+"; color: #000000")
        self.color4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color4.setMaximumWidth(20)
        self.color4.setCheckable(True)
        self.color4.clicked.connect(self.click4)
        self.color5 = QtGui.QPushButton()
        self.color5.setStyleSheet("background-color: "+self.barvyBarev[4]+"; color: #000000")
        self.color5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color5.setMaximumWidth(20)
        self.color5.setCheckable(True)
        self.color5.clicked.connect(self.click5)
        self.color6 = QtGui.QPushButton()
        self.color6.setStyleSheet("background-color: "+self.barvyBarev[5]+"; color: #000000")
        self.color6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color6.setMaximumWidth(20)
        self.color6.setCheckable(True)
        self.color6.clicked.connect(self.click6)
        self.color7 = QtGui.QPushButton()
        self.color7.setStyleSheet("background-color: "+self.barvyBarev[6]+"; color: #000000")
        self.color7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color7.setMaximumWidth(20)
        self.color7.setCheckable(True)
        self.color7.clicked.connect(self.click7)
        self.color8 = QtGui.QPushButton()
        self.color8.setStyleSheet("background-color: "+self.barvyBarev[7]+"; color: #000000")
        self.color8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color8.setMaximumWidth(20)
        self.color8.setCheckable(True)
        self.color8.clicked.connect(self.click8)
        self.color9 = QtGui.QPushButton()
        self.color9.setStyleSheet("background-color: "+self.barvyBarev[8]+"; color: #000000")
        self.color9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color9.setMaximumWidth(20)
        self.color9.setCheckable(True)
        self.color9.clicked.connect(self.click9)

        self.color1check1 = QtGui.QCheckBox()
        self.color1check1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check1.setChecked(True)
        self.color1check1.stateChanged.connect(self.colorChange1)
        self.color1check2 = QtGui.QCheckBox()
        self.color1check2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check2.setChecked(True)
        self.color1check2.stateChanged.connect(self.colorChange2)
        self.color1check3 = QtGui.QCheckBox()
        self.color1check3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check3.setChecked(True)
        self.color1check3.stateChanged.connect(self.colorChange3)
        self.color1check4 = QtGui.QCheckBox()
        self.color1check4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check4.setChecked(True)
        self.color1check4.stateChanged.connect(self.colorChange4)
        self.color1check5 = QtGui.QCheckBox()
        self.color1check5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check5.setChecked(True)
        self.color1check5.stateChanged.connect(self.colorChange5)
        self.color1check6 = QtGui.QCheckBox()
        self.color1check6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check6.setChecked(True)
        self.color1check6.stateChanged.connect(self.colorChange6)
        self.color1check7 = QtGui.QCheckBox()
        self.color1check7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check7.setChecked(True)
        self.color1check7.stateChanged.connect(self.colorChange7)
        self.color1check8 = QtGui.QCheckBox()
        self.color1check8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check8.setChecked(True)
        self.color1check8.stateChanged.connect(self.colorChange8)
        self.color1check9 = QtGui.QCheckBox()
        self.color1check9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check9.setChecked(True)
        self.color1check9.stateChanged.connect(self.colorChange9)

        self.shortNoteLabel = QtGui.QLabel()
        self.shortNoteLabel.setText("Akronym")
        self.shortNoteLabel.setFont(pismo)

        self.shortNoteBtn = QtGui.QPushButton()
        self.shortNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shortNoteBtn.setText("&Editovat")
        self.shortNoteBtn.clicked.connect(self.editShortNote)

        self.shortNoteTB = QtGui.QLineEdit()
        self.shortNoteTB.setDisabled(True)
        self.shortNoteTB.setStyleSheet("background-color: #ffffff")

        self.longNoteLabel = QtGui.QLabel()
        self.longNoteLabel.setText("Poznámka")
        self.longNoteLabel.setFont(pismo)
        self.longNoteLabel.setMinimumWidth(80)

        self.longNoteBtn = QtGui.QPushButton()
        self.longNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.longNoteBtn.setText("E&ditovat")
        self.longNoteBtn.clicked.connect(self.editLongNote)

        self.longNoteTB = QtGui.QTextEdit()
        self.longNoteTB.setDisabled(True)

        self.cas = QtGui.QLabel()
        self.cas.setText(hms(self.time))
        self.cas.setFont(pismo)

        self.casMenu = QtGui.QMenu()
        self.a1 = self.casMenu.addAction("Start/Stop\tSpace",self.startstop)
        self.a2 = self.casMenu.addAction("Vynulovat",self.vynulovat)
        self.a3 = self.casMenu.addAction("Nastavit...",self.nastavitCas)
        self.casMenu.setFocusPolicy(QtCore.Qt.NoFocus)


        self.casStartStop = QtGui.QPushButton()
        self.casStartStop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.casStartStop.setStyleSheet("background-color: #ff0000; color: #ffffff")
        self.casStartStop.setText("&Možnosti")
        self.casStartStop.setMenu(self.casMenu)


        self.odstranitBarvu = QtGui.QPushButton()
        self.odstranitBarvu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.odstranitBarvu.setText("&Odstranit barvu...")
        self.odstranitBarvu.clicked.connect(self.odstranitBarvuClick)

        self.nastaveniBarev = QtGui.QPushButton()
        self.nastaveniBarev.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nastaveniBarev.setText("&Nastavení barev...")
        self.nastaveniBarev.clicked.connect(self.nastaveniBarevClick)

        self.zabarvitDleKandidatu = QtGui.QPushButton()
        self.zabarvitDleKandidatu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zabarvitDleKandidatu.setText("&Zabarvit dle kandidátů")
        self.zabarvitDleKandidatu.clicked.connect(self.zabarvitDleKandidatuClick)

        self.restartovatBtn = QtGui.QPushButton()
        self.restartovatBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.restartovatBtn.setText("&Vzdát se")
        self.restartovatBtn.clicked.connect(self.vzdatSe)

        self.vygenerovatKandidatyBtn = QtGui.QPushButton()
        self.vygenerovatKandidatyBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vygenerovatKandidatyBtn.setText("Vygenerovat kandidáty")
        self.vygenerovatKandidatyBtn.clicked.connect(self.vygenerovatKandidaty)

        self.vyresitBtn = QtGui.QPushButton()
        self.vyresitBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vyresitBtn.setText("Vyřešit")
        self.vyresitBtn.clicked.connect(self.vyresit)

        self.zkontrolovatBtn = QtGui.QPushButton()
        self.zkontrolovatBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zkontrolovatBtn.setText("Zkontrolovat")
        self.zkontrolovatBtn.clicked.connect(self.zkontrolovat)

        self.ukazatChybyBtn = QtGui.QPushButton()
        self.ukazatChybyBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ukazatChybyBtn.setText("Ukázat chyby")
        self.ukazatChybyBtn.clicked.connect(self.ukazatChyby)

        self.poraditStrategiiBtn = QtGui.QPushButton()
        self.poraditStrategiiBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.poraditStrategiiBtn.setText("Poradit strategii")
        self.poraditStrategiiBtn.clicked.connect(self.poraditStrategii)

        self.ukazatKrokBtn = QtGui.QPushButton()
        self.ukazatKrokBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ukazatKrokBtn.setText("Ukázat krok")
        self.ukazatKrokBtn.clicked.connect(self.ukazatKrok)



        self.poleLabel = QtGui.QLabel("ABCDEFGHI"[self.curY]+str(self.curX+1))
        self.poleLabel.setStyleSheet("color: red")
        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(20)
        pismo.setBold(True)
        self.poleLabel.setFont(pismo)

        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()

        vBoxlayout = QtGui.QGridLayout()

        vBoxlayout.addWidget(self.poleLabel,0,0)
        vBoxlayout.addWidget(self.cas,0,1,1,4)
        # vBoxlayout.addWidget(self.casStartStop,0,4,1,5)
        vBoxlayout.addWidget(self.mainNumber,1,1,1,10)
        vBoxlayout.addWidget(self.mainNumberLabel,1,0)
        vBoxlayout.addWidget(self.candLabel,2,0)
        vBoxlayout.addWidget(self.colorLabel,2,2,1,2)
        vBoxlayout.addWidget(self.cand1,3,0)
        vBoxlayout.addWidget(self.cand2,4,0)
        vBoxlayout.addWidget(self.cand3,5,0)
        vBoxlayout.addWidget(self.cand4,6,0)
        vBoxlayout.addWidget(self.cand5,7,0)
        vBoxlayout.addWidget(self.cand6,8,0)
        vBoxlayout.addWidget(self.cand7,9,0)
        vBoxlayout.addWidget(self.cand8,10,0)
        vBoxlayout.addWidget(self.cand9,11,0)
        vBoxlayout.addWidget(self.color1,3,2)
        vBoxlayout.addWidget(self.color2,4,2)
        vBoxlayout.addWidget(self.color3,5,2)
        vBoxlayout.addWidget(self.color4,6,2)
        vBoxlayout.addWidget(self.color5,7,2)
        vBoxlayout.addWidget(self.color6,8,2)
        vBoxlayout.addWidget(self.color7,9,2)
        vBoxlayout.addWidget(self.color8,10,2)
        vBoxlayout.addWidget(self.color9,11,2)
        vBoxlayout.addWidget(self.color1check1,3,3)
        vBoxlayout.addWidget(self.color1check2,4,3)
        vBoxlayout.addWidget(self.color1check3,5,3)
        vBoxlayout.addWidget(self.color1check4,6,3)
        vBoxlayout.addWidget(self.color1check5,7,3)
        vBoxlayout.addWidget(self.color1check6,8,3)
        vBoxlayout.addWidget(self.color1check7,9,3)
        vBoxlayout.addWidget(self.color1check8,10,3)
        vBoxlayout.addWidget(self.color1check9,11,3)
        vBoxlayout.addWidget(self.shortNoteLabel,2,4)
        vBoxlayout.addWidget(self.shortNoteBtn,3,4)
        vBoxlayout.addWidget(self.shortNoteTB,4,4,1,7)
        vBoxlayout.addWidget(self.longNoteLabel,5,4)
        vBoxlayout.addWidget(self.longNoteBtn,6,4)
        vBoxlayout.addWidget(self.longNoteTB,7,4,6,7)
        vBoxlayout.addWidget(self.odstranitBarvu,14,0,1,11)
        vBoxlayout.addWidget(self.zabarvitDleKandidatu,13,0,1,11)
        vBoxlayout.addWidget(self.nastaveniBarev,15,0,1,11)
        vBoxlayout.addWidget(self.restartovatBtn,16,0,1,11)
        self.tab1.setLayout(vBoxlayout)

        vBoxlayout = QtGui.QGridLayout()
        vBoxlayout.addWidget(self.vygenerovatKandidatyBtn)
        vBoxlayout.addWidget(self.zkontrolovatBtn)
        vBoxlayout.addWidget(self.ukazatChybyBtn)
        vBoxlayout.addWidget(self.poraditStrategiiBtn)
        vBoxlayout.addWidget(self.ukazatKrokBtn)
        vBoxlayout.addWidget(self.vyresitBtn)
        self.tab2.setLayout(vBoxlayout)

        self.tabs.addTab(self.tab1,"Řešení")
        self.tabs.show()

        self.startstop()

        self.upravitWidgety()
        self.setFocus()

    def mainNumberChosenZadani(self,cislo):
        self.zadani[self.curY][self.curX] = cislo
        self.upravitWidgety()
        self.update()

    def smazatVsechnaCisla(self):
        self.zadani = [
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

        self.upravitWidgety()
        self.update()

    def hotovo(self):
        print(self.puvod)
        self.reject1 = False
        if len(solver2.solvePC(self.zadani,2)[0]) == 0:
            QtGui.QMessageBox.critical(None,"Chyba","Sudoku nemá řešení.")
            return False
        if len(solver2.solvePC(self.zadani,2)[0]) == 2:
            dotaz = QtGui.QMessageBox.question(None,"Dotaz","Sudoku není jednoznačné. Chcete jej přesto řešit?",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
            if dotaz == QtGui.QMessageBox.Cancel:
                return False

        sudoku = sudoku2string(self.zadani)
        sudoku_v_db = DB2list(db.execute("SELECT zadani FROM sudoku_zadani"))
        if sudoku in sudoku_v_db:
            pass
        else:
            dialog = DBInsertDialog()
            dialog.exec_()
        db.commit()

        if self.reject1:
            return False


        self.zadaniBackup = deepcopy(self.zadani)
        self.zobrazElementy("reseni")

    def zkontrolovatJednoznacnost(self):
        pocetReseni = len(solver2.solvePC(self.zadani,2)[0])
        if pocetReseni == 0:
            self.ukecanejBanner.setText("Sudoku nemá řešení.")
        elif pocetReseni == 1:
            self.ukecanejBanner.setText("Sudoku je jednoznačné.")
        elif pocetReseni == 2:
            self.ukecanejBanner.setText("Sudoku není jednoznačné.")

    def jineMetody(self):
        dialog = JineMetodyDialog()
        dialog.exec_()

    def fetchSettings(self):
        self.styl = db.execute("SELECT styl FROM settings WHERE uzivatel='"+unicode(self.uzivatel)+"'").fetchall()[0][0]
        db.commit()
        app.setStyle(QtGui.QStyleFactory.create(self.styl))

        #############CONFIG#######################################################
        fetch = realWideDB2list(db.execute("SELECT * FROM settings WHERE uzivatel='"+unicode(self.uzivatel)+"'").fetchall())
        self.barvyBarev = [fetch[1],fetch[2],fetch[3],fetch[4],fetch[5],fetch[6],fetch[7],fetch[8],fetch[9]]
        self.barvaKurzoru = fetch[10]
        self.barvaKandidatu = "#000000"
        self.barvaHvezdickyUpoznamky = "#000000"
        self.barvaAkronymu = "#000000"
        self.barvaZadanychCisel = "#000000"
        self.barvaDoplnenychCisel = fetch[11]
        self.barvaSouradnicPolicek = fetch[12]
        self.barvaChyby = "#ff0000"

        self.pismoCeleAplikace = fetch[13]
        self.autoColor = bool(int(fetch[15]))

        self.zobrazitSouradnice = bool(int(fetch[14]))
        #############CONFIG#######################################################

    def tabsZadavani(self):
        self.tabs = QtGui.QTabWidget(self)
        self.tabs.setFocusPolicy(QtCore.Qt.NoFocus)
        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(20)

        self.mainNumber = QtGui.QComboBox()
        self.mainNumber.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainNumber.setMinimumHeight(30)
        self.mainNumber.addItem("nic")
        self.mainNumber.addItem("1")
        self.mainNumber.addItem("2")
        self.mainNumber.addItem("3")
        self.mainNumber.addItem("4")
        self.mainNumber.addItem("5")
        self.mainNumber.addItem("6")
        self.mainNumber.addItem("7")
        self.mainNumber.addItem("8")
        self.mainNumber.addItem("9")
        self.mainNumber.activated.connect(self.mainNumberChosenZadani)

        self.mainNumberLabel = QtGui.QLabel()
        self.mainNumberLabel.setText("Číslo")
        self.mainNumberLabel.setFont(pismo)
        self.mainNumberLabel.setMinimumHeight(30)
        self.mainNumberLabel.setMinimumWidth(80)


        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(15)

        self.candLabel = QtGui.QLabel()
        self.candLabel.setText("Kandidáti")
        self.candLabel.setFont(pismo)
        self.candLabel.setMinimumHeight(30)
        self.candLabel.setMinimumWidth(80)

        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(15)

        self.colorLabel = QtGui.QLabel()
        self.colorLabel.setText("Barvy")
        self.colorLabel.setFont(pismo)
        self.colorLabel.setMinimumHeight(30)
        self.colorLabel.setMinimumWidth(80)

        self.cand1 = QtGui.QCheckBox("1")
        self.cand1.setMinimumHeight(30)
        self.cand1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand1.stateChanged.connect(self.candChange1)
        self.cand2 = QtGui.QCheckBox("2")
        self.cand2.setMinimumHeight(30)
        self.cand2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand2.stateChanged.connect(self.candChange2)
        self.cand3 = QtGui.QCheckBox("3")
        self.cand3.setMinimumHeight(30)
        self.cand3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand3.stateChanged.connect(self.candChange3)
        self.cand4 = QtGui.QCheckBox("4")
        self.cand4.setMinimumHeight(30)
        self.cand4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand4.stateChanged.connect(self.candChange4)
        self.cand5 = QtGui.QCheckBox("5")
        self.cand5.setMinimumHeight(30)
        self.cand5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand5.stateChanged.connect(self.candChange5)
        self.cand6 = QtGui.QCheckBox("6")
        self.cand6.setMinimumHeight(30)
        self.cand6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand6.stateChanged.connect(self.candChange6)
        self.cand7 = QtGui.QCheckBox("7")
        self.cand7.setMinimumHeight(30)
        self.cand7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand7.stateChanged.connect(self.candChange7)
        self.cand8 = QtGui.QCheckBox("8")
        self.cand8.setMinimumHeight(30)
        self.cand8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand8.stateChanged.connect(self.candChange8)
        self.cand9 = QtGui.QCheckBox("9")
        self.cand9.setMinimumHeight(30)
        self.cand9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cand9.stateChanged.connect(self.candChange9)

        self.color1 = QtGui.QPushButton()
        self.color1.setStyleSheet("background-color: "+self.barvyBarev[0]+"; color: #000000")
        self.color1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1.setMaximumWidth(20)
        self.color1.setCheckable(True)
        self.color1.clicked.connect(self.click1)
        self.color2 = QtGui.QPushButton()
        self.color2.setStyleSheet("background-color: "+self.barvyBarev[1]+"; color: #000000")
        self.color2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color2.setMaximumWidth(20)
        self.color2.setCheckable(True)
        self.color2.clicked.connect(self.click2)
        self.color3 = QtGui.QPushButton()
        self.color3.setStyleSheet("background-color: "+self.barvyBarev[2]+"; color: #000000")
        self.color3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color3.setMaximumWidth(20)
        self.color3.setCheckable(True)
        self.color3.clicked.connect(self.click3)
        self.color4 = QtGui.QPushButton()
        self.color4.setStyleSheet("background-color: "+self.barvyBarev[3]+"; color: #000000")
        self.color4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color4.setMaximumWidth(20)
        self.color4.setCheckable(True)
        self.color4.clicked.connect(self.click4)
        self.color5 = QtGui.QPushButton()
        self.color5.setStyleSheet("background-color: "+self.barvyBarev[4]+"; color: #000000")
        self.color5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color5.setMaximumWidth(20)
        self.color5.setCheckable(True)
        self.color5.clicked.connect(self.click5)
        self.color6 = QtGui.QPushButton()
        self.color6.setStyleSheet("background-color: "+self.barvyBarev[5]+"; color: #000000")
        self.color6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color6.setMaximumWidth(20)
        self.color6.setCheckable(True)
        self.color6.clicked.connect(self.click6)
        self.color7 = QtGui.QPushButton()
        self.color7.setStyleSheet("background-color: "+self.barvyBarev[6]+"; color: #000000")
        self.color7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color7.setMaximumWidth(20)
        self.color7.setCheckable(True)
        self.color7.clicked.connect(self.click7)
        self.color8 = QtGui.QPushButton()
        self.color8.setStyleSheet("background-color: "+self.barvyBarev[7]+"; color: #000000")
        self.color8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color8.setMaximumWidth(20)
        self.color8.setCheckable(True)
        self.color8.clicked.connect(self.click8)
        self.color9 = QtGui.QPushButton()
        self.color9.setStyleSheet("background-color: "+self.barvyBarev[8]+"; color: #000000")
        self.color9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color9.setMaximumWidth(20)
        self.color9.setCheckable(True)
        self.color9.clicked.connect(self.click9)

        self.color1check1 = QtGui.QCheckBox()
        self.color1check1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check1.setChecked(True)
        self.color1check1.stateChanged.connect(self.colorChange1)
        self.color1check2 = QtGui.QCheckBox()
        self.color1check2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check2.setChecked(True)
        self.color1check2.stateChanged.connect(self.colorChange2)
        self.color1check3 = QtGui.QCheckBox()
        self.color1check3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check3.setChecked(True)
        self.color1check3.stateChanged.connect(self.colorChange3)
        self.color1check4 = QtGui.QCheckBox()
        self.color1check4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check4.setChecked(True)
        self.color1check4.stateChanged.connect(self.colorChange4)
        self.color1check5 = QtGui.QCheckBox()
        self.color1check5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check5.setChecked(True)
        self.color1check5.stateChanged.connect(self.colorChange5)
        self.color1check6 = QtGui.QCheckBox()
        self.color1check6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check6.setChecked(True)
        self.color1check6.stateChanged.connect(self.colorChange6)
        self.color1check7 = QtGui.QCheckBox()
        self.color1check7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check7.setChecked(True)
        self.color1check7.stateChanged.connect(self.colorChange7)
        self.color1check8 = QtGui.QCheckBox()
        self.color1check8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check8.setChecked(True)
        self.color1check8.stateChanged.connect(self.colorChange8)
        self.color1check9 = QtGui.QCheckBox()
        self.color1check9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.color1check9.setChecked(True)
        self.color1check9.stateChanged.connect(self.colorChange9)

        self.shortNoteLabel = QtGui.QLabel()
        self.shortNoteLabel.setText("Akronym")
        self.shortNoteLabel.setFont(pismo)

        self.shortNoteBtn = QtGui.QPushButton()
        self.shortNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shortNoteBtn.setText("&Editovat")
        self.shortNoteBtn.clicked.connect(self.editShortNote)

        self.shortNoteTB = QtGui.QLineEdit()
        self.shortNoteTB.setDisabled(True)
        self.shortNoteTB.setStyleSheet("background-color: #ffffff")

        self.longNoteLabel = QtGui.QLabel()
        self.longNoteLabel.setText("Poznámka")
        self.longNoteLabel.setFont(pismo)
        self.longNoteLabel.setMinimumWidth(80)

        self.longNoteBtn = QtGui.QPushButton()
        self.longNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.longNoteBtn.setText("E&ditovat")
        self.longNoteBtn.clicked.connect(self.editLongNote)

        self.longNoteTB = QtGui.QTextEdit()
        self.longNoteTB.setDisabled(True)

        self.cas = QtGui.QLabel()
        self.cas.setText(hms(self.time))
        self.cas.setFont(pismo)

        self.casMenu = QtGui.QMenu()
        self.a1 = self.casMenu.addAction("Start/Stop\tSpace",self.startstop)
        self.a2 = self.casMenu.addAction("Vynulovat",self.vynulovat)
        self.a3 = self.casMenu.addAction("Nastavit...",self.nastavitCas)
        self.casMenu.setFocusPolicy(QtCore.Qt.NoFocus)


        self.casStartStop = QtGui.QPushButton()
        self.casStartStop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.casStartStop.setStyleSheet("background-color: #ff0000; color: #ffffff")
        self.casStartStop.setText("&Možnosti")
        self.casStartStop.setMenu(self.casMenu)

        self.zkontrolovatJednoznacnostBtn = QtGui.QPushButton()
        self.zkontrolovatJednoznacnostBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zkontrolovatJednoznacnostBtn.setText("&Zkontrolovat jednoznačnost")
        self.zkontrolovatJednoznacnostBtn.clicked.connect(self.zkontrolovatJednoznacnost)

        self.hotovoBtn = QtGui.QPushButton()
        self.hotovoBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hotovoBtn.setText("&Hotovo")
        self.hotovoBtn.clicked.connect(self.hotovo)

        self.smazatVseBtn = QtGui.QPushButton()
        self.smazatVseBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.smazatVseBtn.setText("&Smazat všechna čísla")
        self.smazatVseBtn.clicked.connect(self.smazatVsechnaCisla)

        self.jinyZpusob = QtGui.QPushButton()
        self.jinyZpusob.setFocusPolicy(QtCore.Qt.NoFocus)
        self.jinyZpusob.setText("&Jiné metody zadávání...")
        self.jinyZpusob.clicked.connect(self.jineMetody)


        self.poleLabel = QtGui.QLabel("ABCDEFGHI"[self.curY]+str(self.curX+1))
        self.poleLabel.setStyleSheet("color: red")
        pismo = QtGui.QFont(self.pismoCeleAplikace)
        pismo.setPixelSize(20)
        pismo.setBold(True)
        self.poleLabel.setFont(pismo)
        self.poleLabel.setMinimumWidth(250)

        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()

        vBoxlayout = QtGui.QGridLayout()

        vBoxlayout.addWidget(self.poleLabel,0,0,4,10)
        vBoxlayout.addWidget(self.mainNumber,1,1,1,10)
        vBoxlayout.addWidget(self.mainNumberLabel,1,0)
        vBoxlayout.addWidget(self.hotovoBtn,13,0,1,11)
        vBoxlayout.addWidget(self.zkontrolovatJednoznacnostBtn,14,0,1,11)
        vBoxlayout.addWidget(self.smazatVseBtn,15,0,1,11)
        vBoxlayout.addWidget(self.jinyZpusob,16,0,1,11)
        self.tab1.setLayout(vBoxlayout)

        self.tabs.addTab(self.tab1,"Zadávání")
        self.tabs.show()

        self.upravitWidgety()
        self.setFocus()

    def wb1click(self):
        dialog = GeneratorDialog2()
        dialog.exec_()

    def wb2click(self):
        self.zobrazElementy("zadavani")

    def wb3click(self):
        dialog = GeneratorDialog()
        dialog.exec_()

    def wb4click(self):
        todo()

    def welcomeScreen(self):
        self.welcomeButton1 = QtGui.QPushButton(self)
        self.welcomeButton2 = QtGui.QPushButton(self)
        self.welcomeButton3 = QtGui.QPushButton(self)
        self.welcomeButton4 = QtGui.QPushButton(self)
        self.welcomeButton1.setText("sem")
        self.welcomeButton2.setText("zde")
        self.welcomeButton3.setText("sem")
        self.welcomeButton4.setText("sem")
        self.welcomeButton1.clicked.connect(self.wb1click)
        self.welcomeButton2.clicked.connect(self.wb2click)
        self.welcomeButton3.clicked.connect(self.wb3click)
        self.welcomeButton4.clicked.connect(self.wb4click)
        self.welcomeButton1.show()
        self.welcomeButton2.show()
        self.welcomeButton3.show()
        self.welcomeButton4.show()

    def zobrazElementy(self,theme):
        self.hideAll()
        self.reset()
        self.rezim = theme

        if self.rezim == "welcome_screen":
            self.setWindowTitle("SuSol")
            self.welcomeScreen()

        if self.rezim == "reseni":
            self.setWindowTitle("SuSol - Trénink")
            self.tabsReseni()

        if self.rezim == "na_cas":
            self.setWindowTitle("SuSol - Řešení na čas")
            self.tabsNaCas()

        if self.rezim == "zadavani":
            self.setWindowTitle("SuSol - Zadávání")
            self.candMode = False
            self.puvod = "zadat ručně"
            self.tabsZadavani()
            self.smazatVsechnaCisla()
            self.curX = 0
            self.curY = 0

        self.update()

    def hideAll(self):
        self.tabs.hide()
        self.welcomeButton1.hide()
        self.welcomeButton2.hide()
        self.welcomeButton3.hide()
        self.welcomeButton4.hide()

    def domu(self):
        if self.rezim != "welcome_screen":
            otazka = QtGui.QMessageBox.question(None,"Dotaz","Veškeré neuložené změny budou ztraceny. Chcete pokračovat?",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
            if otazka == QtGui.QMessageBox.Ok:
                self.zobrazElementy("welcome_screen")
                self.reset()
        else:
            self.zobrazElementy("welcome_screen")
            self.reset()
        self.update()

    def zmenitUzivatele(self):
        if self.rezim != "welcome_screen":
            otazka = QtGui.QMessageBox.question(None,"Dotaz","Pro změnu uživatele musíte být na domovské obrazovce. Chcete přepnout na domovskou obrazovku? Veškerá neuložená činnost bude ztracena!",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
            if otazka == QtGui.QMessageBox.Ok:

                self.zobrazElementy("welcome_screen")
                self.reset()
                dialog = UserSelectDialog2()
                dialog.exec_()
        else:
            self.reset()
            dialog = UserSelectDialog2()
            dialog.exec_()
        self.update()

    def mojeSudokuClick(self):
        seznam_z_db = wideDB2list(db.execute("SELECT id,datum,uzivatel,identifikator FROM sudoku_rozreseno WHERE uzivatel='"+unicode(okno.uzivatel)+"'"))
        if len(seznam_z_db) == 0:
            QtGui.QMessageBox.information(None,"Info","V databázi se žádné sudoku nenachází.")
            return False

        dialog = LoadFromDBDialog2()
        dialog.exec_()
        self.update()

    def mojeNastaveniClick(self):
        dialog = ColorSettingsDialog()
        dialog.exec_()
        self.update()

    def vysledkyClickLehke(self):
        seznam_z_db = wideDB2list(db.execute("SELECT id,cas,uzivatel,obtiznost,datum FROM sudoku_soutez WHERE obtiznost='gen. (lehké)'"))
        if len(seznam_z_db) == 0:
            QtGui.QMessageBox.information(None,"Info","V databázi se žádné sudoku nenachází.")
            return False
        dialog = VysledkyDialog("lehké")
        dialog.exec_()
        self.update()

    def vysledkyClickStredni(self):
        seznam_z_db = wideDB2list(db.execute("SELECT id,cas,uzivatel,obtiznost,datum FROM sudoku_soutez WHERE obtiznost='gen. (střední)'"))
        if len(seznam_z_db) == 0:
            QtGui.QMessageBox.information(None,"Info","V databázi se žádné sudoku nenachází.")
            return False
        dialog = VysledkyDialog("střední")
        dialog.exec_()
        self.update()

    def vysledkyClickTezke(self):
        seznam_z_db = wideDB2list(db.execute("SELECT id,cas,uzivatel,obtiznost,datum FROM sudoku_soutez WHERE obtiznost='gen. (těžké)'"))
        if len(seznam_z_db) == 0:
            QtGui.QMessageBox.information(None,"Info","V databázi se žádné sudoku nenachází.")
            return False
        dialog = VysledkyDialog("těžké")
        dialog.exec_()
        self.update()

    def vysledkyClickVlastni(self):
        seznam_z_db = wideDB2list(db.execute("SELECT id,cas,uzivatel,obtiznost,datum FROM sudoku_soutez WHERE obtiznost='gen. (vlastní)'"))
        if len(seznam_z_db) == 0:
            QtGui.QMessageBox.information(None,"Info","V databázi se žádné sudoku nenachází.")
            return False
        dialog = VysledkyDialog("vlastní")
        dialog.exec_()
        self.update()

    def rezimZadavani(self):
        if self.rezim != "welcome_screen":
            otazka = QtGui.QMessageBox.question(None,"Dotaz","Veškeré neuložené změny budou ztraceny. Chcete pokračovat?",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
            if otazka == QtGui.QMessageBox.Ok:
                self.zobrazElementy("zadavani")
        else:
            self.zobrazElementy("zadavani")
        self.update()

    def rezimReseniNaCas(self):
        if self.rezim != "welcome_screen":
            otazka = QtGui.QMessageBox.question(None,"Dotaz","Veškeré neuložené změny budou ztraceny. Chcete pokračovat?",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
            if otazka == QtGui.QMessageBox.Ok:
                self.reset()
                dialog = GeneratorDialog2()
                dialog.exec_()
        else:
            self.reset()
            dialog = GeneratorDialog2()
            dialog.exec_()
        self.update()

    def rezimReseniTrenink(self):
        if self.rezim != "welcome_screen":
            otazka = QtGui.QMessageBox.question(None,"Dotaz","Veškeré neuložené změny budou ztraceny. Chcete pokračovat?",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
            if otazka == QtGui.QMessageBox.Ok:
                self.reset()
                dialog = GeneratorDialog()
                dialog.exec_()
        else:
            self.reset()
            dialog = GeneratorDialog()
            dialog.exec_()
        self.update()



    def __init__(self):
        super(SuSol, self).__init__()

        self.uzivatel = ""
        dialog = UserSelectDialog()
        dialog.exec_()
        self.resized = False

        self.curX = 0
        self.curY = 0
        self.Xpos = 0
        self.Ypos = 0
        self.margin = 0
        self.bottom = 0
        self.right = 0

        self.tabs = QtGui.QTabWidget()
        self.candMode = False
        self.autoColor = False
        self.casBezi = False
        self.time = 0
        self.timestamp = 0
        self.timeBackup = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.pricitat_cas)

        self.rezim = "welcome_screen"
        self.puvod = ""
        self.zadani = [
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

        self.zadaniBackup = deepcopy(self.zadani)

        self.chyby = [
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

        self.reseni = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

        self.doplneno = [
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

        self.indikace1 = [
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

        self.indikace2 = [
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

        self.indikace3 = [
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

        self.akronymy = [
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""]]

        self.poznamky = [
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""]]

        self.barvy = [
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]]


        self.zobrazitBarvu = [1,1,1,1,1,1,1,1,1]

        self.kandidati = [
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]]]

        #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Windows"))
        self.setWindowTitle("SuSol")
        vyska = QtGui.QDesktopWidget().screenGeometry().height()
        sirka = QtGui.QDesktopWidget().screenGeometry().width()
        self.resize(sirka,vyska)

        self.mainMenu1 = self.menuBar().addMenu("&SuSol")
        self.mainMenu3 = self.menuBar().addMenu("&Přejít")
        self.mainMenu4 = self.menuBar().addMenu("&Uživatel:")

        self.mainMenu1.addAction("Pomoc\tF1")
        self.mainMenu1.addAction("O programu")
        self.mainMenu1.addSeparator()
        self.mainMenu1.addAction("Konec\tAlt+F4",self.quit)

        self.mainMenu3.addAction("Domů\tHome", self.domu)
        self.mainMenu3.addAction("Zadávání sudoku", self.rezimZadavani)
        self.mainMenu3.addAction("Řešení na čas", self.rezimReseniNaCas)
        self.mainMenu3.addAction("Trénink", self.rezimReseniTrenink)

        self.mainMenu4.addAction("Změnit uživatele...", self.zmenitUzivatele)
        self.mainMenu4.addSeparator()
        self.mainMenu4.addAction("Moje sudoku...", self.mojeSudokuClick)
        self.mainMenu4.addAction("Moje nastavení...",self.mojeNastaveniClick)
        self.mainMenu41 = self.mainMenu4.addMenu("Výsledky")
        self.mainMenu41.addAction("Lehké...",self.vysledkyClickLehke)
        self.mainMenu41.addAction("Střední...",self.vysledkyClickStredni)
        self.mainMenu41.addAction("Těžké...",self.vysledkyClickTezke)
        self.mainMenu41.addAction("Vlastní...",self.vysledkyClickVlastni)
        #TODO hotkeys
        #TODO hlasky statusbaru a dialogy
        #TODO dialog vlastni sudoku
        #TODO napsat manual

        self.mainMenu1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainMenu3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainMenu4.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ukecanejBanner = QtGui.QLabel(self)
        self.ukecanejBanner.move(15,vyska-60)
        self.ukecanejBanner.setMinimumWidth(sirka-30)
        self.ukecanejBanner.setMaximumWidth(sirka-30)
        self.ukecanejBanner.setText("SuSol, Karel Jílek, 2015")

        self.uzivatel = uzivatel
        self.mainMenu4.setTitle("&Uživatel: "+uzivatel)

        self.fetchSettings()
        self.welcomeScreen()
        self.fetchSettings()
        self.tabsNaCas()
        self.tabs.hide()
        self.tabsZadavani()
        self.tabs.hide()
        self.tabsReseni()
        self.tabs.hide()
        self.show()

app = QtGui.QApplication(sys.argv)
okno = SuSol()
sys.exit(app.exec_())