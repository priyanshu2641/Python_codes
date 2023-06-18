# The else statement is implemented when the the for loop end or the item that we want in not in a list.
Students=["Priyanshu","Aayush","Rohan","Shashank","Neeraj","Uttam"]
for i in Students:
    print(i)

else:
    print("These students are from Chemical Engineering Branch.")

# Break statement is used here which simply means that for loop is not implemented fully.
Students=["Priyanshu","Aayush","Rohan","Shashank","Neeraj","Uttam"]
for i in Students:
    print(i)
    break
else:
    print("These students are from Chemical Engineering Branch.")

############################################################################################################

Students=["Priyanshu","Aayush","Rohan","Shashank","Neeraj","Uttam"]
for i in Students:
    if i=="Armaan":
        break

else:
    print("This student is not from Chemical Engineering Branch.")