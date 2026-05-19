#Type conversions
#int - str,float
'''a = 56
b = str(a)
c = float(a)
print(a)
print(type(b))
print(type(c))'''
#string - int,float,list
'''n = "678"
m = int(n)
k = float(n)
print(n)
print(type(n)
l = list(n)
print(n)
print(k)
print(type(m))
print(type(l))
print(type(k))'''
#float - int,str
'''a = 2.3
b = float(a)
print(b)
print(type(b))
c = str(a)
print(c)
print(type(c))'''
#list - str,tuple
'''a = [1,2,4,3]
b = str(a)
c = tuple(a)
print(c)
print(b)
print(type(c))
print(type(b))'''
#tuple - str,list
'''n = (1,2,3)
print(str(n))
print(list(n))'''
#userinput - int
'''n = int(input("Enter a number: "))
print(45+n)'''
#userinput - str
'''k = input("enter your name:")
print(k)'''
#userinput - list
'''l = list(map(int,input("enter numbers: ").split()))
print(l)'''
#userinput - tuple
'''a = tuple(map(int,input("enter a number: ").split()))
print(a)'''
n = eval(input("Enter a num: "))
print(type(n))


      
