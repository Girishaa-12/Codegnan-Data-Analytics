#finaci pgrm
'''n = 0
n2 = 1
def finaci(n,n2):
    limit = int(input("enter the number:"))
    print(n,n2,end=" ")
    for i in range(1,limit):
        n3 = n + n2
        n = n2
        n2 = n3
        print(n3, end= " ")
finaci(n,n2)'''
'''n = [2,5,7,9,2,7]
a = []
def remove(n,a):
    for i in n:
        if i not in a:
            a.append(i)
    print(a)
remove(n,a)'''

n = "Learning Python step by step with examples and practice makes programming easier and more interesting for beginners"
count = 0
def words(n,count):
    for j in n.split():
        count += 1
    print(count)
words(n,count)
    
