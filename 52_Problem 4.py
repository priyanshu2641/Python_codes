def nextpalindrome(n):
    n = n + 1
    while not ispalindrome(n):
        n += 1
    return n
def ispalindrome(n):
    return str(n)==str(n)[::-1]

a=int(input("Enter the number: "))
list=[]
for i in range(a):
    number=int(input("Enter the number: "))
    list.append(number)

print(list)
new_list=[]
for i in list:
    if i>=10:
        n=nextpalindrome(i)
        new_list.append(n)
print(new_list)