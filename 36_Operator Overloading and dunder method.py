# Search Mapping Operators to Functions
# dunder method: __method__
class Student:
    no_of_credits=34.5
    def __init__(self,a,b,c):
        self.name=a
        self.cgpa=b
        self.city=c

    @classmethod
    def new_no_of_credits(cls, a):
        cls.no_of_credits = a

    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")
        print(f"The number of credits earned by {self.name} is {Student.no_of_credits}")

    def __add__(self, other):
        return self.cgpa + other.cgpa
    def __truediv__(self,other):
        return self.cgpa/other.cgpa

student1=Student("Priyanshu",7,"Faridabad")
student2=Student("Aayush",7.1,"Gorakhpur")
Student.new_no_of_credits(54)
student1.studentrecord()
student2.studentrecord()
print(student1+student2)
print(student1/student2)

#######################################################################################################
# __str__ dunder method is prefered over __repr__ dunder method.
class Student:
    no_of_credits=34.5
    def __init__(self,a,b,c):
        self.name=a
        self.cgpa=b
        self.city=c

    @classmethod
    def new_no_of_credits(cls, a):
        cls.no_of_credits = a

    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")
        print(f"The number of credits earned by {self.name} is {Student.no_of_credits}")

    def __repr__(self):
        return f"Student('{self.name}',{self.cgpa},'{self.city}',{Student.no_of_credits})"
    def __str__(self):
        return f"The name of the Student is {self.name}\nThe cgpa of the {self.name} is {self.cgpa}\nThe city to which {self.name} belongs is {self.city}\nThe number of credits earned by {self.name} is {Student.no_of_credits}"

student1=Student("Priyanshu",7,"Faridabad")
student2=Student("Aayush",7.1,"Gorakhpur")
Student.new_no_of_credits(54)
student1.studentrecord()
student2.studentrecord()
print(student1)

#####################################################################################################################

class Student:
    no_of_credits=34.5
    def __init__(self,a,b,c):
        self.name=a
        self.cgpa=b
        self.city=c

    @classmethod
    def new_no_of_credits(cls, a):
        cls.no_of_credits = a

    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")
        print(f"The number of credits earned by {self.name} is {Student.no_of_credits}")

    def __repr__(self):
        return f"Student('{self.name}',{self.cgpa},'{self.city}',{Student.no_of_credits})"
    def __str__(self):
        return f"The name of the Student is {self.name}\nThe cgpa of the {self.name} is {self.cgpa}\nThe city to which {self.name} belongs is {self.city}\nThe number of credits earned by {self.name} is {Student.no_of_credits}"

student1=Student("Priyanshu",7,"Faridabad")
student2=Student("Aayush",7.1,"Gorakhpur")
Student.new_no_of_credits(54)
student1.studentrecord()
student2.studentrecord()
print(repr(student1))