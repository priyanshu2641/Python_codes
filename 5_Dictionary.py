a={"Priyanshu":"Python","Rohan":"C++","Aayush":"Java","Shashank":"Kotlin"}
print(type(a))
print(a)
print(a["Priyanshu"])

b={"Aayush":"Java","Rohan":"C++","Shashank":"Kotlin","Priyanshu":{"1st year":"Python","2nd year":"C++","3rd year":"DSA"}}
print(b)
print(b["Priyanshu"])
print(b["Priyanshu"]["2nd year"])

# We can include any list or tuple also inside a dictionary.
c={"Priyanshu":"Python","Rohan":"C++","Aayush":"Java","Shashank":"Kotlin","Virat Kohli":[254,183,94,115]}
print(c)
print(c["Virat Kohli"])

print(a.keys())
print(list(a.keys()))
print(a.values())
print(list(a.values()))
print(a.items())
print(list(a.items()))

# There are 2 ways by which we can easily update the Dictionary.**** We can use any integer as our key also.
a["Neeraj"]="C"
print(a)
a.update({"Mayank":"HTML"})
print(a)
d={"Uttam":"Javascript"}
a.update(d)
print(a)

# Ways to delete any item from Dictionary
del a["Uttam"]
print(a)

# Copy
e=a.copy()
print(e)

# get function
print(a.get("Priyanshu"))
print(a.get("Virat Kohli"))  #.get function will print None for the item not present in the Dictionary.


# Question 1
a={"Priyanshu":"Python","Rohan":"C++","Aayush":"Java","Shashank":"Kotlin"}
b=input("Enter the word: ")
print(a[b])

