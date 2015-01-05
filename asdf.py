import solver
zadani = [
[0,0,0,0,0,9,2,0,3],
[0,0,0,0,0,2,7,0,9],
[0,0,0,6,0,0,0,0,0],
[0,0,6,1,0,0,0,7,0],
[0,3,0,8,0,0,0,0,0],
[0,5,1,0,7,0,0,2,0],
[0,1,7,0,0,0,5,0,0],
[0,0,0,3,8,0,0,0,1],
[0,0,0,0,0,0,0,0,0]
]

reseni = solver.solve(zadani,mode=0,bf=True)
for i in reseni:
    print ""
    print ""
    print ""
    for j in i:
        print j

print len(reseni)