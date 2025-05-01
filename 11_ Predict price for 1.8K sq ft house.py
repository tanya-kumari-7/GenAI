"""
🏠 Q5. House Size vs Price

    Size (1000s sq ft) (x)	Price (Lakhs) (y)
    1	50
    1.5	65
    2	80
    2.5	95
    📌 Task:

    Find slope and intercept
    Predict price for 1.8K sq ft house
"""

Ex = 1 + 1.5 + 2 + 2.5
Ey = 50 + 65 + 80 + 95
Exy = 1 * 50 + 1.5 * 65 + 2 * 80 + 2.5 * 95
Ex2 = 1 ** 2 + 1.5 ** 2 + 2 ** 2 + 2.5 ** 2
n = 4

m = (n * Exy - (Ex * Ey))/( n * Ex2 - (Ex **2))
print("Slope (m):", m)

b = (Ey - m * Ex)/n
print("Intercept (b):", b)

y = m * 1.8 + b
print("Predicted Price for 1.8K sq ft house:", y)

# prediction Using model
size = np.array([[1], [1.5], [2], [2.5]])
price = np.array([50, 65, 80, 95])

#################################


model = LinearRegression()
model.fit(size, price)
predicted_price = model.predict([[1.8]])    
print("Predicted Price for 1.8K sq ft house using model:", predicted_price[0])

