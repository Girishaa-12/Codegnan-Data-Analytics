#Polymorphism : this means "many forms" it allows the same function,method, or operator to behave differently depending on the object
#1.Method overloading 2.method overriding 3.opearator overloading

#1.Method overloading: Method Overloading means having multiple methods with the same name but different numbers or types of parameters.
'''
example - 1
class calc:
    def add(self,a,b,c=0):
        return a+b+c
c=calc()
print(c.add(23,12))'''

'''class calc:
    def add(self,a=0,b=0):
        print(a+b)
n=calc()
n.add(4)
n.add(4,5)'''

'''
example - 2
class calc:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
c=calc()
print(c.add(12,19))
print(c.add(12,19,26))'''

#2.method overriding :this occurs when a child class provide its own implementation of a method already defined in the parent class.
'''class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
n = dog()
n.sound()'''

#3.opearator overloading : Operator Overloading means giving a special meaning to an operator (+, -, *, etc.)to perform different actions for user-defined objects (classes).
'''class stu:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
a_1 = stu(8)
n = stu(45)
print(a_1 + n)

class stu:
    def __init__(self,marks):
        self.marks = marks
    def __sub__(self,other):
        return self.marks - other.marks
a_1 = stu(8)
n = stu(45)
print(a_1 - n)

class stu:
    def __init__(self,marks):
        self.marks = marks
    def __mul__(self,other):
        return self.marks * other.marks
a_1 = stu(8)
n = stu(45)
print(a_1 * n)

#division operator overloading, use __truediv__().

class stu:
    def __init__(self, marks):
        self.marks = marks

    def __truediv__(self, other):
        return self.marks / other.marks

a_1 = stu(45)
n = stu(9)

print(a_1 / n)
note: the operator inside the method will overload a special method or operator given in the call '''

#Data Abstraction:
'''this is the process of hiding the internal implementation details and showing only the essenstial features to the user.
it focus on wat an object does rather than how it does it '''

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimeters(self):
        return 2*(self.a * self.b)
a=Rec(10,5)
print(a.area())
    




    
