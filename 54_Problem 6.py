a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=[]
i=a
while (i<b+1):
    c.append(i)                                           #Or
    i=i+1                                                 #use random.randit(a,b)
print(c)

import random
number=random.choice(c)

i=1
while(i<1000000000):
    choice=int(input("Player1-Guess the number: "))
    print(choice)
    if(choice==number):
        print("You have entered the correct number.")
        print("Number of chance you took is", i)
        break
    elif(choice<a):
        print("Invalid Choice.")
    elif (choice>b):
        print("Invalid Choice.")
    elif (choice>number and choice<=b):
        print("Choose a lesser number.")
    elif (choice<number and choice>=a):
        print("Choose a greater number.")

    i=i+1


import random
number=random.choice(c)

j=1
while(i<1000000000):
    choice=int(input("Player2-Guess the number: "))
    print(choice)
    if(choice==number):
        print("You have entered the correct number.")
        print("Number of chance you took is", j)
        break
    elif(choice<a):
        print("Invalid Choice.")
    elif (choice>b):
        print("Invalid Choice.")
    elif (choice>number and choice<=b):
        print("Choose a lesser number.")
    elif (choice<number and choice>=a):
        print("Choose a greater number.")

    j=j+1

if i==j:
    print("Tied!")
elif i>j:
    print("Player 2 won!")
elif i<j:
    print("Player 1 won!")



