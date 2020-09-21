# Modulus.py includes several useful functions when dealing with programs using modular arithmetic
class Modulus():

    @staticmethod
    def mod(num1, num2):
        return num1%num2

    @staticmethod
    def multiplicativeInverse():
        pass

    @staticmethod # Ecuclid
    def gcd(a,b):
        if b>a: a,b = b,a
        rem = a%b
        if rem == 0:
            return b
        else: 
            return Modulus.gcd(b,rem)

    @staticmethod # Using State Machine
    def gcdMachine(a,b,e=1):
        if min(a,b) > 0:
            if a%2==0 and b%2==0: return Modulus.gcdMachine(a/2,b/2,2*e)
            elif a%2==0: return Modulus.gcdMachine(a/2,b,e)
            elif b%2==0: return Modulus.gcdMachine(a,b/2,e)
            elif a>b: return Modulus.gcdMachine(a-b,b,e)
            elif b>a: return Modulus.gcdMachine(a,b-a,e)
            elif a==b: return Modulus.gcdMachine(1,0,e*a)
            else:
                return int(e)
        return int(e) 

# driver code:
if __name__ == "__main__":
    mod = Modulus()
    print(mod.gcdMachine(42,27))