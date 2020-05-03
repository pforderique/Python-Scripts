# RUNNER CLASS FOR TESTING SEARCHES AND SORTS SCRIPTS

import Searches 

MASTER_LIST = [
    [1,2,3,4,5,6,7,8,9,10], #0:                                     10 sorted first 10 numbers
    [0,1,1,2,3,5,8,13,21,34,55], #1:                                11 sorted fib sequence
    [5,10,15,20,25,30,35,40,45,50,65,70,75,80,85,90,95,100], #2     20 sorted multiples of 5
    [3,6,9,12,15,18,21,24,27,30], #3                                10 sorted multiples of 3

    [10,9,8,7,6,5,4,3,2,1], #4                                      10 BACKsorted first 10 numbers
    [89,76,66,58,41,34,26,11,7,2], #5                               10 BACKsorted random

    [8,12,4,64,100,60,20,28,40,16], #6                              10 UNsorted multiples of 4
    [23,52,66,3,42,63,45,27,43,23,5,57,3,2,3,2], #7                 16 UNsorted random
    [90,4,23,5,2,35,23,52,3,235,23,5,42,4,5,2,32,5,57,34,25,242,435,235,23,52,4,52,3,235,235,2] #8  32 UNsorted random
]

result = Searches.linearSearch(MASTER_LIST[3],12)

print(result)