import random
random_number=random.randint(0,10)
print(random_number)
rand=random.random()                           #prints any number between 0 and 1
print(rand)

a=["Aayush","Neeraj","Priyanshu","Rohan","Shashank"]
choice=random.choice(a)
print(choice)

import math
a=math.sqrt(70)
print(a)
a=math.sin(70)
print(a)
a=math.cos(70)
print(a)
a=math.tan(70)
print(a)
a=math.degrees(70)
print(a)



# Exercise- Snake, Water, Gun Game
Player_point=0
Computer_point=0
i=1
while(i<=5):
    import random
    a=["SCISSOR","PAPER","STONE"]
    choice=random.choice(a)
    Player=input("Enter your choice(either SCISSOR,PAPER OR STONE): ")
    print(choice)
    if Player== "PAPER" and choice=="STONE":
        print("You Won the round", i)
        Player_point=Player_point+1
    elif Player == "PAPER" and choice == "PAPER":
        print("This round is tied.", i)
        Player_point = Player_point + 0
    elif Player == "PAPER" and choice == "SCISSOR":
        print("You Lost the round", i)
        Computer_point = Computer_point + 1
    if Player == "STONE" and choice == "SCISSOR":
        print("You Won the round", i)
        Player_point = Player_point + 1
    elif Player == "STONE" and choice == "STONE":
        print("This round is tied.", i)
        Player_point = Player_point + 0
    elif Player == "STONE" and choice == "PAPER":
        print("You Lost the round", i)
        Computer_point = Computer_point + 1
    if Player == "SCISSOR" and choice == "PAPER":
        print("You Won the round", i)
        Player_point = Player_point + 1
    elif Player == "SCISSOR" and choice == "SCISSOR":
        print("This round is tied.", i)
        Player_point = Player_point + 0
    elif Player == "SCISSOR" and choice == "STONE":
        print("You Lost the round", i)
        Computer_point = Computer_point + 1

    i=i+1
print("Your Total Score=", Player_point)
if Player_point>Computer_point:
    print("You Won")
elif Player_point==Computer_point:
    print("Game is tied")
else:
    print("You lost. FUCK OFF!")



