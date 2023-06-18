# Syntax=(normal,*args,**kwargs)
# WE CAN EASILY ADD OR DELETE ANY ELEMENT USING KWARGS AND ARGS.

def func1(Intro,*args):        #We can replace args with any other argument also.
    print(Intro)
    for students in args:
        print(students)

a=["Saahil","Sanchit","Shantanu","Aditya","Uday"]
b="Following are the best dancers of IIT Delhi: "
func1(b,*a)

def func1(Intro,*args,**kwargs):        #We can replace args and kwargs with any other argument also.
    print(Intro)
    for students in args:
        print(students)
    for name,cgpa in kwargs.items():
        print(f"CGPA of {name} is {cgpa}.")

a=["Saahil","Sanchit","Shantanu","Aditya","Uday"]
b="Following are the best dancers of IIT Delhi: "
c={"Saahil":"8.5","Sanchit":"8.2","Shantanu":"8.8","Aditya":"8.4","Uday":"8.0"}

func1(b,*a,**c)
