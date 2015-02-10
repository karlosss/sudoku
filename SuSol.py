#coding: utf8
from __future__ import print_function, unicode_literals
from PyQt4 import QtGui, QtCore
from misc import num2alpha, arr2str, alpha2num, hms
from copy import deepcopy
from time import time
import sys
import solver2

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
        obsah = self.entry.text()

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

    def click11(self):
        self.tempColors = ["#8888ff","#88ff88","#ff8888","#ffff88","#ff88ff","#88ffff","#880088","#888800","#008888"]
        self.tempCursor = "#ffbbbb"
        self.but10.setStyleSheet("background-color: "+self.tempCursor)
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


    def toggle(self):
        if self.cbox.isChecked():
            self.tempAutoColor = True
        else:
            self.tempAutoColor = False

    def acceptDialog(self):
        okno.barvyBarev = deepcopy(self.tempColors)
        okno.barvaKurzoru = self.tempCursor
        okno.autoColor = self.tempAutoColor
        okno.upravitWidgety()
        self.close()

    def __init__(self):
        super(ColorSettingsDialog, self).__init__()

        self.tempColors = deepcopy(okno.barvyBarev)
        self.tempCursor = okno.barvaKurzoru

        self.setWindowTitle("Nastavení barev")
        self.resize(300,100)

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
        self.but10 = QtGui.QPushButton()
        self.but10.setStyleSheet("color: #000000; background-color: "+self.tempCursor)
        self.but10.setText("Změnit barvu kurzoru")
        self.but10.clicked.connect(self.click10)
        self.but11 = QtGui.QPushButton()
        self.but11.setText("Obnovit výchozí")
        self.but11.clicked.connect(self.click11)

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

        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)
        buttons.rejected.connect(self.close)
        buttons.accepted.connect(self.acceptDialog)


        layout = QtGui.QVBoxLayout(self)
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
        layout.addWidget(self.but10)
        layout.addWidget(line3)
        layout.addWidget(self.but11)
        layout.addWidget(line4)
        layout.addWidget(buttons)

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

