#OOPS:
#1.class : a class is a blueprint or template used to create object
''' exmpl:
class stu:
    name = "girishaa"
s1 = stu()
print(s1.name)'''
    
#2.object: an object is an instance of a class
''' exmpl:
class stu:
    name = "girishaa"
s1 = stu()
print(s1.name)'''

#3.Attributes:attributes are the variables that belong to a class or an object 
'''class stu:
    name = "girishaa"
    age = 21
s1 = stu()
print(s1.name)
print(s1.age)'''

#methods: this functions define inside the class is called methods, which are in the def keywords is knw  as methods, 
'''class DA_PFS:
    def python(n):
        DA_PFS = "batch_3"
        print("this is DA and PFS batch_03")
    def powerbi(n):
        DA = "batch_03"
        print("this is DA batch_03")
all = DA_PFS()
all.python()
all.powerbi()'''
#methods are python() amd powerbi

#constructor:cons also knw as  __init__ , the const is used to carry the all attributes
#a constructor is a special method that is automatically called when an object is created
'''class ATM:
    def __init__(self,balance,name):
        self.balance = balance
        self.name = name
        
    def bal_check(self):
        print(f"{self.name} your total balance is {self.balance + 700}")
        
    def name_(self):
        print(self.name)
        
card = ATM(balance = 60000,name = "Girishaa")
card.bal_check()'''

#access specifiers: 
#1.public: name - Anywhere
#2.protected: _name - Class and subclasses (by convention)
#3.private: __name - Only inside the class

#public-this can be accessed from anywhere in the pgrm
'''class stu:
    name = "Girisha"
s1 = stu()
print(s1.name)'''

#protected: this is repesented using a single underscore(_)
'''class stu:
    _name = "Girishaa"

s1 = stu()
print(s1._name)'''
    
#public:this is represented using a doublr underscore(__)
'''class stu:
    __name = "Girishaa"
s1 = stu()
print(s1._stu__name)'''

#encapsulation:
'''Encapsulation is the process of binding data (variables) and methods (functions) into a single unit (class) and restricting direct access to data to
protect it from accidental modification.
Encapsulation = Data Hiding + Controlled Access'''
class bank:
    def __init__(self,balance):
        self.__balance = balance

    def depo(self,amnt):
        self.__balance += amnt
    def get_bal(self):
        return self.__balance
acc = bank(1000)
acc.depo(50000)
print(acc.get_bal())
    
    
