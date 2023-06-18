def greet(name):
    print("Good Morning"+" "+name)

greet("Priyanshu")

def sum(a,b):
    """This is a docstring. This tells the user about the function. For eg., This functions tells the sum."""
    return a+b
a=int(input("Enter the first Number="))
b=int(input("Enter the second Number="))

c=sum(a,b)
print(sum.__doc__)
print(c)

def average(a,b):
    print("The average of the 2 numbers is ",(a+b)/2)

average(7,9)
