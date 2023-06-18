#########################      static method      ####################################
class Student:

    @staticmethod
    def greeting(Student):
        print("Good Morning" + Student)
Priyanshu=Student()

Priyanshu.name="Priyanshu"
Priyanshu.cgpa=7
Priyanshu.city="Faridabad"


print(Priyanshu.name)
print(Priyanshu.cgpa)
print(Priyanshu.city)

Priyanshu.greeting(" Priyanshu")