class Student:
    def __init__(self, a, b, c):
        self.name = a
        self.cgpa = b
        self.city = c

    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")

class Programmer(Student):
    def __init__(self,a,b,c,d):
        self.name=a
        self.cgpa=b
        self.city=c
        self.language=d
    def programmerdetails(self):
        print(f"The name of the Programmer is {self.name}")
        print(f"The Programmer scored a cgpa of {self.cgpa}")
        print(f"The Programmer lives in {self.city}")
        print(f"The Languages used by {self.name} is {self.language}")

student1 = Student("Priyanshu", 7, "Faridabad")
student2 = Student("Aayush", 7.1, "Gorakhpur")
student3 = Student("Rohan", 7.25, "Varanasi")
programmer1=Programmer("Neeraj",7.3,"Jind",["Python","C++","C"])
student1.studentrecord()
programmer1.programmerdetails()                   #this is an attribute of Programmer class only.
programmer1.studentrecord()                       #this is an attribute of Student class.


#############################################################################################################










