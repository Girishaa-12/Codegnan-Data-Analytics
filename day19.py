#Error Handlings
#1.try block: the try block,test block of code for error
#2.except block: the except block let hand if the code contain error
#3.else block: this will be excuted if the try block has no errors in the code
#4.finally block: this block will be excuted either try block contain error or not 

'''#types of errors
ZeroDivisionError - Division by zero
ValueError - Invalid value
NameError - Variable not defined
TypeError - Wrong data type
IndexError - List index out of range
KeyError - Dictionary key not found
FileNotFoundError - File does not exist'''

'''ZERO DIVISON ERROR
try:
    print(10/0)
except:
    print("This will handle zero division error")'''


'''ValueError
try: 
    n = int(input("enter the number:"))
    print(num)
except:
    print("enter the valid num")'''

'''NameError
try:
    print(hello)
    print(5+"py")
except:
    print("this is an name error")
else:
    print("no error")'''

'''try:
    print(5+"py")
except:
    print("this will handle name error")
else:
    print("no error")'''
'''try:
    print("py" + 3 + hello)
except:
    print("this will be an name error")
else:
    print("no error")'''
'''
try:
    print(a)
except:
    print("this is an type error")
else:
    print("no error")'''

    
'''TypeError
try:
    print(5+"py")
    print(a)
except TypeError:
    print("This will handle TypeError")
except NameError:
    print("This will handle NameError")
else:
    print("No Error")'''

'''VALUE ERROR WITH FINALLY"
try:
    n = int(input("enter a num"))
    print(n)
except ValueError:
    print("this will handle a valuerror")
else:
    print("no error")
finally:
    print("the end")'''

'''INDEX VALUE ERROR
try:
    n = [2,5,6]
    print(n[3])
except:
    print("this will handle a index error")
finally:
    print("this is the end")'''


try:
    a = {"name" : "Girishaa"}
    print(a['age'])
except:
    print("this handle a keyValue error")
else:
    print("no error")
finally:
    print("this is end")

