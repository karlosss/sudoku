def sameChars(string):
    pole = []
    for i in string:
        if i in pole:
            return True
        else:
            pole.append(i)
    return False

def arr2str(array):
    string = ""
    for i in array:
        string = string + str(i)
    return string

def str2arr(string):
    arr = []
    for i in string:
        arr.append(int(i))
    return arr
