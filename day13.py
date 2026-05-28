#List comprehension: it offers a shortest syntax when we want to create a new list from existing list
#syntax: vari_name = [expression loop condition]
'''old = [1,2,3,4,5]
new = [so for so in old if so % 2 == 0]
print(new)
'''
'''old = [1,2,3,4,5,32,45,76,87,88]
new = [so if so % 2 != 0  else "even" for so in old]
print(new)
'''
#generators:(lazy evolution)
'''genearators in python are special tpe of itterable, allows users to itterate over the data efficientl without storing everything the memory.
they generate the values lazil using ield keyword'''

#we use generators for:
'''1.generators doesnt store entire dataset in the memory,they generate values on the fly or run time.
#we should store in memory otherwise it will boosted
#2.avoiding the unnecessar storage of data speed up execution'''

#how it works:
'''it looks like nrml function but uses the yield keyword insted of return
when the function is called it doesnt excute immdiately,instead it return a generator object which can be iterated using loop or the next() function''' 

'''def simple_gen():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))'''

#by using functions
'''def square(num):
    res = []
    for i in range(1, num + 1):
        res.append(i*i)
    return res
print(square(5))'''

#by using gen
'''def any (num):
    for i in range(num):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))'''

#
n = "Python is considered one of the easiest programming languages for beginners because its syntax is simple and easy to understand"
a = ' '
for j in n:
    if j not in "AEIOUaeiou":
        a += j
print(a)


