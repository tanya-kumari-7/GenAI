"""
    Sleep Hours (x)	Productivity Score (y)
    4	60
    6	70
    8	90
    📌 Task:

    Find the equation of line
    Predict productivity for 7 hours of sleep

"""

Ex = 4 + 6 + 8
Ey = 60 + 70 + 90
Exy = 4 * 60 + 6 * 70 + 8 * 90
Ex2 = 4 ** 2 + 6 ** 2 + 8 ** 2
n = 3

m = (n * Exy - (Ex * Ey))/(n * Ex2 - (Ex **2))
print("Slope (m):", m)

b = (Ey - m * Ex)/n
print("Intercept (b):", b)

y = m*7 + b
print("Predicted Productivity for 7 hours of sleep:", y)


# prediction Using model

hour = np.array([[4], [6], [8]])
score = np.array([60, 70, 90])

model = LinerRegression()
model.fit(hour,score)
predicted_score = model.predict([[7]])
print("Predicted Productivity for 7 hours of sleep using model:", predicted_score[0])