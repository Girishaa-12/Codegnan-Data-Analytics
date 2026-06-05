#inheritance :
'''this allows one class to aquire properties and methods of another class
types :
1. single inheritance - father -> child
2. multiple  - father and mother = child
3. multi - level
4. hierachical
5. hybrid inheritance'''
#single inheritance: a class inherts from a sinhle parent class (father = son)
'''class father:
    def land(self):
        print("i am father, i have 8A")
class girishaa(father):
    def own(self):
        print("i have 4A")
n = girishaa()
n.land()'''

'''class person:
    def name(self):
        print("my name is girishaa")
class student(person):
    def marks(self):
        print("i score 95%")
s=student()
s.name()
s.marks()'''

#multiple inheritance:a child class containing more than one parent class (father,mother = son)
'''class father:
    def land(self):
        print("my father has 5A")
class mother:
    def gold(self):
        print("my mother has 4KG gold")
class daughter(father,mother):
    def mine(self):
        print("i have ntg")
s = daughter()
s.land()
s.gold()'''

'''class Animal:
    def dog(self):
        print("It barks")

class Bird:
    def parrot(self):
        print("It eats guava")

class Water(Animal, Bird):
    def whale(self):
        print("It swims in water")

d = Water()
d.dog()
d.parrot()
d.whale()'''

#multi - level : a class inherits from a parent class and another class inherts from that child class
'''class grandfather:
    def land(self):
        print("grandfather has 6A")
class father(grandfather):
    def flat(self):
        print("father has flat in vizag")
class daughter(father):
    def car(self):
        print("i has a car")
s = daughter()
s.land()
s.flat()
s.car()'''

#hierarchical : a multiple childeren inherits from a single parent 
'''class father:
    def land(n):
        print("my father has 10A land")
class Girisha(father):
    def mine(n):
        print("job")
class nitish(father):
    def bro(n):
        print("jobless")

niti = nitish()
niti.land()

sha = Girisha()
sha.land()'''

#hybrid : this is the combination of two or more typs of inheritance

'''class A:
    def some(self):
        print("class A")
class B(A):
    def any(self):
        print("class B")
class C(A):
    def sha(self):
        print("class C")
class D(B,C):
    def ha(self):
        print("class D")
n = D()
n.sha()'''

#super method (): is used to access methods and constructor of the parent class from the child class
'''class parent:
    def display(self):
        print("method parent")
class child(parent):
    def display(self):
        super().display()
        print("method child")
s = child()
s.display()'''

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, rollno):
        super().__init__(name)
        self.rollno = rollno

    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")

s = Student("Girishaa", 112)
s.show()
        
        
        
