#Project based on RegExp
'''
Validation
1.Mobile Number - 10 digits init
2.password - cap,small,digit,special,char,atleast 8
3.Mail - @gmail.com
'''
import re
name = input("Enter the Name: ")
if re.fullmatch(r"[A-Za-z ]+",name):
    print("Valid Name")
else:
    print("Invalid Name")

mobile = input("Enter the Mobile Number: ")
if re.fullmatch(r"^[6-9][0-9]{9}",mobile):
    print("Number is Valid")
else:
    print("Number is Invalid")
password = input("Enter the Password: ")
if re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$",password):
    print("Password is strong")
else:
    print("Password is weak")
mail = input("Enter the Mail:")
if re.fullmatch(r"^[a-zA-Z0-9._%+-]+@gmail\.com$",mail):
    print("Mail is Valid")
else:
    print("Mail is Invalid")





    

