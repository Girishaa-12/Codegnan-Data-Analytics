#--Built-in functions:
'''print()
input()
len()
type()
max()
min()
sort()
example:
m = [1,2,3,6,4]
m.sort()
print(m)'''

#Recursive function:a recursive fun call by itself to solve a problem by breaking it into small or simple subprblms
'''def fac(num):
    if num == 1:
        return 1
    return num *fac(num - 1)
print(fac(5))'''

#return : this ends a function excution and sends a value back to the code that call the function
'''def add(a,b):
    return a + b
res = add(4,5)
print(res)'''

#lambda function:lambda funtion is a small anonamus function
#lambda takes no of arugements but one expression
#syntax:lambda arguments : expression
'''n = lambda a,b,c: a+b+c
print(n(2,4,5))'''
'''m = lambda a,b,c,d : a+b-c*a+d
print(m(3,5,2,6))'''


