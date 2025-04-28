"""
    Data:


    x (Days)	y (Apples Sold)
        1	            15
        2	            25
        3	            35
        4	            50

    Find the slope and intercept.
    Predict apples sold on Day 5.


"""
# import numpy as np
# from sklearn.linear_model import LinearRegression

Ex = 1 + 2 + 3 + 4
Ey = 15 + 25 + 35 + 50
Exy = 1*15 + 2*25 + 3*35 + 4*50
Ex2 = 1**2 + 2**2 + 3**2 + 4**2
n = 4

m = (n * Exy - (Ex * Ey)) /(n * Ex2 -  (Ex**2))
b = (Ey - m * Ex) / n

y = m * 5 + b
print(f"slop: {m}")
print(f"intercept: {b}")
print(f"Predicted apples sold on Day 5: {y}")

# # Creating the model
# # Train the model using the dataset

model = LinearRegression()
model.fit([[1], [2], [3], [4]], [15, 25, 35, 50])
print(f"Model slope: {model.coef_[0]}")
print(f"Model intercept: {model.intercept_}")   
print(f"Predicted apples sold on Day 5: {model.predict([[5]])[0]}")