#matploitb:-this is a lib in py for data visualization allowing user to create a variety  places
'''
grid() → Shows grid lines.
title() → Adds chart title.
figure() → Creates a figure.
axes() → Creates axes area.
axis() → Controls axis limits.
legend() → Shows labels for data.
'''
#bar graph sales grpah
'''
import matplotlib.pyplot as plt
sales = ["A","B","C"]
values = [25,40,56]
plt.bar(sales,values,color = "red",edgecolor = "black")
plt.xlabel("car models")
plt.ylabel("values")
plt.title("BMW sales")
plt.show()
'''
'''
import matplotlib.pyplot as plt
year = [2020,2021,2022,2023,2024]
sales = [120,90,400,350,200]
plt.bar(year,sales,color = "red",edgecolor = "black")
plt.title("Audi")
plt.xlabel("Years")
plt.ylabel("sales")
plt.show()
'''
#line plot graph
'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,70,30,40,50]
plt.plot(x,y,color = "pink")
plt.title("line plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
'''
#pie - cmpnys - sales - %
'''
import matplotlib.pyplot as plt
subj = ["Python","D.A","JAVA"]
students = [35,11,6]
plt.pie(students,labels = subj,autopct = "%1.1f%%")
plt.legend(subj)
plt.title("students in courses")
plt.show()
'''
import matplotlib.pyplot as plt
company = ["kitkat","perk","much","dairymilk","fivestar"]
sales = [38000,25000,50000,76000,45000]
plt.pie(sales,labels = company,autopct = "%1.1f%%")
plt.legend(company)
plt.title("Chocolate Company Sales")
plt.show()
#scatter
'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
 y = [10,15,20,25,19]
plt.scatter(x,y,color = "red")
plt.title("scatter plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
'''
#histogram
'''
import matplotlib.pyplot as plt
y = [10,13,18,25,13]
plt.hist(y)
plt.title("histogram plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
'''
