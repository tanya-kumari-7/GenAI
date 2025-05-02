"""
📱 Q6. App Usage vs Battery Drain
Usage (Hours) (x)	Battery Drain (%) (y)
1	10
2	20
3	30
5	50
📌 Task:

Find the slope and intercept
Predict battery drain for 4 hours of usage

"""

Ex = 1 + 2 + 3 + 5
Ey = 10 + 20 + 30 + 50
Exy = 1 * 10 + 2 * 20 + 3 * 30 + 5 * 50
Ex2 = 1**2 + 2**2 + 3**2 + 5**2
n = 4

m = ( n * Exy - (Ex * Ey))/( n * Ex2 - (Ex **2))
print("Slope (m):", m)

b = (Ey - m * Ex)/n
print("Intercept (b):", b)

y = m * 4 + b
print("Predicted Battery drain for 4 hours of usage:", y)

# prediction Using model

Hours = np.array([[1], [2], [3], [5]])
BatteryDrain = np.array([10, 20, 30, 50])

model = LinearRegression()
model.fit(Hours, BatteryDrain)

predicted_battery_drain = model.predict([[4]])
print("Predicted Battery drain for 4 hours of usage using model:", predicted_battery_drain[0])