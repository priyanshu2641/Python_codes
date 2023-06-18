# an empty a={} is not a set but a empty dictionary

a={1,2,3,4,4,4,5,5,6,6,7,8,5}
print(a)                        # a set will only take unique values.
print(type(a))

syntax=set()                #syntax
set_from_list= set([1, 2, 3, 4, 5, 5, 5, 6, 7, 8])         #set can be made from the list
print(set_from_list)

# adding elements to a set.*We can't add any list or dictionary to a set as they are mutable but we can add tulep to set.
a.add(9)
a.add(10)
a.add((1,2,3,4))
print(a)

# length of a set
print(len(a))

# removing any random material from the set
# a.pop()
# print(a)

# clearing the whole set
# a.clear()
# print(a)

# removing any elememt from the set
# a.remove(7)
# print(a)

# union and intersection
d={2,4,6,8,10,12,14,16,18}
union=a.union(d)
print(union)

intersection=a.intersection(d)
print(intersection)

print(max(d))
print(min(d))

print(a.isdisjoint(d))

