#coding: utf8

import gtk
import glib
import cairo
import math
import Tkinter
import gobject
import time
from copy import deepcopy
import pango
from misc import sameChars, arr2str, str2arr

ZADANI = [
[0, 0, 0, 0, 4, 0, 8, 0, 2],
[0, 0, 0, 7, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 6, 3, 0, 0, 0],
[0, 7, 0, 2, 0, 0, 4, 0, 0],
[0, 0, 0, 8, 0, 5, 0, 9, 0],
[5, 0, 0, 0, 3, 0, 0, 0, 0],
[7, 0, 0, 0, 0, 4, 0, 0, 3],
[0, 6, 0, 0, 0, 0, 0, 1, 4],
[0, 5, 3, 0, 2, 0, 9, 0, 0]
]

USER_RESENI = [
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

USER_KANDIDATI = [
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

USER_ZNACKY = [
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""]
]

USER_NOTES = [
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""],
["","","","","","","","",""]
]

class Prefs(gtk.Dialog):

    def clickCancel(self, x):
        self.destroy()

    def clickOK(self, x):
        self.destroy()

    def toggle1(self,x):
        if self.customSudokuEntry1.get_sensitive():
            self.customSudokuEntry1.set_sensitive(False)
        else:
            self.customSudokuEntry1.set_sensitive(True)

    def toggle2(self,x):
        if self.customSudokuChB2.get_sensitive():
            self.customSudokuChB2.set_sensitive(False)
        else:
            self.customSudokuChB2.set_sensitive(True)

    def entry_checkInput(self,x,y):
        try:
            if self.customSudokuEntry1.get_text()[len(self.customSudokuEntry1.get_text())-1].isdigit() == False and len(self.customSudokuEntry1.get_text()) == 2:
                self.customSudokuEntry1.set_text(self.customSudokuEntry1.get_text()[0])
                self.customSudokuEntry1.set_position(-1)
            elif self.customSudokuEntry1.get_text()[len(self.customSudokuEntry1.get_text())-1].isdigit() == False and len(self.customSudokuEntry1.get_text()) == 1:
                self.customSudokuEntry1.set_text("")
            elif self.customSudokuEntry1.get_text()[0] == "0" and len(self.customSudokuEntry1.get_text()) == 2:
                self.customSudokuEntry1.set_text(self.customSudokuEntry1.get_text()[1])
                self.customSudokuEntry1.set_position(-1)
        except IndexError:
            pass

        try:
            if int(self.customSudokuEntry1.get_text()) > 80:
                self.customSudokuEntry1.set_text("80")
                self.customSudokuEntry1.set_position(-1)
        except ValueError:
            pass

    def generalToggle(self,x):
        if self.generalChB1.get_active():
            print("1")
        else:
            print("2")

    def __init__(self, x):
        gtk.Dialog.__init__(self,"Preferences",hlavni)

        self.set_size_request(500, 600)
        self.set_modal(True)

        self.tooltips = gtk.Tooltips()
        self.notebook = gtk.Notebook()
        self.notebook.set_tab_pos(gtk.POS_TOP)

        self.contentBox = self.get_content_area()
        self.buttonBox = self.get_action_area()
        self.customSudokuFixed = gtk.Fixed()
        self.generalFixed = gtk.Fixed()

        self.notebook.append_page(self.generalFixed,gtk.Label("General"))
        self.notebook.append_page(self.customSudokuFixed, gtk.Label("Custom Sudoku"))



        self.generalChB1 = gtk.CheckButton("Generate puzzles in the background")
        self.generalChB1.set_active(True)
        self.generalChB1.connect("toggled",self.generalToggle)
        self.tooltips.set_tip(self.generalChB1, "If checked, the generator will run in the background. The puzzles will be available immediately but the program might be slower.")



        self.generalFixed.put(self.generalChB1,20,20)








        self.customSudokuChB1 = gtk.CheckButton("Generate single-solution puzzles only")
        self.tooltips.set_tip(self.customSudokuChB1, "If checked, all the generated puzzles will have exactly one solution.")
        self.customSudokuChB1.set_active(True)
        self.customSudokuChB1.connect("toggled",self.toggle2)

        self.customSudokuChB2 = gtk.CheckButton("Use advanced generating methods")
        self.tooltips.set_tip(self.customSudokuChB2, "If checked, the generator uses more complex algorithm to generate puzzles. The puzzle is slightly more difficult but it takes longer to generate.")


        self.customSudokuChB3 = gtk.CheckButton("Minimum amount of pre-filled numbers")
        self.customSudokuChB3.connect("toggled",self.toggle1)
        self.tooltips.set_tip(self.customSudokuChB3, "If checked, the generator will fill in at least the given amount of numbers. Takes an integer argument in range from 0 to 80.\n\nIf unchecked and multiple-solution puzzles are allowed, the generator will yield an empty grid.")

        self.customSudokuEntry1 = gtk.Entry()
        self.customSudokuEntry1.set_size_request(width=30, height=-1)
        self.customSudokuEntry1.set_sensitive(False)
        self.customSudokuEntry1.set_text("0")
        self.customSudokuEntry1.set_max_length(2)
        self.customSudokuEntry1.connect("key-press-event",self.entry_checkInput)
        self.customSudokuEntry1.connect("key-release-event",self.entry_checkInput)

        self.canc = gtk.Button(stock=gtk.STOCK_CANCEL)
        self.canc.connect("clicked",self.clickCancel)

        self.ok = gtk.Button(stock=gtk.STOCK_OK)
        self.ok.connect("clicked",self.clickOK)

        self.defs = gtk.Button("Restore Defaults")

        self.contentBox.add(self.notebook)
        self.buttonBox.add(self.defs)
        self.buttonBox.add(self.canc)
        self.buttonBox.add(self.ok)
        self.customSudokuFixed.put(self.customSudokuChB1,20,20)
        self.customSudokuFixed.put(self.customSudokuChB2,70,50)
        self.customSudokuFixed.put(self.customSudokuChB3,20,100)
        self.customSudokuFixed.put(self.customSudokuEntry1,310,100)

        self.show_all()

