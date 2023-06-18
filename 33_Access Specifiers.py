# Public
# Protected
# Private
class Student:
    name="Priyanshu"                         #public
    _branch="Chemical Engineering"       #_protected- can be accessed by base class as well as classes derived from it.
    __cgpa=7                                #__public= can be accessed by base class as well as classes derived from it.


class Teacher(Student):
    name="Arghya Baneerjee"

a=Student()
b=Teacher()

print(a.name)
print(a._branch)
print(a._Student__cgpa)

print(b.name)
print(b._branch)
print(b._Student__cgpa)
