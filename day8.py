#elif:
#marks
'''stu_marks = int(input("Enter the marks: "))
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
    print("A")
elif stu_marks >= 70:
    print("B")
elif stu_marks >= 60:
    print("C")
elif stu_marks >= 50:
    print("D")
elif stu_marks >= 35:
    print("pass")
else:
    print("Fail")'''
#max 3 num
'''a = int(input("enter the num: "))
b = int(input("enter the num: "))
c = int(input("enter the num: "))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)'''
#Nested IF :nested if when we want to check a condition inside another condition
'''Second condition should run only if first condition is true.
Problems have multiple levels of checking.'''
'''SBI = {"ATM PIN" : "2020"}
pin = input("Enter four digits of ATM Pin:")
if len(pin) == 4:
    if pin in SBI['ATM Pin']:
        print("welcome to sbi atm")
    else:
        print("invalid pin")
else:
    print("pls enter 4 digit pin")'''
#For statement - used to iterate over a squence  
#exmpl:tuple,int,list
'''a = "python"
an = [1,2,3,4]
am = (1,2,3,4)
for j in a:
    print(j)'''
#range()- is a in-built function used to generate numbers in sequence manner
#syntax: range(start,end,step)
#else in for- onces the itteration cmpltd this else will be excuted
#break,pass,continue
'''for i in range(1,100):
    print(i)
else:
    print("code end here")'''
#break - used to exit it from the loop based on the condition
'''for i in range(1,10):
    print(i)
    if i == 5:
        break'''
#continue - used to skip current itteration based on the condition
'''for i in range(1,10):
    if i == 3:
        continue
    print(i)'''
#pass - pass is a space holder
'''for i in range(1,10):
     if i == 3:
         pass'''
#>>While -is the combination of for and if
i = 1
while i <= 5:
    print(i)
    i += 1
