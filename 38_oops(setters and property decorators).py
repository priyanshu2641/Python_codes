class Employee:
    def __init__(self,a,b):
        self.firstname=a
        self.lastname=b

    def intro(self):
        print(f"The name of the Employee is {self.firstname} {self.lastname}")

    def email(self):
        return f"The email of {self.firstname} {self.lastname} is {self.firstname}{self.lastname}2001@gmail.com"

PC= Employee("Priyanshu", "Chand")
print(PC.email())                    # we use () parenthesis if we are calling a function.

PC.firstname="Rahul"
print(PC.email())

##############################################################################################################

class Employee:
    def __init__(self,a,b):
        self.firstname=a
        self.lastname=b

    def intro(self):
        print(f"The name of the Employee is {self.firstname} {self.lastname}")
    # To access this function directly as an attribute, we use @property decorator
    @property
    def email(self):
        return f"The email of {self.firstname} {self.lastname} is {self.firstname}{self.lastname}2001@gmail.com"

PC= Employee("Priyanshu", "Chand")
print(PC.email)                    # we use () parenthesis if we are calling a function.

PC.firstname="Rahul"
print(PC.email)

#############################################################################################################

class Employee:
    def __init__(self,a,b):
        self.firstname=a
        self.lastname=b

    def intro(self):
        print(f"The name of the Employee is {self.firstname} {self.lastname}")
    # To access this function directly as an attribute, we use @property decorator
    @property
    def email(self):
        return f"The email of {self.firstname} {self.lastname} is {self.firstname}{self.lastname}2001@gmail.com"

    @email.setter
    def email(self,string):
        a=string.split("@")[0]                            #this split function splits the string in list
        self.firstname=a.split(".")[0]
        self.lastname=a.split(".")[1]

PC= Employee("Priyanshu", "Chand")
print(PC.email)                    # we use () parenthesis if we are calling a function.

PC.firstname="Rahul"
print(PC.email)

PC.email="Priyanshu.kalra@gmail.com"
print(PC.lastname)

################################################################################################################
class Employee:
    def __init__(self,a,b):
        self.firstname=a
        self.lastname=b

    def intro(self):
        print(f"The name of the Employee is {self.firstname} {self.lastname}")
    # To access this function directly as an attribute, we use @property decorator
    @property
    def email(self):
        if self.firstname==None and self.lastname==None:
            return "Email not set."
        return f"The email of {self.firstname} {self.lastname} is {self.firstname}{self.lastname}2001@gmail.com"

    @email.setter
    def email(self,string):
        a=string.split("@")[0]                            #this split function splits the string in list
        self.firstname=a.split(".")[0]
        self.lastname=a.split(".")[1]

    @email.deleter
    def email(self):
        self.firstname=None
        self.lastname=None

PC= Employee("Priyanshu", "Chand")

del PC.email
print(PC.email)

##########################################################################################################

import inspect
print(inspect.getmembers(PC))