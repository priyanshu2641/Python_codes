# Class Method
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

student1=Student("Priyanshu",7,"Faridabad")
student2=Student("Aayush",7.1,"Gorakhpur")
student3=Student("Rohan",7.25,"Varanasi")
Student.new_no_of_credits(54)
student1.studentrecord()
student2.studentrecord()
student3.studentrecord()

# Class Methods as Alternative Constructor
class Student:
    no_of_credits=34.5
    def __init__(self,a,b,c):
        self.name=a
        self.cgpa=b
        self.city=c

    @classmethod
    def new_no_of_credits(cls, a):
        cls.no_of_credits = a

    @classmethod
    def func(cls,string):
        a=string.split("_")             #returns as list
        print(a)
        return cls(a[0],a[1],a[2])

    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")
        print(f"The number of credits earned by {self.name} is {Student.no_of_credits}")

student1=Student("Priyanshu",7,"Faridabad")
student2=Student("Aayush",7.1,"Gorakhpur")
student3=Student("Rohan",7.25,"Varanasi")
student4=Student.func("Neeraj_7.3_Jind")
print(student4.cgpa)
Student.new_no_of_credits(54)
print(student4.no_of_credits)
student1.studentrecord()
student2.studentrecord()
student3.studentrecord()