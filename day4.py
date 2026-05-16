#concatination : the(+) for int and can add but for the other data types it will act as concatinating the data type
a = 90
b = 8
print(a + b)
any_ = "python"
so = " is a lanuguage"
print(any_ + so)
an = [1,2]
am = [3,4]
print(an + am)

#tuple: collection of diff data types, sprtd by commas , represent in () ans its immutable.
#example:int, string, list, tuple inside tuple
#methods :
'''count()- used to used the particular item in the tuple
syntax: variable_name.count(item)
example:'''
a = 23, "python", [1,2], ((3,4))
print(a.count("python"))
'''Index()- used to find the position of the item, and only gives the first occurance
syntax: variable_name.index(item)
example:'''
a = 23, "python", [1,2], ((3,4))
print(a.index("python"))
a = ("python", (1,2), ("this is a python", [7,8], 98))
print(a[2][2])
#Dictionary - Dict is a key : value pair, key and value sprtd by : and pair is sprtd by commas , and represented by curly braces {}
#syntax: dict.keys()
#example:
girisha = {"Name" : "Rollno",
           1 : 2,
           (1, 2) : [3, 4]}
print(girisha)
#keys in dict: used to get all the values from the keys in dict
#syntax: variablename.keys()
girisha = {"Name" : "Girisha",
           "age" : 21,
           "mob" : "12345689",
           "pan" : "G23hji44"
           }
print(girisha.keys())
#values in dict: get all the values in value in dict
#syntax: variablename.value()
girisha = {"Name" : "Girisha",
           "age" : 21,
           "mob" : "12345689",
           "pan" : "G23hji44"
           }
print(girisha.values())
#items()-
"""girisha = {"Name" : "Girisha",
           "age" : 21,
           "mob" : "12345689",
           "pan" : "G23hji44"
           }
print(girisha.items())
print(girisha.["age"])"""
#update - used to add a new key : value pair in the dict
girisha = {"Name" : "Girishaa",
           "age" : 21,
           "mob" : "12345689",
           "pan" : "G23hji44"
           }
girisha.update({"adhar" : "3923456789"})
girisha["name"] = "Thangavalu"
print(girisha)
#clear - used to remove all the items in the dict
girisha = {"Name" : "Girishaa",
           "age" : 21,
           "mob" : "12345689",
           "pan" : "G23hji44"
           }
print(girisha.clear())
