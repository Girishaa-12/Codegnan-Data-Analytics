#sets
'''collection of unordered and unique elements
duplicates are not allowed
reprstd by {}
items are not stored in index order'''
'''a = {1,2,2,4,5}
print(a)'''
#methods
#Union()-it will give all the values from the 2 sets together in ones
#syntax - variable_name.union(another var)
"""a = {1,2,2,3}
b = {24,5}
print(a.union(b))
#intersection-common value in the 2 sets
#syntax : variable_name.intersection(another var)
a = {1,2,3,4,5,4}
b = {22,43,22,2,4}
print(a.intersection(b))
#difference - to get the diff value from the set
#syntax: variable_name.difference()
a = {1,2,3,4}
b = {1,3,5}
#print(a-b)
print(a.difference(b))
#symmetric_difference
a = {1,2,3}
b = {1,2,4}
print(a.symmetric_difference(b))
#methods of sets
#add()-add an new element into set
c#synatx: variable_name.add(element)
a = {1,2,2,3,4}
a.add(34)
print(a)
#update() - add multiple items
a = {1,2,34}
a.update([43,54])
print(a)
#sum()
a = {1,2,34}
print(sum(a))"""
#remove
aaa = {1,2,3,4}
aaa.remove(2)
print(aaa)
#min()
b = {1,2,5,8}
print(min(b))
#max
c = {23,65,98}
print(max(c))
#discard
n = {1,2,3,4,5}
n.discard(6)
print(n)
#len
n = {1,2,3,4}
print(len(n))
#pop
m = {48,1,2,3,4}
m.pop()
print(m)

