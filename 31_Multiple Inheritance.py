class Student:
    var=10
    def __init__(self, a, b, c):
        self.name = a
        self.cgpa = b
        self.city = c

    def studentrecord(self):
        print(f"The name of the Student is {self.name}")
        print(f"The cgpa of the {self.name} is {self.cgpa}")
        print(f"The city to which {self.name} belongs is {self.city}")

student1 = Student("Priyanshu", 7, "Faridabad")
student2 = Student("Rohan",7.25,"Varanasi")
student1.studentrecord()

class Programmer:
    var=9
    salary="300k"
    interests="Cosmology"
    def __init__(self,a,b):
        self.name=a
        self.language=b

    def programmerdetails(self):
        print(f"The name of the Programmer is {self.name}")
        print(f"The languages used by the Programmer are {self.language}")

programmer1=Programmer("Priyanshu",["Phython","Js","C++"])
programmer1.programmerdetails()

class Player(Student,Programmer):       # Order Matters
    # var=8
    sport=["Cricket"]
    def playerdetails(self):
        print(f"{self.name} likes to play {self.sport}")

player1=Player("Priyanshu",7,"Faridabad")
player1.studentrecord()
player1.playerdetails()
print(player1.var)
print(player1.salary)
print(player1.interests)