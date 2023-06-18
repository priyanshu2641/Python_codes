a=["Priyanshu","Aayush","Rohan","Shashank","Neeraj"]
for items in a:                     #the loop runs for the number of times equal to number of items
    print(items)

lang=[["Priyanshu","Python"],["Aayush","Java"],["Rohan","C++"],["Shashank","Javascript"],["Neeraj","HTML"]]
for names,language in lang:
    print(names,"Uses",language)

lang = {"Priyanshu":"Python", "Aayush":"Java", "Rohan":"C++", "Shashank":"Javascript", "Neeraj":"HTML"}
for names, language in lang.items():       #For dictionary use .items() function
    print(names, "Uses", language)

# Quiz
a=["Priyanshu","Virat","Sanchit",4,5,6,7,8,9,10]
for items in a:
    if str(items).isnumeric() and items>6:
        print(items)

# While loop
i=1
while(i<15):
    print(i)
    i=i+1

i=0
while(i<5):
    print("Priyanshu")
    i=i+1

a=["Albert Einstien","Stephan Hawking","Galileo Galieli","Issac newton","Richard Fenymann"]
i=0
while(i<len(a)-3):
    print(a[i])
    i=i+1