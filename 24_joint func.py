a=["Virat Kohli","KL Rahul","Suryakumar Yadav","Shikhar Dhawan","Ravi Ashwin","Ravindra Jadeja"]
print("Indian Cricket Heros:")
for players in a:
    print(players,"and", end=" ")
print("others.")

# Another better method is using Joint function
b= " and ".join(a)
print(b,end=" ")
print("and others.")