class SuSol(QtGui.QMainWindow):

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        #painter.begin(self)
        Xpos = 10
        Ypos = 30
        margin = 0
        bottom = 40
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
        if self.frameGeometry().height()-40-Ypos-margin > 520:
            a = 520
        else:
            a = self.frameGeometry().height()-40-Ypos-margin

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


        pismo = QtGui.QFont("Arial")
        pismo.setWeight(100)
        velikost = 0.7*squareSize
        if velikost < 1:
            velikost = 1
        pismo.setPixelSize(velikost)

        pismo2 = QtGui.QFont("Arial")
        pismo2.setWeight(100)
        velikost = 0.7*squareSize
        if velikost < 1:
            velikost = 1
        pismo2.setPixelSize(velikost)

        pismo3 = QtGui.QFont("Arial")
        velikost = 0.15*squareSize
        if velikost < 1:
            velikost = 1
        pismo3.setPixelSize(velikost)

        pismo4 = QtGui.QFont("Arial")
        velikost = 0.18*squareSize
        if velikost < 1:
            velikost = 1
        pismo4.setPixelSize(velikost)

        pismo5 = QtGui.QFont("Arial")
        velikost = 0.12*squareSize
        if velikost < 1:
            velikost = 1
        pismo5.setPixelSize(velikost)

        pismo6 = QtGui.QFont("Arial")
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
                if self.reseni[i][j] != 0 and self.zadani[i][j] == 0:
                    painter.setFont(pismo2)
                    painter.setPen(QtGui.QColor("#0000ff"))

                    x = j*squareSize+Xpos+squareSize/2.85
                    y = i*squareSize+Ypos+0.9*squareSize

                    painter.drawText(x,y,str(self.reseni[i][j]))

                if self.poznamky[i][j] != "":
                    x = j*squareSize+Xpos+0.8*squareSize
                    y = i*squareSize+Ypos+0.8*squareSize

                    painter.setFont(pismo6)
                    painter.setPen(QtGui.QColor("#000000"))
                    painter.drawText(x,y,"*")


                painter.setPen(QtGui.QColor("#888888"))
                painter.setFont(pismo3)

                x = j*squareSize+Xpos+squareSize/2.85+squareSize*0.45
                y = i*squareSize+Ypos+0.9*squareSize

                painter.drawText(x,y,num2alpha(i)+str(j+1))

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
        self.update()

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()

        squareSize = min((self.frameGeometry().height()-self.Ypos-2*self.margin-self.bottom)/9,(self.frameGeometry().width()-self.Xpos-2*self.margin-self.right)/9)

        if (x-self.Xpos)//squareSize >= 0 and (x-self.Xpos)//squareSize < 9 and (y-self.Ypos)//squareSize >= 0 and (y-self.Ypos)//squareSize < 9:
            self.curX = (x-self.Xpos)//squareSize
            self.curY = (y-self.Ypos)//squareSize
            string = "ABCDEFGHI"
            self.poleLabel.setText(string[self.curY]+str(self.curX+1))

        self.upravitWidgety()
        self.update()

    def keyPressEvent(self, event):
        key = event.key()

        if self.rezim in ("zadavani","reseni"):
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

            if self.rezim in ("zadavani"):
                if key == QtCore.Qt.Key_Delete:
                    self.doplnCislo(0)

            if self.rezim in ("reseni"):
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
                elif key == QtCore.Qt.Key_Space:
                    self.startstop()


            self.curX = divmod(self.curX,9)[1]
            self.curY = divmod(self.curY,9)[1]
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
            self.zadani[self.curX][self.curY] = cislo
            self.update()
        if self.rezim in ("reseni"):
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

    def click2(self,x):
        if x:
            self.color2.setText("x")
            self.barvy[self.curY][self.curX][1] = 1
        else:
            self.color2.setText("")
            self.barvy[self.curY][self.curX][1] = 0

    def click3(self,x):
        if x:
            self.color3.setText("x")
            self.barvy[self.curY][self.curX][2] = 1
        else:
            self.color3.setText("")
            self.barvy[self.curY][self.curX][2] = 0

    def click4(self,x):
        if x:
            self.color4.setText("x")
            self.barvy[self.curY][self.curX][3] = 1
        else:
            self.color4.setText("")
            self.barvy[self.curY][self.curX][3] = 0

    def click5(self,x):
        if x:
            self.color5.setText("x")
            self.barvy[self.curY][self.curX][4] = 1
        else:
            self.color5.setText("")
            self.barvy[self.curY][self.curX][4] = 0

    def click6(self,x):
        if x:
            self.color6.setText("x")
            self.barvy[self.curY][self.curX][5] = 1
        else:
            self.color6.setText("")
            self.barvy[self.curY][self.curX][5] = 0

    def click7(self,x):
        if x:
            self.color7.setText("x")
            self.barvy[self.curY][self.curX][6] = 1
        else:
            self.color7.setText("")
            self.barvy[self.curY][self.curX][6] = 0

    def click8(self,x):
        if x:
            self.color8.setText("x")
            self.barvy[self.curY][self.curX][7] = 1
        else:
            self.color8.setText("")
            self.barvy[self.curY][self.curX][7] = 0

    def click9(self,x):
        if x:
            self.color9.setText("x")
            self.barvy[self.curY][self.curX][8] = 1
        else:
            self.color9.setText("")
            self.barvy[self.curY][self.curX][8] = 0



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
        temp = deepcopy(self.doplneno)
        temp = solver2.solvePC(temp)
        print(temp)
        if temp == False:
            QtGui.QMessageBox.warning(None,"Varování","Sudoku obsahuje chyby. Nejdříve je opravte.")
        else:
            self.doplneno = deepcopy(temp)
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
            QtGui.QMessageBox.information(None,"Info","Vyřešeno bez chyb.")

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

            if self.casBezi:
                self.startstop()
            self.time = 0
            self.timeBackup = 0
            self.cas.setText("Čas: 0:00:00")


            self.zadani = [
                [0,0,5,3,0,0,0,0,0],
                [8,0,0,0,0,0,0,2,0],
                [0,7,0,0,1,0,5,0,0],
                [4,0,0,0,0,5,3,0,0],
                [0,1,0,0,7,0,0,0,6],
                [0,0,3,2,0,0,0,8,0],
                [0,6,0,5,0,0,0,0,9],
                [0,0,4,0,0,0,0,3,0],
                [0,0,0,0,0,9,7,0,0]
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

    def __init__(self):
        super(SuSol, self).__init__()

        #############CONFIG#######################################################
        self.barvyBarev = ["#8888ff","#88ff88","#ff8888","#ffff88","#ff88ff","#88ffff","#880088","#888800","#008888"]
        self.barvaKurzoru = "#ffbbbb"
        self.barvaKandidatu = "#000000"
        self.barvaHvezdickyUpoznamky = "#000000"
        self.barvaAkronymu = "#000000"
        self.barvaZadanychCisel = "#000000"
        self.barvaDoplnenychCisel = "#0000ff"
        self.barvaSouradnicPolicek = "#888888"

        self.pismoCeleAplikace = "Arial"

        self.zobrazitSouradnice = True
        #############CONFIG#######################################################

        self.curX = 0
        self.curY = 0
        self.Xpos = 0
        self.Ypos = 0
        self.margin = 0
        self.bottom = 0
        self.right = 0

        self.candMode = False
        self.autoColor = False
        self.casBezi = False
        self.time = 0
        self.timestamp = 0
        self.timeBackup = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.pricitat_cas)

        self.rezim = "reseni"
        self.zadani = [
            [0,0,5,3,0,0,0,0,0],
            [8,0,0,0,0,0,0,2,0],
            [0,7,0,0,1,0,5,0,0],
            [4,0,0,0,0,5,3,0,0],
            [0,1,0,0,7,0,0,0,6],
            [0,0,3,2,0,0,0,8,0],
            [0,6,0,5,0,0,0,0,9],
            [0,0,4,0,0,0,0,3,0],
            [0,0,0,0,0,9,7,0,0]
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

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Windows"))
        self.setWindowTitle("SuSol")
        vyska = QtGui.QDesktopWidget().screenGeometry().height()
        sirka = QtGui.QDesktopWidget().screenGeometry().width()
        #vyska = 480
        #sirka = 640
        self.resize(sirka,vyska)

        mainMenu1 = self.menuBar().addMenu("&SuSol")
        mainMenu2 = self.menuBar().addMenu("S&udoku")
        for i in QtGui.QStyleFactory.keys():
            print(i)

        mainMenu1.addAction("Pomoc\tF1")
        mainMenu1.addAction("O programu")
        mainMenu1.addSeparator()
        mainMenu1.addAction("Konec\tAlt+F4",self.quit)
        mainMenu2.addAction("Nové sudoku\tCtrl+N")
        mainMenu2.addAction("Načíst sudoku\tCtrl+O")
        mainMenu2.addAction("Uložit sudoku\tCtrl+S")
        mainMenu2.addAction("Uložit sudoku jako\tF12")
        mainMenu2.addSeparator()
        mainMenu2.addAction("Soutěžní režim")
        mainMenu2.addAction("Výsledky")

        mainMenu1.setFocusPolicy(QtCore.Qt.NoFocus)
        mainMenu2.setFocusPolicy(QtCore.Qt.NoFocus)


        self.tabs = QtGui.QTabWidget(self)
        self.tabs.setFocusPolicy(QtCore.Qt.NoFocus)
        pismo = QtGui.QFont("Arial")
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


        pismo = QtGui.QFont("Arial")
        pismo.setPixelSize(15)

        self.candLabel = QtGui.QLabel()
        self.candLabel.setText("Kandidáti")
        self.candLabel.setFont(pismo)
        self.candLabel.setMinimumHeight(30)
        self.candLabel.setMinimumWidth(80)

        pismo = QtGui.QFont("Arial")
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

        self.shortNoteBtn = QtGui.QPushButton()
        self.shortNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shortNoteBtn.setText("&Editovat")
        self.shortNoteBtn.clicked.connect(self.editShortNote)

        self.shortNoteTB = QtGui.QLineEdit()
        self.shortNoteTB.setDisabled(True)
        self.shortNoteTB.setStyleSheet("background-color: #ffffff")

        self.longNoteLabel = QtGui.QLabel()
        self.longNoteLabel.setText("Poznámka")
        self.longNoteLabel.setMinimumWidth(80)

        self.longNoteBtn = QtGui.QPushButton()
        self.longNoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.longNoteBtn.setText("E&ditovat")
        self.longNoteBtn.clicked.connect(self.editLongNote)

        self.longNoteTB = QtGui.QTextEdit()
        self.longNoteTB.setDisabled(True)

        self.cas = QtGui.QLabel()
        self.cas.setText("Čas: 0:00:00")
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

        self.poleLabel = QtGui.QLabel("A1")
        self.poleLabel.setStyleSheet("color: red")
        pismo = QtGui.QFont("Arial")
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
        vBoxlayout.addWidget(self.nastaveniBarev,15,0,1,11)
        vBoxlayout.addWidget(self.restartovatBtn,16,0,1,11)
        self.tab1.setLayout(vBoxlayout)

        vBoxlayout = QtGui.QGridLayout()
        vBoxlayout.addWidget(self.vygenerovatKandidatyBtn)
        vBoxlayout.addWidget(self.vyresitBtn)
        self.tab2.setLayout(vBoxlayout)

        self.tabs.addTab(self.tab1,"Řešení")
        self.tabs.addTab(self.tab2,"Pomoc počítače")
        self.tabs.show()



        self.show()
        self.upravitWidgety()
        self.setFocus()

app = QtGui.QApplication(sys.argv)
okno = SuSol()
sys.exit(app.exec_())

#TODO dalsi featury v pomoci pocitace