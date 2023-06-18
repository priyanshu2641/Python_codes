#
def name():
    print("My name is Priyanshu.")
intro=name
intro()
# Interest function will run even after deleting hobby Function
def hobby():
    print("I like Coding.")
interest=hobby
del hobby
interest()

#   ****We can return a function through a function also.
def function(func):
    func("This is Pycharm.")

function(print)


#         #############    Decorators      ###############
def decorator(func):
    def lines():
        print("Start Executing.")
        func()
        print("Execution Completed.")
    return lines

def college():
    print("IIT Ropar")

college=decorator(college)
college()





