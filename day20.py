#File Handling
'''File handler is an object of file to maintain several functions of file like,creating,reading, updating and deleting the file
we have two ways to open the file
1.open() - we have to close the file
2.with open() - here no need to close the file'''

#modes
'''
'r' - is used to read the file, error if file doesn't exit
'a' - is used to add the text into file at last index, if file dosent exit 
'w' - is used to add the text into the file but it will overrde of all txt inside file. if the file doesnt exit it will create with that name
write - is used for append(a) and  w
'x' - used to create the file..,bu it through error if we are using 'r' mode to  create
'''

#open():
'''
name = open("filename","mode") 
----------------------------
----------------------------
-----------------------------
name.close()'''
#open() - example
'''
n = open("sha.txt","r")
print(n.read())
n.close()'''

n = open("sha.txt","w")
print(w.write())
n.close()

'''n = open("sha.txt","a")
print(n.write("girisha"))
n.close()'''

#with open()

'''with open("sha.txt", "r") as n:
    print(n.read(2))
n.close()'''

#methods
#write() -
'''with open("sha.txt", "w") as n:
    print(n.write())
n.close()'''

#read() - this method can read entire file chunk by chunk
'''with open("sha.txt", "r") as n:
    print(n.read(2))
n.close()'''

#readline() - can read one line at a tym
'''with open("sha.txt", "r") as n:
    print(n.readline())
n.close()'''

#readlines() - this method can read entire lines  or an entire file at a tym 
'''with open("sha.txt", "r") as n:
    print(n.readlines())
n.close()'''

#to delete the file
import os
os.remove("b.txt")

