# Tuples are inmutable i.e. we can not change their values.
# For making a tuple of one element, add a Coma(,)
a=(26,)
print(a)

a=(26,4,2001,5,11,1988,254,183,94,2001)
print(a)

# Tuple Methods
print(a.count(2001))    #It gives the no. of times that 2001 has appeared in the Tuple
print(len(a))           #It gives the length of the Tuple
print(a.index(183))     #It gives the Index number of the element specified

a=26
b=5
print(a, b)
a, b = b, a
print(a,b)
temp=a
a=b
b=temp
print(a,b)

