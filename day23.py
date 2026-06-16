#-----------------DATA ANALYSIS-----------------------
'''
this is the process of inspecting,cleaning,transforming and modeling data to discover useful insights.....

#Types of DA:

1.Descriptive Analysis : Descriptive analysis is the process of examining historical data to summarize and understand what has happened in the past.
2.Diagnostic Analysis : Diagnostic analysis is the process of investigating data to determine the causes or reasons behind past events and outcomes.
3.Predictive Analysis : Predictive analysis is the process of using historical data, statistical techniques, and machine learning models to forecast future events or trends.
4.Presscriptive Analysis : Prescriptive analysis is the process of recommending the best course of action by analyzing data, predicting outcomes, and evaluating possible decisions.

#One-Line Definitions:
    
Descriptive Analysis: Explains what happened.
Diagnostic Analysis: Explains why it happened.
Predictive Analysis: Predicts what is likely to happen.
Prescriptive Analysis: Suggests what should be done.

#Why Data Analysis? (Short Points)

Improves decision-making
Identifies trends and patterns
Solves problems effectively
Predicts future outcomes
Increases efficiency
Reduces risks
Supports business growth
Helps achieve goals faster

#NumPy (Numerical Python):
this py library for numerical computing it provides support for mutli-dimenisonal arrays, and linear algebra operations, makng it essential for data analysis

#using numpy in DA
improve perfromance
simplifies complex operations
easy data manuplation
'''
#one dimenisonal
'''
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1)
'''
#two dimen
'''
import numpy as np
arr_1 = np.array([[4,5,6,7],[1,2,3,4]])
print(arr_1)
'''
#three dimen
'''
import numpy as np
arr_1 = np.array([[4,5,6,7],[1,5,7,3],[1,2,3,4]])
print(arr_1)
'''
#array shape
'''
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshaped(3,2)
print(reshaped)
'''
'''
import numpy as np
arr_1 = np.array([10,20,30,40,50])
print(arr_1)
print(arr_1 + 5)
print(arr_1 - 2)
'''
'''
import numpy as np
arr_1 = np.array([[10,20],[50,60]])  
arr_2 = np.array([[1,2],[4,5]])        
print(np.dot(arr_1, arr_2))
'''

#shallow copy
'''
import numpy as np
arr_1 = np.array([10,20,30])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)
'''
#deep copy
'''
import numpy as np
arr_1 = np.array([10,20,30])
copy_dee = arr_1.copy
arr_1[1] = 200
print(copy_dee)
print(arr_1)
'''

#pandas :
'''the pandas is a poerful data manipulation and analysis libary
where it provides data structure like series and datframes for efficient data handling
#methods for seires
mean()
sum()
min()
max()
apply()
map()
'''
'''
import pandas as pd
any = pd.Series([2999,15999,52999,4999,1999],
                index = ["Earbuds","Smartphone","Laptop","Watch","Footware"])
print(any)'''

#Dataframe
import pandas as pd
data = {
    "product": ["Earbuds", "Smartphone", "Laptop", "Watch", "Footware"],
    "Brand": ["Noise", "Oneplus", "Hp", "Bolt", "Nike"],
    "Price": [1500, 20000, 60000, 2000, 5000],
    "stock": [50, 25, 30, 56, 89]
}

dip = pd.DataFrame(data)
print(dip)


