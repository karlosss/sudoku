import solver
zadani = [
[0,0,0,0,4,0,8,0,2],
[0,0,0,7,0,0,0,0,0],
[1,0,0,0,6,3,0,0,0],
[0,7,0,2,0,0,4,0,0],
[0,0,0,8,0,5,0,9,0],
[5,0,0,0,3,0,0,0,0],
[7,0,0,0,0,4,0,0,3],
[0,6,0,0,0,0,0,1,4],
[0,5,3,0,2,0,9,0,0]
]

reseni = solver.solve(zadani,mode=1,bf=True)
for i in reseni:
    print ""
    print ""
    print ""
    for j in i:
        print j

print len(reseni)