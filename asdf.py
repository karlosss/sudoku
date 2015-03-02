import solver2,solver
import time

# import solver
#
# # zadani = [
# #
# # [0, 0, 0,     6, 8, 4,     0, 1, 0],
# # [0, 0, 0,     0, 0, 0,     0, 3, 0],
# # [6, 1, 0,     0, 0, 0,     7, 0, 0],
# #
# # [0, 2, 0,     9, 0, 7,     3, 6, 0],
# # [0, 0, 0,     0, 0, 2,     0, 4, 1],
# # [0, 0, 4,     0, 6, 0,     9, 0, 2],
# #
# # [0, 5, 2,     8, 0, 1,     0, 0, 0],
# # [0, 0, 0,     0, 0, 0,     0, 0, 0],
# # [0, 0, 9,     0, 3, 0,     0, 0, 0]
# #
# # ]
#
# zadani = [
#     [1,2,3,4,5,6,7,8,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0]
#     ]
#
# reseni = solver.solve(zadani, mode=1)
#
# for i in reseni:
#     for j in i:
#         print(j)

sudoku = [
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

# sudoku = [
#     [0,6,1,0,0,7,0,0,3],
#     [0,9,2,0,0,3,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,8,5,3,0,0,0,0],
#     [0,0,0,0,0,0,5,0,4],
#     [5,0,0,0,0,8,0,0,0],
#     [0,4,0,0,0,0,0,0,1],
#     [0,0,0,1,6,0,8,0,0],
#     [6,0,0,0,0,0,0,0,0]
#     ]

# sudoku = [
#     [0,2,0,1,0,0,0,0,0],
#     [0,0,6,0,0,0,0,0,0],
#     [5,0,3,0,0,0,0,0,0],
#     [0,3,0,0,0,0,0,0,0],
#     [0,1,0,0,2,0,6,0,0],
#     [0,0,0,6,0,0,0,0,0],
#     [8,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [9,0,0,0,0,0,0,0,0]
# ]


start = time.time()
solver2.solvePC(sudoku)
print time.time()-start