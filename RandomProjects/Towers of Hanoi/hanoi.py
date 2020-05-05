#   Solving the world famous towers of hanoi problem 

counter = 0
def hanoi(n,start,middle,end):
    global counter
    counter += 1 
    if n == 1: 
        print('Move disk from peg',start,'to peg',end)
    else:
        hanoi(n-1,start,end,middle)
        print('Move disk from peg',start,'to peg',end)
        hanoi(n-1,middle,start,end)
        

if __name__ == "__main__":
    print('================= TOWERS OF HANOI ==================\n')
    hanoi(7,1,2,3)
    print('Number of Steps:',counter)