###############################     MAP      ##################################
a=["26","4","2001","5","11","1988"]
# Method 1
for numbers in range(len(a)):
    a[numbers]=int(a[numbers])
add=a[3]+7
print(add)
# Method 2(We use MAP function)
b=list(map(int,a))                           #SYNTAX= list(map(func,nameoflist))
add=a[3]+7
print(add)


a=["26","4","2001","5","11","1988"]
def square(a):
    return a*a
c=list(map(int,a))
print(c)
b=list(map(square,c))
print(b)

# using lamba function
d=list(map(lambda a:a*a,c))
print(d)


def cube(a):
    return a*a*a
d=list(map(cube,c))
print(d)


def square(a):
    return a*a
def cube(a):
    return a*a*a
p=[square,cube]
for i in range(1,6):
    a=list(map(lambda x:x(i),p))
    print(a)


#####################################      FILTER       #####################################
a=[26,4,2001,5,11,1988]
def numbersgreaterthan11(num):
    return num>11
b=list(filter(numbersgreaterthan11,a))
print(b)


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
def divisibleby3(a):
    return a%3==0
a=list(filter(divisibleby3,a))
print(a)

#########################################       REDUCE      ####################################

a=[2,3,4,5,6,7,9,8]
# Method 1
sum=0
for numbers in a:
    sum=sum + numbers
print(sum)

# Method 2
from functools import reduce

def sum(b,c):
    return b+c
a=reduce(sum,a)
print(a)