# how to find if n is prime? 

# naive way
def is_prime_naive(n):
    if n < 2: return False
    for i in range(2, n-1):
        if n % i == 0: return False
    return True

# faster way: sqrt(n)
from math import sqrt
def is_prime(n):
    if n < 2: return False
    root = int(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0: return False
    return True

# the chad way: The Sieve of Eratosthenes
def sieve_of_eratosthenes(max:int):
    # initialize flags to all true except 0 and 1
    flags = [True]*(max+1)
    flags[0] = flags[1] = False

    count = 0 
    prime = 2
    while prime <= sqrt(max):
        # cross off remaining multiples of prime
        cross_off(flags, prime)

        #find next value which is true
        prime = get_next_prime(flags, prime)
        
    return flags

def cross_off(flags:list, prime):
    '''
    cross off remaining multiples of prime. We can start with prime*prime because
    if we have a k*prime, where k < prime, this values would have already been crossed off in a prior iteration
    '''
    for i in range(prime*prime, len(flags), prime):
        flags[i] = False

def get_next_prime(flags, prime):
    next = prime + 1
    while next < len(flags) and not flags[next]:
        next+=1
    return next

if __name__ == "__main__":
    print(sieve_of_eratosthenes(9))