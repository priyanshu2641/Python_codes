# If we want to force anything, we use this abstractmethod. For example, in the question given below, we are forcing the frint printarea function.

from abc import ABCMeta, abstractmethod
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    sides=4
    def __init__(self,a,b):
        self.length=a
        self.breadth=b

    def printarea(self):
        return self.length * self.breadth

rectangle1=Rectangle(5,10)
print(rectangle1.printarea())