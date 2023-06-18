# Factorial calculation using iterative method
def factorial_iterative(n):
    fac=1
    for i in range(1,n+1):
        fac = fac*(i)
    return fac

number=int(input("Enter the Number: "))
a=factorial_iterative(number)
print(a)

def factorial_recursive(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return (n*factorial_recursive(n-1))
a=int(input("Enter the number: "))
b=factorial_recursive(a)
print(b)


def fibbonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)
a=fibbonacci(8)
print(a)