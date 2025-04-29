"""
    Q4.
    Data:

    x (Hours Watched)	y (Marks)
            1	            30
            2	            45
            3	            55
            4	            70
"""

# Importing Libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression

hours_watched = np.array([ [1], [2], [3],[4]])
print(hours_watched)
marks = np.array([30, 45, 55, 70])
print(marks)

Ex = 1+2+3+4
Ey = 30+45+55+70
Exy = 1*30 + 2*45+3*55+4*70
Ex2 = 1**2 + 2**2 + 3**2 + 4**2
n = 4

m = ( n * Exy - (Ex*Ey))/( n * Ex2 - (Ex**2))
print(f"Slope of the line: {m}")

b = (Ey - (m * Ex))/n
print(f"Intercept of the line: {b}")


y = m * 10 + b
print(f"Predicted marks for someone with 10 hours watched: {y}")


# Creating the model
# Train the model using the dataset

model = LinearRegression()
model.fit(hours_watched, marks)
print(model.intercept_)
print(model.predict([[10]])[0])
print(f"Model slope: {model.coef_[0]}")
print(f"Model intercept: {model.intercept_}")
print(f"Predicted marks for someone with 10 hours watched: {model.predict([[10]])[0]}") 








print(model.coef_)  
