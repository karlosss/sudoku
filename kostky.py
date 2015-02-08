from __future__ import print_function

kostka1 = ["G",["R","Y","Y","B"],"R"]
kostka2 = ["B",["Y","G","Y","Y"],"R"]
kostka3 = ["Y",["R","R","G","B"],"G"]
kostka4 = ["G",["Y","R","B","B"],"G"]

def rotateClockwise(kostka):
    zaloha = kostka[1][3]
    kostka[1][3] = kostka[1][2]
    kostka[1][2] = kostka[1][1]
    kostka[1][1] = kostka[1][0]
    kostka[1][0] = zaloha
    return kostka

def rotateCounterclockwise(kostka):
    zaloha = kostka[1][0]
    kostka[1][0] = kostka[1][1]
    kostka[1][1] = kostka[1][2]
    kostka[1][2] = kostka[1][3]
    kostka[1][3] = zaloha
    return kostka

def rotateUp(kostka):
    zaloha = kostka[0]
    kostka[0] = kostka[1][0]
    kostka[1][0] = kostka[2]
    kostka[2] = kostka[1][2]
    kostka[1][2] = zaloha
    return kostka

def rotateDown(kostka):
    zaloha = kostka[0]
    kostka[0] = kostka[1][2]
    kostka[1][2] = kostka[2]
    kostka[2] = kostka[1][0]
    kostka[1][0] = zaloha
    return kostka

def testWin(k1,k2,k3,k4):
    horni = k1[0]+k2[0]+k3[0]+k4[0]
    predni = k1[1][0]+k2[1][0]+k3[1][0]+k4[1][0]
    zadni = k1[1][2]+k2[1][2]+k3[1][2]+k4[1][2]
    dolni = k1[2]+k2[2]+k3[2]+k4[2]

    horni = horni.count("R") == 1 and horni.count("G") == 1 and horni.count("B") == 1 and horni.count("Y") == 1
    predni = predni.count("R") == 1 and predni.count("G") == 1 and predni.count("B") == 1 and predni.count("Y") == 1
    zadni = zadni.count("R") == 1 and zadni.count("G") == 1 and zadni.count("B") == 1 and zadni.count("Y") == 1
    dolni = dolni.count("R") == 1 and dolni.count("G") == 1 and dolni.count("B") == 1 and dolni.count("Y") == 1

    #print(horni,predni,zadni,dolni)

    if horni and predni and zadni and dolni:
        return True
    else:
        return False

def nastavRotaci(kostka,rot,pos):
    if pos == 1:
        kostka = rotateUp(kostka)
    elif pos == 2:
        kostka = rotateUp(kostka)
        kostka = rotateUp(kostka)
    elif pos == 3:
        kostka = rotateUp(kostka)
        kostka = rotateUp(kostka)
        kostka = rotateUp(kostka)
    elif pos == 4:
        kostka = rotateClockwise(kostka)
        kostka = rotateUp(kostka)
    elif pos == 5:
        kostka = rotateCounterclockwise(kostka)
        kostka = rotateUp(kostka)


    if rot == 0:
        return kostka
    elif rot == 1:
        kostka = rotateClockwise(kostka)
        return kostka
    elif rot == 2:
        kostka = rotateClockwise(kostka)
        kostka = rotateClockwise(kostka)
        return kostka
    elif rot == 3:
        kostka = rotateClockwise(kostka)
        kostka = rotateClockwise(kostka)
        kostka = rotateClockwise(kostka)
        return kostka

def controller(k1,k2,k3,k4):
    for pos1 in range(0,6,1):
        for rot1 in range(0,4,1):
            k1 = nastavRotaci(k1,rot1,pos1)

            for pos2 in range(0,6,1):
                for rot2 in range(0,4,1):
                    k2 = nastavRotaci(k2,rot2,pos2)

                    for pos3 in range(0,6,1):
                        for rot3 in range(0,4,1):
                            k3 = nastavRotaci(k3,rot3,pos3)

                            for pos4 in range(0,6,1):
                                for rot4 in range(0,4,1):
                                    k4 = nastavRotaci(k4,rot4,pos4)
                                    if testWin(k1,k2,k3,k4):
                                        print(pos1,rot1,pos2,rot2,pos3,rot3,pos4,rot4)


