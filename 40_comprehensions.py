a=[]
for i in range(100):
    if i%4==0:
        a.append(i)

print(a)

#comprehensions method
a=[i for i in range(100) if i%4==0]
print(a)

# DICTIONARY
a={i:f"Enter name{i}" for i in range(1,100) if i%4==0}
print(a)
a={f"Enter name{i}":i for i in range(1,100) if i%4==0}
print(a)

#Set
a={i for i in (2,3,4,5,2,4,5,6,7,8,6,5,6,7)}
print(a)

#Generators
a=(i for i in range(100) if i%5==0)
print(a)


a=(i for i in range(100) if i%5==0)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


a=(i for i in range(100) if i%5==0)
for i in a:
    print(i)