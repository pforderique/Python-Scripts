##################################################
##  Problem 2.4 TubeYou
##################################################

PRIME = 2 ** 31 - 1

def copyright_match(T, S):
    """
    Input: T | an ASCII string 
    Input: S | an ASCII string where |S| < |T|
    
    Return `True` if S appears inside the transcript T and `False` otherwise.
    """

    # Calculate R(S)
    R_S = R(S)
    # Calculate first hash R(T_0) = ord(c)
    R_T = R(T[:len(S)])
    # see if hash values are equal first!!
    if R_T == R_S:
        if T[:len(S)] == S: return True

    # store first character
    c1 = T[0]
    # store f prime
    fprime = 128**len(S) % PRIME# get_f(S)

    # print("R(S) =", R_S)
    # print("R(T0) =", R_T)
    
    # if not, lets iterate through every substring !
    for idx in range(1, len(T) - len(S) + 1):
        # if idx == 16:
        #     print("WORD:", T[idx : idx + len(S)])

        # get the last char in this word, which is 
        c2 = T[idx + len(S) - 1]
        # calculate HASH OF T[idx : idx + len(S)] by using prev value
        R_T = ( (128*R_T)%PRIME - (ord(c1)%PRIME)*fprime + ord(c2) ) % PRIME
        # update "previous" first char
        c1 = T[idx]

        # debugging
        # print(f"R(T{idx}) =", R_T)

        # IF we get a match NOW CHECK if the string actually is the string and not false match
        if R_T == R_S:
            if T[idx : idx + len(S)] == S: return True

    return False

############ SINCE WE CAN'T STORE 128^n, but we CAN STORE 128^n mod p

# return 128^S mod p
def get_f(S):
    res = 1
    multiplier = 1
    times = 1
    while times <= len(S):
        res = (128*res)%PRIME
        times += 1
    return res

def R(string):
    res = 0
    multiplier = 1
    for i in range(len(string) - 1, -1, -1):
        res += multiplier*(ord(string[i])) % PRIME
        multiplier = (multiplier * 128) % PRIME
    return res % PRIME

# T = "Are you cheating on this code submission?"
# S = "u cheat"
# T = "Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark"
# S = "shark"
# T = "Who ever said money can't solve your problems, Must not have had enough money to solve 'em"
# S = "Who"
#### FAILING THIS ONE TEST CASE :((
# T = "sdiovsensriobnskbnseurnflvsuenvlijriodznvbfkurzks"
# S = "bnseurnflvsu"

# if __name__ == "__main__":
#     print(copyright_match(T, S))
#     # print()
#     # print(R("sdiovsensrio"))
#     # print(R("diovsensriob"))
#     # print("a")