#modules: a module in python is a file that contains py code such as
#variables,functions,classes,statements
#two types of modules:user-define,built-in
#user-define
'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b'''

#built-in
'''from math import sqrt
print(sqrt(25))'''

'''import math as m
print(m.factorial(10))
print(m.pow(2,5))'''

#to create file
'''import os
os.mkdir("some_python")'''

#to remove file
'''import os
os.remove("shaa.txt")'''

#to remove the folder
'''import os
os.rmdir("abc")'''

#to check the version
'''import sys
print(sys.version)
print(sys.path)
print(sys.exit)'''

#random
'''import random
print(random.randint(1000,8989)'''
      
#collections
'''from collections import Counter
data = ['a','b','c','d']
counter = Counter(data)
print(counter)'''

from collections import defaultdict
dd = defaultdict(int)
dd['missing'] += 1
print(dd['missing'])
print(dd)
