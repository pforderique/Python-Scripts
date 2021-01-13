class Matrix():
    '''replaces the common array structure for a matrix with special properties'''
    def __init__(self, matrix:list) -> None:
        self.matrix = matrix
        self.properties = []
