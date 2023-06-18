"""
Iterable- __iter__() or __getitem__()
Iterator- __next__()
Iterator
"""

def gen(n):
    for i in range(n):
        yield i                               #generates but not print(saves RAM)

a=gen(12345678901234567890)
print(a)

#####################################################################################################
def gen(n):
    for i in range(n):
        yield i                               #generates but not print(saves RAM)

a=gen(5)

# print(a.__next__() )
# print(a.__next__() )
# print(a.__next__() )
# print(a.__next__() )
# print(a.__next__() )
# print(a.__next__() )

for i in a:
    print(i)

#################################################################################################################
a="Priyanshu"
ier=iter(a)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())