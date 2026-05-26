#---problems using function
#1.odd or even
'''def even(num):
    if num % 2 == 0:
        print(f"{num} is even num")
    else:
        print(f"{num} is odd num")
even(12)
even(13)'''
#2.higgest or lowest
'''def high(a,b):
    if a >= b:
        print("higgest num", a)
        print("lowest num", b)
    else:
        print("higgest num", b)
        print("lowest num", a)
high(a=12,b=26)'''

#3.postive negative num
'''def check(num):
    if num >= 0:
        print("postive num")
    else:
        print("negative num")
check(1234)
'''
#---patterns
#4.star pattern
'''def pattern(n=5):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
pattern()'''
#5.alphabet pattern
'''def pattern(star=5):
    for g in range(1, star + 1):
        for n in range(1, g + 1):
            print(chr(64 + n), end=" ")
        print()
pattern()'''
#6.numbers pattern
'''def pattern(star=9):
    count=0
    for i in range(1,star+1):
        for j in range(i,star+1):
            count+=1
            print(star,end=" ")
        print()
pattern()'''
#7.star in reverse
'''def pattern(star=7):
    count=0
    for i in range(star,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
pattern()'''
#8.alphabet in reverse
'''def pattern(star=10):
    count=0
    for i in range(star,0,-1):
        for j in range(i):
            print(chr(64+j),end=" ")
        print()
pattern()'''
#9.pyramid pattern
'''def pattern(star=8):
    for i in range(1,star+1):
        print(" "*(star-i),end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
pattern()'''
#10.amstrong no
'''def amstrong(num): 
    sum=0
    n=len(str(num))
    for i in str(num):
        sum += int(i)**n
    if sum == num:
        print(f"{num} is an amstrong num")
    else:
        print(f"{num} is not an amstrong num")
amstrong(153)
amstrong(123)'''
#11.perfect num
'''def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum == num:
        print(f"{num} is a perfect num")
    else:
        print(f"{num} is not a perfect num")
perfect(123)
perfect(6)'''
#12.prime num
'''def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(f"{num} is a prime num")
    else:
        print(f"{num} is not prime num")
prime(2)
prime(6)'''
#13.squares
'''def square(num):
    print(num * num)
square(3)'''
#14.table
'''def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
table(2)
table(5)'''
#15.palindrome
'''def palindrome(num):
    empty = ""
    for i in str(num):
        empty = i + empty
        print(empty)
    if empty == str(num):
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not a palindrome")
palindrome(121)
palindrome(123)'''
#16.student marks
'''def grade(stu_marks):
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
        print("Fail")
marks = int(input("Enter the marks: "))
grade(marks)'''
#17.max num
'''def max(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
a = int(input("enter the num: "))
b = int(input("enter the num: "))
c = int(input("enter the num: "))
max(a,b,c)'''
#18.min num
'''def min(a,b,c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    else:
        print(c)
a = int(input("enter the num: "))
b = int(input("enter the num: "))
c = int(input("enter the num: "))
min(a,b,c)'''
#19.cube num
'''def cube(num):
    print(num * num * num)
cube(4)'''
#20.factorial num
def factorial(num):
    sum = 1
    for i in range(1, num + 1):
        sum = sum * i
    print(sum)
factorial(5)
