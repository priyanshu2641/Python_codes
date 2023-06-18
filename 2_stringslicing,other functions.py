a="priyanshu is a Coder."
print(len(a))
print(a[4])   #the count starts from 0
print(a[0:8])            #It will count from 0 to 7 as the last entry is non included.
print(a[1:16:2])         #It will leave one space after each and every alphabet used.
print(a[::-1])           #It simply reverses the string.
print(a[-15:-1])         #Reverse slicing

print(a.endswith("Coder."))
print(a.endswith("Programmer."))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.count("i"))
print(a.count("priyanshu"))
print(a.replace("Coder","Programmer"))