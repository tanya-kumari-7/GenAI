"""

📊 Q3. Ad Spend vs Sales
Ad Spend (Lakhs) (x)	Sales (Lakhs) (y)
        5	45
        10	80
        15	120
        20	150
📌 Task:

Find m, b
Predict sales if ₹12 Lakhs is spent on ads

"""

Ex = 5+10+15+20
Ey = 45+80+120+150
Exy = 5*45 + 10*80 + 15*120 + 20*150
Ex2 = 5**2 + 10**2 + 15**2 + 20**2
n = 4

m = ( n * Exy - (Ex * Ey))/(n * Ex2 - (Ex **2) )
print("Slope (m):", m)

b = (Ey - m * Ex)/n
print("Intercept (b):", b)

y = m * 12 + b
print("Predicted Sales if ₹12 Lakhs is spent on ads:", y)


# prediction Using model

Spend = np.array([[5], [10], [15], [20]])
sales = np.array([45, 80, 120, 150])


model = LinearRegression()
model.fit(Spend, sales)
predicted_sales = model.predict([[12]])
print("Predicted Sales if ₹12 Lakhs is spent on ads using model:", predicted_sales[0])