class PyApp(gtk.Window):

    def openPrefs(self, x):
        Prefs(self)

    def openAbout(self, x):
        md = gtk.MessageDialog(self,gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "SuSol\n\nVersion: 0.0\nKarel Jilek")
        md.run()
        md.destroy()

    def klik(self,x,y):

        self.setNumfilInactive()
        evX = y.x
        evY = y.y

        evX = evX // 80
        evY = evY // 80

        self.sudokuX = int(evX)
        self.sudokuY = int(evY)

        if ZADANI[self.sudokuY][self.sudokuX]+USER_RESENI[self.sudokuY][self.sudokuX] != 0:
            self.entryNumberFilled.set_text(str(ZADANI[self.sudokuY][self.sudokuX]+USER_RESENI[self.sudokuY][self.sudokuX]))
        else:
            self.entryNumberFilled.set_text("")

        if len(USER_KANDIDATI[self.sudokuY][self.sudokuX]) > 0:
            self.entryKandidati.set_text(arr2str(USER_KANDIDATI[self.sudokuY][self.sudokuX]))
        else:
            self.entryKandidati.set_text("")

        self.entryZnacka.set_text(USER_ZNACKY[self.sudokuY][self.sudokuX])
        self.entryPoznamkaBuff.set_text(USER_NOTES[self.sudokuY][self.sudokuX])
        self.entryPoznamka.get_buffer()

        if ZADANI[self.sudokuY][self.sudokuX] != 0:
            self.setNumfilDisable()
        else:
            self.entryNumberFilled.set_sensitive(True)
            self.entryNumberFilled.set_alignment(xalign=0.5)
            self.entryKandidati.set_sensitive(True)

        self.vykresli()

    def zapisCislo(self,cislo):
        global USER_RESENI, USER_KANDIDATI
        if not self.tabMode:
            if ZADANI[self.sudokuY][self.sudokuX] == 0:
                USER_RESENI[self.sudokuY][self.sudokuX] = cislo
        else:
            if ZADANI[self.sudokuY][self.sudokuX] == 0 and cislo != 0:
                if cislo not in USER_KANDIDATI[self.sudokuY][self.sudokuX]:
                    USER_KANDIDATI[self.sudokuY][self.sudokuX].append(cislo)
                    USER_KANDIDATI[self.sudokuY][self.sudokuX].sort()
                else:
                    USER_KANDIDATI[self.sudokuY][self.sudokuX].remove(cislo)
                    USER_KANDIDATI[self.sudokuY][self.sudokuX].sort()
        self.expose(None,None)


    def swapMode(self):
        if self.tabMode == True:
            self.tabMode = False
        else:
            self.tabMode = True
        self.expose(None,None)


    def klavesa(self,x,y):
        if y.keyval == 65361: #sipky
            self.sudokuX = (self.sudokuX-1)%9
            self.vykresli()
        elif y.keyval == 65362:
            self.sudokuY = (self.sudokuY-1)%9
            self.vykresli()
        elif y.keyval == 65363:
            self.sudokuX = (self.sudokuX+1)%9
            self.vykresli()
        elif y.keyval == 65364:
            self.sudokuY = (self.sudokuY+1)%9
            self.vykresli()

        elif y.keyval == 49: #cisla 1-9 a delete
            self.zapisCislo(1)
        elif y.keyval == 50:
            self.zapisCislo(2)
        elif y.keyval == 51:
            self.zapisCislo(3)
        elif y.keyval == 52:
            self.zapisCislo(4)
        elif y.keyval == 53:
            self.zapisCislo(5)
        elif y.keyval == 54:
            self.zapisCislo(6)
        elif y.keyval == 55:
            self.zapisCislo(7)
        elif y.keyval == 56:
            self.zapisCislo(8)
        elif y.keyval == 57:
            self.zapisCislo(9)
        elif y.keyval == 65535:
            self.zapisCislo(0)

        elif y.keyval == 65289: #tab
            self.swapMode()

        elif y.keyval == 65293 and not self.numfilAktivni and ZADANI[self.sudokuY][self.sudokuX] == 0: #enter
            if not self.skipEnter:
                print("asdf")
                self.setNumfilActive(None,None)
                self.set_focus(self.entryNumberFilled)
                self.skipEnter = True
        elif y.keyval == 65293 and not self.numfilAktivni and ZADANI[self.sudokuY][self.sudokuX] != 0: #enter na zadane
            if not self.skipEnter:
                print("asdf222")
                self.numfilAktivni = True
                self.entryZnacka.modify_cursor(gtk.gdk.Color("#000000"),gtk.gdk.Color("#000000"))
                self.entryZnacka.set_property("editable", True)
                self.entryZnacka.set_flags(gtk.CAN_FOCUS)
                self.entryPoznamka.modify_cursor(gtk.gdk.Color("#000000"),gtk.gdk.Color("#000000"))
                self.entryPoznamka.set_property("editable", True)
                self.entryPoznamka.set_flags(gtk.CAN_FOCUS)
                self.disconnect(self.event3)
                self.set_focus(self.entryZnacka)
                self.skipEnter = True


        print(self.sudokuY,self.sudokuX)

        if ZADANI[self.sudokuY][self.sudokuX]+USER_RESENI[self.sudokuY][self.sudokuX] != 0:
            self.entryNumberFilled.set_text(str(ZADANI[self.sudokuY][self.sudokuX]+USER_RESENI[self.sudokuY][self.sudokuX]))
        else:
            self.entryNumberFilled.set_text("")

        if len(USER_KANDIDATI[self.sudokuY][self.sudokuX]) > 0:
            self.entryKandidati.set_text(arr2str(USER_KANDIDATI[self.sudokuY][self.sudokuX]))
        else:
            self.entryKandidati.set_text("")

        self.entryZnacka.set_text(USER_ZNACKY[self.sudokuY][self.sudokuX])
        self.entryPoznamkaBuff.set_text(USER_NOTES[self.sudokuY][self.sudokuX])
        self.entryPoznamka.get_buffer()

        if ZADANI[self.sudokuY][self.sudokuX] != 0:
            self.setNumfilDisable()
        else:
            self.entryNumberFilled.set_sensitive(True)
            self.entryKandidati.set_sensitive(True)

    def vykresli(self):
        self.expose(None,None)
        return self.redrawSudoku

    def znicit(self,x):
        self.darea.disconnect(self.event1)
        self.darea.disconnect(self.event2)
        self.disconnect(self.event3)
        self.redrawSudoku = False
        self.fixed.hide_all()
        gtk.main_quit()

    def setNumfilActive(self,x,y):
        if self.numfilAktivni == False:
            self.numfilAktivni = True
            self.entryNumberFilled.modify_cursor(gtk.gdk.Color("#000000"),gtk.gdk.Color("#000000"))
            self.entryNumberFilled.set_property("editable", True)
            self.entryNumberFilled.set_flags(gtk.CAN_FOCUS)
            self.entryKandidati.modify_cursor(gtk.gdk.Color("#000000"),gtk.gdk.Color("#000000"))
            self.entryKandidati.set_property("editable", True)
            self.entryKandidati.set_flags(gtk.CAN_FOCUS)
            self.entryZnacka.modify_cursor(gtk.gdk.Color("#000000"),gtk.gdk.Color("#000000"))
            self.entryZnacka.set_property("editable", True)
            self.entryZnacka.set_flags(gtk.CAN_FOCUS)
            self.entryPoznamka.modify_cursor(gtk.gdk.Color("#000000"),gtk.gdk.Color("#000000"))
            self.entryPoznamka.set_property("editable", True)
            self.entryPoznamka.set_flags(gtk.CAN_FOCUS)
            self.disconnect(self.event3)

    def setNumfilInactive(self):
        if self.numfilAktivni:
            self.numfilAktivni = False
            self.entryNumberFilled.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
            self.entryNumberFilled.set_property("editable", False)
            self.entryNumberFilled.unset_flags(gtk.CAN_FOCUS)
            self.entryKandidati.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
            self.entryKandidati.set_property("editable", False)
            self.entryKandidati.unset_flags(gtk.CAN_FOCUS)
            self.entryZnacka.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
            self.entryZnacka.set_property("editable", False)
            self.entryZnacka.unset_flags(gtk.CAN_FOCUS)
            self.entryPoznamka.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
            self.entryPoznamka.set_property("editable", False)
            self.entryPoznamka.unset_flags(gtk.CAN_FOCUS)
            self.event3 = self.connect("key_press_event",self.klavesa)

    def setNumfilDisable(self):
        self.entryNumberFilled.set_sensitive(False)
        self.entryKandidati.set_sensitive(False)

    def checkInputNumfil(self,x,y):
        print(y.keyval)

        try:
            if self.entryNumberFilled.get_text()[len(self.entryNumberFilled.get_text())-1] not in ("1","2","3","4","5","6","7","8","9") and len(self.entryNumberFilled.get_text()) == 2:
                self.entryNumberFilled.set_text(self.entryNumberFilled.get_text()[0])
                self.entryNumberFilled.set_position(-1)
            elif self.entryNumberFilled.get_text()[len(self.entryNumberFilled.get_text())-1] not in ("1","2","3","4","5","6","7","8","9") and len(self.entryNumberFilled.get_text()) == 1:
                self.entryNumberFilled.set_text("")

            if y.keyval in range(49,58,1) and len(self.entryNumberFilled.get_text()) == 1:
                self.entryNumberFilled.set_text(str(y.keyval-48))
                print("asdf")

        except IndexError:
            pass


        if ZADANI[self.sudokuY][self.sudokuX] == 0:
            if len(self.entryNumberFilled.get_text()) > 0:
                USER_RESENI[self.sudokuY][self.sudokuX] = int(self.entryNumberFilled.get_text())
            else:
                USER_RESENI[self.sudokuY][self.sudokuX] = 0


    def checkInputKand(self,x,y):
        global USER_KANDIDATI
        print(y.keyval)

        a = self.entryKandidati.get_text()
        newstr = ""
        for i in a:
            if i in newstr:
                continue
            if i in ("1","2","3","4","5","6","7","8","9"):
                newstr=newstr+i

        self.entryKandidati.set_text(newstr)
        if newstr != a:
            self.entryKandidati.set_position(-1)
        b = str2arr(newstr)
        b.sort()
        USER_KANDIDATI[self.sudokuY][self.sudokuX] = deepcopy(b)

    def inputZnacka(self,x,y):
        global USER_ZNACKY
        USER_ZNACKY[self.sudokuY][self.sudokuX] = self.entryZnacka.get_text()

    def inputPoznamka(self,x,y):
        global USER_NOTES

        if y.keyval == 65307:
            self.enter(None,gtk.gdk.Event(gtk.gdk.KEY_PRESS))
            return False
        USER_NOTES[self.sudokuY][self.sudokuX] = self.entryPoznamkaBuff.get_text(self.entryPoznamkaBuff.get_start_iter(),self.entryPoznamkaBuff.get_end_iter())
        print(USER_NOTES[self.sudokuY][self.sudokuX])

    def enter(self,x,y):
        if y.keyval == 0:
            y.keyval = 65293
        print(self.skipEnter,y.keyval,self.numfilAktivni,ZADANI[self.sudokuY][self.sudokuX])
        if not self.skipEnter:
            if y.keyval == 65293 and self.numfilAktivni and ZADANI[self.sudokuY][self.sudokuX] == 0:
                self.setNumfilInactive()
                print("asdfiu")
                self.entryKandidati.select_region(0,0)
                self.entryZnacka.select_region(0,0)
            elif y.keyval == 65293 and self.numfilAktivni and ZADANI[self.sudokuY][self.sudokuX] != 0:
                self.numfilAktivni = False
                self.entryZnacka.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
                self.entryZnacka.set_property("editable", False)
                self.entryZnacka.unset_flags(gtk.CAN_FOCUS)
                self.event3 = self.connect("key_press_event",self.klavesa)
                print("asdfiu222")
                self.entryKandidati.select_region(0,0)
                self.entryZnacka.select_region(0,0)
        self.skipEnter = False

    def __init__(self):
        super(PyApp, self).__init__()


        self.sudokuX = 0
        self.sudokuY = 0
        self.redrawSudoku = True
        self.tabMode = False
        self.numfilAktivni = False
        self.skipEnter = False




        self.set_title("SuSol")
        self.set_size_request(1200, 800)
        self.set_position(gtk.WIN_POS_CENTER)

        try:
            self.set_icon_from_file("snapshot1.png")
        except:
            print("ikona nenalezena")
            pass

        # self.btn1 = gtk.Button("Button")
        # self.btn1.set_sensitive(False)
        self.btn2 = gtk.Button("Tlacitka")
        # self.btn3 = gtk.Button(stock=gtk.STOCK_CLOSE)
        # self.btn4 = gtk.Button("Button")
        # self.btn4.set_size_request(800, 100)

        self.fixed = gtk.Fixed()
        self.add(self.fixed)

        self.darea = gtk.DrawingArea()
        self.darea.set_size_request(720,720)

        self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#ffffff'))

        self.fixed.put(self.darea,20,60)

        self.event1 = self.darea.connect("expose_event", self.expose)
        self.event2 = self.darea.connect("button_press_event", self.klik)
        self.event3 = self.connect("key_press_event",self.klavesa)
        self.darea.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        # gobject.timeout_add(100,self.vykresli)


        self.reseniSudoku = gtk.Fixed()
        self.fixed.put(self.reseniSudoku,800,100)

        self.entryNumberFilled = gtk.Entry()
        self.entryNumberFilled.set_size_request(width=110,height=-1)
        self.entryNumberFilled.set_max_length(1)
        self.entryNumberFilled.set_alignment(xalign=0.5)
        self.entryNumberFilled.set_property("editable", False)
        self.entryNumberFilled.unset_flags(gtk.CAN_FOCUS)
        self.entryNumberFilled.modify_font(pango.FontDescription("Arial 60"))
        self.entryNumberFilled.connect("button_press_event",self.setNumfilActive)
        self.entryNumberFilled.connect("key_release_event",self.checkInputNumfil)
        self.entryNumberFilled.connect("key_press_event",self.enter)
        self.entryNumberFilled.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
        self.reseniSudoku.put(self.entryNumberFilled,0,0)

        self.entryKandidati = gtk.Entry()
        self.entryKandidati.set_size_request(width=110,height=-1)
        self.entryKandidati.set_max_length(9)
        self.entryKandidati.set_property("editable", False)
        self.entryKandidati.unset_flags(gtk.CAN_FOCUS)
        self.entryKandidati.modify_font(pango.FontDescription("Arial 14"))
        self.entryKandidati.connect("button_press_event",self.setNumfilActive)
        self.entryKandidati.connect("key_release_event",self.checkInputKand)
        self.entryKandidati.connect("key_press_event",self.enter)
        self.entryKandidati.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
        self.reseniSudoku.put(self.entryKandidati,0,150)

        self.entryZnacka = gtk.Entry()
        self.entryZnacka.set_size_request(width=110,height=-1)
        self.entryZnacka.set_max_length(8)
        self.entryZnacka.set_property("editable", False)
        self.entryZnacka.unset_flags(gtk.CAN_FOCUS)
        self.entryZnacka.modify_font(pango.FontDescription("Arial 13"))
        self.entryZnacka.connect("button_press_event",self.setNumfilActive)
        self.entryZnacka.connect("key_release_event",self.inputZnacka)
        self.entryZnacka.connect("key_press_event",self.enter)
        self.entryZnacka.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
        self.reseniSudoku.put(self.entryZnacka,0,250)

        self.entryPoznamka = gtk.TextView()
        self.entryPoznamka.set_wrap_mode(gtk.WRAP_WORD_CHAR)
        self.entryPoznamkaBuff = gtk.TextBuffer()
        self.entryPoznamka.set_buffer(self.entryPoznamkaBuff)
        self.entryPoznamka.set_size_request(width=150,height=100)
        self.entryPoznamka.set_property("editable", False)
        self.entryPoznamka.unset_flags(gtk.CAN_FOCUS)
        self.entryPoznamka.modify_cursor(gtk.gdk.Color("#ffffff"),gtk.gdk.Color("#ffffff"))
        self.entryPoznamka.connect("button_press_event",self.setNumfilActive)
        self.entryPoznamka.connect("key_release_event",self.inputPoznamka)
        self.entryPoznamka.modify_font(pango.FontDescription("Arial 11"))
        self.reseniSudoku.put(self.entryPoznamka,0,350)



        self.reseniSudoku.show_all()

        self.mb = gtk.MenuBar()

        self.agr = gtk.AccelGroup()
        self.add_accel_group(self.agr)

        self.m1s1 = gtk.Menu()
        self.m2s1 = gtk.Menu()
        self.m3s1 = gtk.Menu()
        self.m1 = gtk.MenuItem("SuSol")
        self.m2 = gtk.MenuItem("Sudoku")
        self.m3 = gtk.MenuItem("Results & Statistics")
        self.m1.set_submenu(self.m1s1)
        self.m2.set_submenu(self.m2s1)
        self.m3.set_submenu(self.m3s1)

        self.about = gtk.ImageMenuItem(gtk.STOCK_ABOUT)

        self.help = gtk.ImageMenuItem(gtk.STOCK_HELP,self.agr)
        self.key, self.mod = gtk.accelerator_parse("<Control>H")
        self.help.add_accelerator("activate", self.agr, self.key, self.mod, gtk.ACCEL_VISIBLE)

        self.preferences = gtk.ImageMenuItem(gtk.STOCK_PREFERENCES)

        self.exit = gtk.ImageMenuItem(gtk.STOCK_QUIT,self.agr)
        self.key, self.mod = gtk.accelerator_parse("<Control>Q")
        self.exit.add_accelerator("activate", self.agr, self.key, self.mod, gtk.ACCEL_VISIBLE)




        self.new = gtk.ImageMenuItem(gtk.STOCK_NEW,self.agr)
        self.key, self.mod = gtk.accelerator_parse("<Control>N")
        self.new.add_accelerator("activate", self.agr, self.key, self.mod, gtk.ACCEL_VISIBLE)

        self.open = gtk.ImageMenuItem(gtk.STOCK_OPEN,self.agr)
        self.key, self.mod = gtk.accelerator_parse("<Control>O")
        self.open.add_accelerator("activate", self.agr, self.key, self.mod, gtk.ACCEL_VISIBLE)

        self.competitive = gtk.MenuItem("Competitive Mode")

        self.competitive2 = gtk.MenuItem("Competitive Mode")

        self.overall = gtk.MenuItem("Overall Statistics")




        self.exit.connect("activate", self.znicit)
        self.preferences.connect("activate",self.openPrefs)
        self.about.connect("activate",self.openAbout)
        self.help.connect("activate",self.znicit)



        self.m1s1.append(self.help)
        self.m1s1.append(self.about)
        sep = gtk.SeparatorMenuItem()
        self.m1s1.append(sep)
        self.m1s1.append(self.preferences)
        sep = gtk.SeparatorMenuItem()
        self.m1s1.append(sep)
        self.m1s1.append(self.exit)

        self.m2s1.append(self.new)
        self.m2s1.append(self.open)
        sep = gtk.SeparatorMenuItem()
        self.m2s1.append(sep)
        self.m2s1.append(self.competitive)

        self.m3s1.append(self.competitive2)
        self.m3s1.append(self.overall)



        self.mb.append(self.m1)
        self.mb.append(self.m2)
        self.mb.append(self.m3)

        self.fixed.put(self.mb, 0, 0)

        self.connect("destroy", gtk.main_quit)

        self.show_all()

    def expose(self,x,y):
        self.entryNumberFilled.select_region(0,0)
        self.entryNumberFilled.set_position(1)
        self.cr = self.darea.window.cairo_create()

        #kurzor
        if not self.tabMode:
            self.cr.save()
            self.cr.set_source_rgb(1, 0.8, 0.8)
            self.cr.set_line_width(5)
            self.cr.rectangle(self.sudokuX*80,self.sudokuY*80,80,80)
            self.cr.fill()
            self.cr.restore()
        else:
            self.cr.save()
            self.cr.set_source_rgb(1, 0.8, 0.8)
            self.cr.set_line_width(5)
            self.cr.rectangle(self.sudokuX*80,self.sudokuY*80,80,18)
            self.cr.fill()
            self.cr.restore()

        #cisla ze zadani
        self.cr.save()
        self.cr.set_source_rgb(0,0,0)
        self.cr.set_font_size(70)
        self.cr.select_font_face("Arial",cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

        for i in range(0,9,1):
            for j in range(0,9,1):
                if ZADANI[i][j] != 0:
                    self.cr.move_to(j*80+22,i*80+70)
                    self.cr.show_text(str(ZADANI[i][j]))

        self.cr.restore()

        #cisla z reseni
        self.cr.save()
        self.cr.set_source_rgb(0,0,1)
        self.cr.set_font_size(70)
        self.cr.select_font_face("Arial",cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        for i in range(0,9,1):
            for j in range(0,9,1):
                if USER_RESENI[i][j] != 0:
                    self.cr.move_to(j*80+22,i*80+70)
                    self.cr.show_text(str(USER_RESENI[i][j]))

        self.cr.restore()

        #kandidati
        self.cr.save()
        self.cr.set_source_rgb(0,0,0)
        self.cr.set_font_size(12)
        self.cr.select_font_face("Arial",cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        for i in range(0,9,1):
            for j in range(0,9,1):
                self.cr.move_to(j*80+3,i*80+13)
                tisk = ""
                for kandidat in USER_KANDIDATI[i][j]:
                    tisk = tisk + str(kandidat)
                self.cr.show_text(tisk)

        self.cr.restore()

        #znacky
        self.cr.save()
        self.cr.set_source_rgb(0,0,0)
        self.cr.set_font_size(11)
        self.cr.select_font_face("Arial",cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        for i in range(0,9,1):
            for j in range(0,9,1):
                self.cr.move_to(j*80+5,i*80+77)
                if USER_ZNACKY[i][j] != None and USER_ZNACKY[i][j] != "":
                    self.cr.show_text(USER_ZNACKY[i][j])
                else:
                    continue

        self.cr.restore()

        #poznamky
        self.cr.save()
        self.cr.set_source_rgb(0,0,0)
        self.cr.set_font_size(20)
        self.cr.select_font_face("Arial",cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        for i in range(0,9,1):
            for j in range(0,9,1):
                self.cr.move_to(j*80+70,i*80+75)
                if USER_NOTES[i][j] != "":
                    self.cr.show_text("*")
                else:
                    continue

        self.cr.restore()

        #mrizka
        self.cr.set_source_rgb(0, 0, 0)
        for i in range(1,9,1):
            self.cr.save()
            if i in (3,6):
                self.cr.set_line_width(5)
            else:
                self.cr.set_line_width(1)

            self.cr.move_to(0.5+i*80,0)
            self.cr.rel_line_to(0,720)

            self.cr.stroke()
            self.cr.restore()

        for i in range(1,9,1):
            self.cr.save()
            if i in (3,6):
                self.cr.set_line_width(5)
            else:
                self.cr.set_line_width(1)

            self.cr.move_to(0,0.5+i*80)
            self.cr.rel_line_to(720,0)

            self.cr.stroke()
            self.cr.restore()

        alloc = self.get_allocation()
        self.queue_draw_area(alloc.x, alloc.y, alloc.width, alloc.height)
        self.window.process_updates(True)








hlavni = PyApp()
gtk.main()