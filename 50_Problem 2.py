a=int(input("Enter the number of apples:"))
b=int(input("Max numbers of Students:"))
c=int(input("Min numbers of Students:"))

if b==c:
    print("This is not a Range.")
    if a%b==0:
        print(f"{b} is a divisor of {a}")
    else:
        print(f"{b} is not a divisor of {a}")

else:
    for i in range(c,b+1):
        if a%i==0:
            print(f"{i} is a divisor of {a}")
        else:
            print(f"{i} is not a divisor of {a}")