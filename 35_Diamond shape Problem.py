class A:
    def diamond(self):
        print("This is a method from class A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

a=A()
b=B()
c=C()
d=D()

d.diamond()

##############################################################################

class A:
    def diamond(self):
        print("This is a method from class A")

class B(A):
    def diamond(self):
        print("This is a method from class B")

class C(A):
    def diamond(self):
        print("This is a method from class C")

class D(B,C):
    pass

a=A()
b=B()
c=C()
d=D()

d.diamond()

######################################################################################################
class A:
    def diamond(self):
        print("This is a method from class A")

class B(A):
    def diamond(self):
        print("This is a method from class B")

class C(A):
    def diamond(self):
        print("This is a method from class C")

class D(C,B):
    pass

a=A()
b=B()
c=C()
d=D()

d.diamond()

#######################################################################################################

class A:
    def diamond(self):
        print("This is a method from class A")

class B(A):
    def diamond(self):
        print("This is a method from class B")

class C(A):
    def diamond(self):
        print("This is a method from class C")

class D(B,C):
    def diamond(self):
        print("This is a method from class D")


a=A()
b=B()
c=C()
d=D()

d.diamond()
