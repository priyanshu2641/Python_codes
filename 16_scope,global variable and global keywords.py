#global variable and local Variables
a=10                        #Global Variable
def N(name):
    a=5                     #Local Variable
    print(a)
    print(name)

N("Priyanshu")
print(a)

a=10                        #Global Variable
def N(name):
    print(a)
    print(name)

N("Priyanshu")
print(a)

# Global Keyword
a=10                        #Global Variable
def N(name):
    global a                #global function changes the value of global variable.
    a=20
    print(a)
    print(name)

N("Priyanshu")
print(a)

