#Program to convert 24hrs clock into nrml clock
"""time_ = input("enter 24 hours time:")
parts_ = time_.split(":")
hour_ = int(parts_[0])
min_ = int(parts_[1])
print(f"{time_} is converted into {hour_ -12} : {min_} pm") """
#list- list is a collection of diff datatypes, its represtend in [] and sprtd by commas , - mutable
"""a = [1, "python", [1,2]]
print(a)
a = [1, "python", [1,2,[34, "this is python 3rd class", 78], "python is a language",89],34,[3,4]]
print(a[2][4][2])
"""
#methods in list
#append() - this method is used to add new items into list, and it will in the last index position
#syntax - variable_name.append(item)
a = [1,2,3]
a.append(6)
print(a)
a.append([20,90])
print(a)

#immutable - could not able to modify on that particular variable
#ex: int, string
#muttable - can able to modify on that particular variable
#ex: list

so = "python is a"
print(so.replace("python", "java"))
print(so)
a = [1,2,3]
print(a.append(6))
print(a)
#extend - this method is used to add itterable into list, and it will be in the last index position, each value or substring in each index in the list
#syntax : variable_name.extend(iterrables)

a = [1,2,3]
a.extend("python")
print(a)
a = [1,2,3]
a.extend(["python"])
print(a)

#pop()- used to remove the items from the list but will mention here index postion in the pop method
#syntax: variable_name.pop(index postion)
any = [1,2,3]
any.pop(1)
print(any)

#remove - used the remove the item from the list, but will mention here direct in the remove method
#syntax: variable_name.delete(direct value)
any = [1,2,3,4]
any.remove(4)
print(any)
a = ["python",50,"java"]
a.remove("python")
print(a)
