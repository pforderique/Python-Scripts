#####USING PARENT METHODS ON CHILDREN
# let jelly = Cat('bob')
# print(jelly) will print cat:bob //because it overrides the animal __str__ method
# print(Animal.__str__(jelly)) will print animal:bob

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")
class B(A):
    def __init__(self):
        # A.__init__(self)
        # self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")
class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")
class D(B, C):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# obj = D()
# obj.y()
me = B()
print(me.a)
