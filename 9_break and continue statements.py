i=1
while(i<=20):
    print(i , end=" ")
    if i==12:
        break
    i=i+1

i=1
while(i<40):
    if i<8:
        i = i + 1
        continue
    print(i)
    if i==19:
        break
    i=i+1

# Question
while(True):
    a = int(input("Enter the Number: "))
    if a<=100:
        continue
    if a>100:
        print("You have entered ",a)
        break

n=18
print("No. of guesses=9")
i=1
while(True):
    a=int(input("Enter your guess: "))
    if i>=9:
        print("No. of guesses left= 0")
        print("Limit exceeded. Game Over.")
        break
    else:
        if a>25:
            print("You have chosen a number that is greater.")
            print("No.of guesses left=",9-i)
            i=i+1
            continue
        elif a<10:
            print("You have chosen a number that is lesser.")
            print("No.of guesses left=", 9 - i)
            i=i+1
            continue
        elif a == 18:
            print("Correct answer!")
            print("No. of guesses you took to finish=", i)
            break
        elif a>18:
            print("You are close. Choose a number that is lesser.")
            print("No.of guesses left=", 9 - i)
            i=i+1
            continue
        elif a>10:
            print("You are close. Choose a number that is Greater.")
            print("No.of guesses left=", 9 - i)
            i = i + 1
            continue

