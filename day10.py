#assert: this statement is knw as debbuggin,it is used to test or check whether condition is true,if the condition is not true will get error call
'''num= 10
assert num > 15
print("True")'''
'''num = 1
assert num > 0
print("true")'''
'''age = 16
assert age >=17, "age must be greater than equal to 17"
print("eligible")'''

#FUNCTIONS:
'''1. a function is a block of code which only excute when it is called
2. you can pass data, knwn as parameters into a function
3. we use functions to avoid repeated lines in code

def function_name(parameters): - defination fun
    --------------------
    --------------------
function_name(agruments)
num = 9
def even(num):
    if num % 2 == 0:
        print(f" {num} even")
    else:
        print(f" {num} odd")
even(num)
even(108)'''

#ways to pass arguments:
#1.required agruments: a fun must be called with the same num of agruments
'''exmple:
def even(num):
    if num % 2 == 0:
        print(f" {num} even")
    else:
        print(f" {num} odd")
even(108,99)'''
'''def even(num,num_2,num_3):
    if num % 2 == 0:
        print(f" {num} even")
    else:
        print(f" {num} odd")
even(108,99,111)'''

#2.default arugement
'''by default, values is defined at parameters even tho it will take from aruguments
def even(name = "girisha",age=22,sal=50):
    print(name)
    print(age)
    print(sal)
even("ishaa",21,500)'''
#3.keyword arugments: we can send agruments with key-value
'''syntax: by this,the order of agruments doest not matter
def even(age,sal,name):
    print(name)
    print(age)
    print(sal)
even("ishaa",21,500)'''
#4.variable arugments: adding a star(*) before the parameters name in the function, receive a tuple of arugements and can access items with indexes
'''def even(*name):
    print(name[1])
even("Thangavalu","Girisha","ishaa")'''
#5.passing by value
'''def even(a):
    a = 5
    print(a)
b = 10
even(b)
print(b)'''

#6.passing by refrence
#program add of 2 nums
'''def n(a,b):
    b = a + b
    print(b)
n(10,20)'''
#check even or odd
'''def even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
even(11)'''
#higesht and lowest
'''def abc(a,b):
    if a >= b:
        print("higgest num" , a)
        print("lowest num" , b)
    else:
        print("higgest num" , b)
        print("lowest num" , a)
abc(a=12,b=25)'''
#squares
'''def squares(a):
    print(a * a)
squares(2)'''
#num is postive or neg
def check(num):
    if num >= 0:
        print("postive num")
    else:
        print("negative num")
check(-3)


