"""
 Q1.
    Data:


    x (Hours)	y (Score)
        2	         40
        4	         60
        6	         80

    Find the slope (m) and intercept (c).
    Predict the score if a student studies for 5 hours.
"""
"""
 y = mx + b
"""


# import numpy as np
# from sklearn.linear_model import LinearRegression

Ex = 2+4+6
Ey = 40+60+80
Exy = 2*40 + 4*60 + 6*80
Ex2 = 2**2 + 4**2 + 6**2
n = 3

m = (n * Exy - (Ex * Ey)) / (n * Ex2 - (Ex**2))
b = (Ey - m * Ex) /n

y = m * 5 + b
print(f"slop: {m}")
print(f"intercept: {b}")
print(f"Predicted score for a student who studied for 5 hours: {y}")
