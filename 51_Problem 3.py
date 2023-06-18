print("Restaurant= Xero Degrees")
a=[2000,2300,1000,2500,3000,3400,3150,3800,2800]
a.sort()
print(a)
a.reverse()
print(a)


a=[2000,2300,1000,2500,3000,3400,3150,3800,2800]
a.sort()
print(a)
print(a[::-1])



a=[2000,2300,1000,2500,3000,3400,3150,3800,2800]
a.sort()
print(a)
for i in range(len(a)):
    a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
    print(f"The reverse list is {a}")
    break

