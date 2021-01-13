'''
@author Piero Orderique
@date 12 Jan 2021

This file contain is the linear algebra API (library)
'''

class Matrix():
    '''replaces the common array structure for a matrix with special properties'''
    def __init__(self, matrix:list) -> None:
        self.matrix = matrix
        self.properties = []

    def dot(self, other):
        """returns dot product with other matrix"""
        pass

    def transpose(self):
        '''transposes self'''
        pass

    def dim(self):
        '''returns dimension of matrix'''
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __str__(self) -> str:
        rep = ''
        pass 