#Operators
#Arithmetic - +, -, *, %, /, //, **
print(2*3)
print(4%5 == 0)
print(10**2)
print(10/2)
print(35.20//5)
#Assignment operator - =, +=,-=,>=,=<,%=,*=
count = 0
for j in range(1,10):
    count +=1
print(count)
#Comparision - ==, !=, >=, <=, < ,>
a = [1,2]
b = [1,2]
c = a
print(type(a))
print(id(a))
print(id(b))
print(id(c))
print(a == b)
print(a is not b)
#Logical
#and - both conditions should be true
#Example:
a = 5
if a % 3 == 0 and a % 5 == 0:
    print(a)
#or - any of one condition should be true    
a = 5
if a % 3 == 0 or a % 5 == 0:
    print("true")
#Membership
#in - the value should be in the list
#not in - if the value is not i the list   
a = 7
b = [1,3,5,7]
print(a in b)
 #not in
a = 7
b = [1,3,5]
print(a is not b)
#Strings- sequence of characters that are inclosed in '',"",''''''
a = "python@34"
b = " @7,."
print(a)
print(b)
#Methods
#replace()
a = "python is a high level programming language"
print(a.replace("python", "Java"))
#Split()
a = "python is a language"
print(a.split())
#len()- len of the char
a = "python"
print(len(a))
#slicing()- :
a = "python is a language"
print(a[3:11])
#indexing
a = "python is a langugage"
print(a[3:9])

