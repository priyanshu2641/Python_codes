a=["Boiled eggs","Burger","Oats","Pizza","Sprouts","Momos"]
# If we want to remove the food items that are not good for our health, then we will have to remove the items at the even places.
i=0
for fooditem in a:
    if i%2==0:
        print(fooditem)
    i=i+1

# We can do this question more faster by using enumerate functions.It takes both index as well as item.
# ***index starts from 0.

for index,fooditem in enumerate(a):
    if index%2==0:
        print(fooditem)
