#   Solving the world famous towers of hanoi problem 

counter = 0
def hanoi(n,start,middle,end):
    global counter
    if n == 1:
        counter += 1  
        print('Move disk from peg',start,'to peg',end)
    else:
        counter += 1
        hanoi(n-1,start,end,middle)
        print('Move disk from peg',start,'to peg',end)
        hanoi(n-1,middle,start,end)
        

if __name__ == "__main__":
    print('================= TOWERS OF HANOI ==================\n')
    hanoi(3,1,2,3)
    print('Number of Steps:',counter)
    counter = 0