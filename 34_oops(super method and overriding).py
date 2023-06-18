class A:
    classvar1 = "I am a class variable in class A."
    def __init__(self):
        self.var1 = "I am inside class A's constructor."                      #instant variable
        # self.classvar1 = "Instance variable in class A."

class B(A):
    classvar2 = "I am in class B."

a = A()
b = B()

print(b.classvar1)

############################################################################################

# Here instataneous variable in also present so it will print instant variable in class and not the class variable.

class A:
    classvar1 = "I am a class variable in class A."                             #class variable

    def __init__(self):
        self.var1 = "I am inside class A's constructor."  # instant variable
        self.classvar1 = "Instance variable in class A."


class B(A):
    classvar2 = "I am in class B."


a = A()
b = B()

print(b.classvar1)

######################################################################################################

# Here class variable in class B is present but it will not print it because instantaneous variable in class B is not present
# but it is present in class A so it will print that.

class A:
    classvar1 = "I am a class variable in class A."                             #class variable

    def __init__(self):
        self.var1 = "I am inside class A's constructor."  # instant variable
        self.classvar1 = "Instance variable in class A."


class B(A):
    classvar1 = "I am in class B."                                            #class variable


a = A()
b = B()

print(b.classvar1)

#######################################################################################################

class A:
    classvar1 = "I am a class variable in class A."  # class variable

    def __init__(self):
        self.var1 = "I am inside class A's constructor."  # instant variable
        # self.classvar1 = "Instance variable in class A."


class B(A):
    classvar1 = "I am in class B."  # class variable


a = A()
b = B()

print(b.classvar1)

#######################         SUPER METHOD            ###################################################

class A:
    classvar1 = "I am a class variable in class A."  # class variable

    def __init__(self):
        self.var1 = "I am inside class A's constructor."  # instant variable
        self.classvar1 = "Instance variable in class A."
        self.special="Special"


class B(A):
    classvar1 = "I am in class B."  # class variable
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor."  # instant variable
        self.classvar1 = "Instance variable in class B."

a = A()
b = B()

print(b.special)

#############################################################################################################

class A:
    classvar1 = "I am a class variable in class A."  # class variable

    def __init__(self):
        self.var1 = "I am inside class A's constructor."  # instant variable
        self.classvar1 = "Instance variable in class A."
        self.special="Special"


class B(A):
    classvar1 = "I am in class B."  # class variable
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor."  # instant variable
        self.classvar1 = "Instance variable in class B."

a = A()
b = B()

print(b.special)
print(b.var1)
print(b.classvar1)

######################################################################################################

class A:
    classvar1 = "I am a class variable in class A."  # class variable

    def __init__(self):
        self.var1 = "I am inside class A's constructor."  # instant variable
        self.classvar1 = "Instance variable in class A."
        self.special="Special"


class B(A):
    classvar1 = "I am in class B."  # class variable
    def __init__(self):
        self.var1 = "I am inside class B's constructor."  # instant variable
        self.classvar1 = "Instance variable in class B."
        super().__init__()

a = A()
b = B()

print(b.special)
print(b.var1)
print(b.classvar1)