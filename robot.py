for i in range(1024,2047,1):
    string = str(i)
    soucin = 0
    for a in string:
        a = int(a)
        soucin = soucin+a**2
    if soucin == 135:
        print(i)

