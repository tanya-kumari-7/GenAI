"""
🔍 Q1. Student Hours vs Marks

    Hours Studied (x)	Marks Scored (y)
    2	35
    4	55
    6	65
    8	80
    📌 Task:

    Find slope (m) and intercept (b)
    Predict marks for 15 hours of study

"""

# Importing LinearRegression
# from sklearn.linear_model import LinearRegression
# Importing numpy

Hour = np.array([[2], [4], [6], [8]])  # Features (Hours Studied)
Marks = np.array([35, 55, 65, 80])       # Labels (Marks Scored)

Ex = 2+4+6+8
Ey = 35+55+65+80
Exy = 2*35+4*55+6*65+8*80
Ex2 = 2**2+4**2+6**2+8**2
n = 4

m = (n * Exy - (Ex * Ey))/(n * Ex2 - (Ex**2))
b = (Ey - m * Ex)/n

y = m* 15 + b



print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")
print(f"Predicted Marks for 5 hours of study: {y}")

# Prediction using Model

model = LinearRegression()
model.fit(Hour,Marks)

print(f"Model slope: {model.coef_[0]}")
print(f"Model intercept: {model.intercept_}")
print(f"Predicted salary for someone with 2.5 years experience: {model.predict([[15]])[0]}")

