#regular expression or (RegEx)
'''
RegEX is a sequence of characters that form a searching pattern
this can be used to check the string contains a specified search pattern
python has a built in package called "re" which can be used to work with RegEX
'''

#functions in re
'''
Findall
Search()
fullmatch
'''
#findall
'''text = "Python is a high-level programming language renowned for its clean, highly readable syntax"
import re
print(re.findall("a", text))
'''

#Meta Charc
'''
[] - a-z,A-Z,0-9 and any specified squence...
. (dot) - here each dot is one char
^ (cap) - this look for the , string is starting with specified seq or not
$ (dollar) - this look for the , string is ending with specified seq or not
* (star) - Zero or more
? - zero or one
+ - one or more occurence
{} curly braces -
special squence:
\S - no space
\s - only space
\D - non digit
\d - only digits
\W - non words
\w - matchs any word char (letters,digits, underscore)

'''
#[]
#alphabets
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("[a-zA-Z]", text))
'''

#numbers
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("[0-9]", text))
'''

#it find single letters of a l s
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("[als]", text))
'''

# Dot(.):
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("re......", text))
'''

#Cap(^):
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("^Python is", text))
print(re.findall("^is", text))
'''

#dollar($)
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("syntax$", text))
print(re.findall("is$", text))
'''

#star*
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.*ython", text))
print(re.findall("P.*e", text))
'''

#?
'''import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.?ython", text))'''

#+
'''import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.+ython", text))'''

#{}
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("P.{10}", text))
'''

#/S and /s
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("\S", text))
print(re.findall("\s", text))'''

#/D and /d
'''
import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("\D", text))
print(re.findall("\d", text))'''

#/W and /w
'''import re
text = "Python is a high-level programming23 language98 renowned fo8r its clean, highly readable syntax"
print(re.findall("\W", text))
print(re.findall("\w", text))'''

#phone num
import re
mobile = input("Enter 10 digits number: ")
how = re.fullmatch("[6-9][0-9]{9}",mobile)
if how:
    print(f"{mobile} this is an indian number")
else:
    print(f"{mobile} this is not an indian number")




