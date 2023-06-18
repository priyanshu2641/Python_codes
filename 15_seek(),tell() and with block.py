a=open("Priyanshu.txt")
print(a.tell())          #this tells us the no. from which the line starts.
print(a.readline())
print(a.tell())
print(a.readline())
print(a.tell())
print(a.readline())
print(a.tell())
print(a.readline())
a.close()

a=open("Priyanshu.txt")
print(a.tell())
print(a.readline())
a.seek(36)
print(a.readline())
a.close()

with open("Priyanshu.txt") as a:
# The above syntax is simply equivaent to writing- {a=open("Priyanshu.txt")
#                                                   a.close()}
    data=a.read()
    print(data)