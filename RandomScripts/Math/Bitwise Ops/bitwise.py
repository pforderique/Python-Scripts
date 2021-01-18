'''
Bitwise methods
Following: CTCI 

@author Piero Orderique
@date 18 Jan 2021
'''

def getBit(num, i):
    '''shifts 1 over by i bits and performs AND'''
    return int(num & (1 << i) != 0) 

def setBit(num, i):
    '''shifts 1 over by i bits and performs OR'''
    return int(num | (1 << i))

def clearBit(num, i):
    '''shift 1 over by i bits. then negate it and perform AND'''
    mask = ~(1 << i)
    return int(num & mask)

def updateBit(num, i, bitIs1:bool):
    '''shift 1 over by i bits. then negate it and perform AND'''
    value = 1 if bitIs1 else 0
    mask = ~(1 << i)
    return int( num & mask | (value << i) )
