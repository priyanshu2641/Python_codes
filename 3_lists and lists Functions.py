interests = ["Cricket", "Cosmology", "Astrophysics", "Sneakers", 26, 4, 2001]
print(interests)
print(interests[0])
print(interests[4])

interests.reverse()   #reverses the list components
print(interests)

a= [26,4,2001,5,11,1988]

print(len(a))         #print the length of the list
print(max(a))         #prints the element with the highest value
print(min(a))         #prints the element with the lowest value

a.append(254)           #adds the numbers to the list
a.append(183)           #adds the numbers to the list
print(a)
a.pop()               #removes the last element from the list
print(a)

a.insert(3,94)       #it will add the specified number to the given Index
print(a)
a.remove(94)         #removes the Element
print(a)

a.sort()              #list elements are arranged in the ascending order
print(a)

# list slicing
print(a[0:5])        #elements with index numbers from 0 to 4 are printed
print(a[2:5])        #elements with index numbers from 2 to 4 are printed
print(a[:5:2])       #one element is left
print(a[::-1])       #reverse slicing but a shortcut to reverse the list

