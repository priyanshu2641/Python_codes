class Student:
    pass

Priyanshu=Student()
Aayush=Student()
Rohan=Student()

Priyanshu.name="Priyanshu"
Aayush.name="Aayush"
Rohan.name="Rohan"
Priyanshu.cgpa=7
Aayush.cgpa=7.1
Rohan.cgpa=7.25
Priyanshu.city="Faridabad"
Aayush.city="Gorakhpur"
Rohan.city="Varanasi"

print(Priyanshu.name)
print(Priyanshu.cgpa)
print(Priyanshu.city)

##################################     INSTANCE AND CLASS VARIABLES     #########################################
class Student:
    Branch="Chemical Engineering"

Priyanshu=Student()
Aayush=Student()
Rohan=Student()

Priyanshu.name="Priyanshu"
Aayush.name="Aayush"
Rohan.name="Rohan"
Rohan.Branch="Mechanical Engineering"              #Instance Variable

print(Priyanshu.name)
print(Priyanshu.Branch)
print(Rohan.Branch)

print(Student.__dict__)

################################  self    #########################################

class Student:
    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")

Priyanshu=Student()
Aayush=Student()
Rohan=Student()

Priyanshu.name="Priyanshu"
Aayush.name="Aayush"
Rohan.name="Rohan"
Priyanshu.cgpa=7
Aayush.cgpa=7.1
Rohan.cgpa=7.25
Priyanshu.city="Faridabad"
Aayush.city="Gorakhpur"
Rohan.city="Varanasi"

Priyanshu.studentrecord()


################################  __init__ function    #########################################
class Student:
    def __init__(self,a,b,c):
        self.name=a
        self.cgpa=b
        self.city=c

    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")

student1=Student("Priyanshu",7,"Faridabad")
student2=Student("Aayush",7.1,"Gorakhpur")
student3=Student("Rohan",7.25,"Varanasi")
student1.studentrecord()
student2.studentrecord()
student3.studentrecord()
