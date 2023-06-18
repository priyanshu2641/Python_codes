# We use this in the cases like for eg.- if a given code takes a lot of time to execute and even if we enter an incorrect
# value, then also it will run the code and our time will be wasted. To reduce this problem, we use "raise".

a=input("Enter your name: ")

if a.isnumeric():
    raise Exception("Please enter in an alphabetical form.")

print(f"Hello {a}")

a=int(input("Enter the Numerator: "))
b=int(input("Enter the Denominator: "))

if int(b)==0:
    raise ZeroDivisionError("b is 0 so it could not be run.")
else:
    print(a/b)

##############################################################################################################

a=input("Enter your name: ")
try:
    print(c)

except Exception as e:
    if a=="Priyanshu":
        raise ValueError("Priyanshu is blocked and he is not allowed.")
