Priyanshu_dob= 26
a=int(input("Enter Ram's D.O.B: "))

if Priyanshu_dob>a:
    print("sorry bro")
elif Priyanshu_dob==a:
    print("Same dob")
else:
    print("Fuck off!")

a=[26,4,2001,5,11,1988]
print(2001 in a)
print(12 not in a)
if 2001 in a:
    print("List contains 2001.")
if 12 not in a:
    print("List does not contains 12.")
# Question
a=int(input("Enter your age: "))
if a>100:
    print("Enter a legal age.")
elif a<7:
    print("Enter a legal age.")
elif a>18:
    print("Yes")
elif a<18:
    print("Grow up")
else:
    print("Come to office to get verified.")


# Exercise
a=int(input("Enter the first No.:"))
b=int(input("Enter the second No.:"))
c=(input("Enter the Operator:"))

if a==45 and b==3 and c=='*' :
    print("555")

elif a ==56 and b==9 and c=='+':
    print("77")

elif a == 56 and b==6 and c=='/':
    print("4")

elif c=='+':
    print(a+b)

elif c=='-':
    print(a-b)

elif c=='*':
    print(a*b)
else:
    print(a/b)

