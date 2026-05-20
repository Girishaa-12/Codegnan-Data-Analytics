#>>Statements
#condition statements - if,nested if, elif
#>if- 
'''num = 8
if num % 2 == 0:
    #print(num,"is a even number") 
    print(f"{num} is a even number")'''

#else - else in the if statement, incase the condition becomes false then it will enter into flow-back(else),it will execute whatever inside it
#even or odd
'''n = int(input("enter the num: "))
if n % 2 != 0:
    print(f"{n} is an odd num")
else:
    print(f"{n} is an even num")'''
#vote 
'''age = int(input("Enter your age:"))
if age >= 18:
    print("you are eligible to vote")
else:
    #print("you are not eligible to vote")
    print(f"{age} you are eligible to vote after {18-age} years" )'''
#leap year
'''year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is an leap year")
else:
    print(f"{year} is not an leap year")'''
#vowel
'''vowel = "a"
if vowel in "AEIOUaeiou":
    print(f"{vowel} is an vowel")
else:
    print(f"{vowel} is not an vowel")'''
#postive and negative
'''num = -5
if num >= 0:
    print(f"{num} is a postive num")
else:
    print(f"{num} is a negative num")'''
#pass or fail
'''student_name = input("enter the name: ")
marks = int(input("enter the marks: "))
if marks >= 35:
            print(f" {student_name} {marks} pass")
else:
    print(f"{student_name} {marks} fail")'''
#divisible by 3 and 5
num = 15
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")
#traffic
n = int(input("enter \n1.Red \n2.Green: "))
if n == 1:
    print(f"{n} stop")
else:
    print(f"{n} Go")

            
            
            
            
            



