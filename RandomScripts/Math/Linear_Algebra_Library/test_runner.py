'''
@author Piero Orderique
@date 12 Jan 2021

This file is for testing linalg module
'''

from linalg import Matrix

mat1 = Matrix([
    [1, 1, 2],
    [3, 5, 8],
    [3, 0, 4],
])

mat2 = Matrix([
    [7, 0, 6],
    [9, 8, 7],
    [3, 9, 5],
])

print(mat1 + mat2)