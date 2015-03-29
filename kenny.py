# from random import randint
#
# a = 0
# b = 0
#
# jednicka = 0.0
# nula = 0.0
#
# lidi = [1]
# for i in range(50):
#     lidi.append(0)
#
# while True:
#     lidi = [1]
#     for i in range(50):
#         lidi.append(0)
#     while True:
#         a = 0
#         b = 0
#         while a == b:
#             a = randint(0,50)
#             b = randint(0,50)
#
#         if randint(0,1) == 0:
#             lidi[a] = lidi[b]
#         else:
#             lidi[b] = lidi[a]
#
#         if 0 not in lidi:
#             jednicka = jednicka + 1
#             break
#         if 1 not in lidi:
#             nula = nula + 1
#             break
#
#     print(jednicka,nula,jednicka/nula)

# import math
# from random import random
#
# counter = 0.0
#
# for i in range(1000000):
#
#     stredY = random()
#
#     uhel = 2*math.pi*random()
#
#     y = stredY+math.sin(uhel)
#
#     if int(stredY) != int(y):
#         counter = counter + 1
#
# print(float(1000000.0/counter))

import solver2

for i in solver2.solvePC([
    [0,0,0,0,0,6,8,7,9],
    [8,9,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,3],
    [0,0,0,0,0,9,3,0,4],
    [0,0,0,5,0,0,1,0,0],
    [1,0,6,0,7,0,0,0,0],
    [0,7,0,3,0,0,2,4,0],
    [0,0,8,0,0,1,9,0,0],
    [9,0,0,0,0,4,0,0,0]
])[0][0]:
    print(i)














