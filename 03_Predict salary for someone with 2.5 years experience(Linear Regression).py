"""
    Q3.
    Data:

    x (Experience Years)	y (Salary in LPA)
            1	                    4
            2	                    5.5
            3	                    7


    Find the equation of line.
    Predict salary for someone with 2.5 years experience.

"""

# import numpy as np
# from sklearn.linear_model import LinearRegression

# Creating the dataset

experience_years = np.array([[1], [2], [3]])
print(experience_years)
salary = np.array([4, 5.5, 7])
print(salary)

Ex  = 1+2+3
Ey = 4+5.5+7
Exy = 1*4 + 2*5.5+3*7
Ex2 = 1**2 + 2**2 + 3**2
n = 3

m = (n * Exy - Ex * Ey) /(n * Ex2 -(Ex**2))
print(f"Slope of the line: {m}")

b = ( Ey - (m * Ex))/n
print(f"Intercept of the line: {b}")

y = m * 2.5 + b
print(f"Predicted salary for someone with 2.5 years experience: {y}")


# Creating the model
# Train the model using the dataset

model = LinearRegression()
model.fit(experience_years, salary)
print(f"Model slope: {model.coef_[0]}")
print(f"Model intercept: {model.intercept_}")
print(f"Predicted salary for someone with 2.5 years experience: {model.predict([[2.5]])[0]}")