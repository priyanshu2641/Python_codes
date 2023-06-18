presentyear=2021
a=(input("Enter your age or year of Birth: "))
if len(a)>3:
    if int(a) > 2025:
        print("Invalid Year of Birth Entered.")
    else:
        print("Your Year of Birth is",a)

    print("The year in which you will turn 100 years old is",int(a)+100)

    b = int(input("Enter the year in which you wish to find your age:"))
    print(f"Your age in the Year {b} will be",b-a)

elif len(a)<=3:
    if int(a)>150:
        print("You could be the Oldest man alive.")
    else:
        print("Your age is ",a)
        print("Hence your year of birth is",2021-int(a))

    print("The year in which you will turn 100 years old is", 2021-int(a) + 100)

    b = int(input("Enter the year in which you wish to find your age:"))
    print(f"Your age in the Year {b} will be",b-(2021-int(a)))

