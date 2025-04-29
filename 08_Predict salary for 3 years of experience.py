"""
💼 Q2. Experience vs Salary

Experience (Years) (x)	Salary (LPA) (y)
            1	3.2
            2	5.1
            4	8.3


Find the regression line
Predict salary for 3 years of experience

"""

Ex = 1+2+4
Ey = 3.2+5.1+8.3
Exy = 1*3.2 + 2*5.1 + 4*8.3
Ex2 = 1**2 + 2**2 + 4**2
n = 3

m = (n * Exy - (Ex * Ey))/(n * Ex2 - (Ex**2))
print("Slope (m):", m)
b = (Ey - m * Ex)/n
print("Intercept (b):", b)

Y = m * 3 +b
print("Predicted Salary for 3 years of experience:", Y)


# prediction Using model
year = np.array([[1], [2], [4]])
salary = np.array([3.2,5.1, 8.3])

model = LinearRegression()
model.fit(year, salary)

predicted_salary = model.predict([[3]])
print("Predicted Salary for 3 years of experience using model:", predicted_salary[0])