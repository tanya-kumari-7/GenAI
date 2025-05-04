"""
🎯 Q3. Hours of Sleep vs Productivity
Sleep (Hours)	Productivity Score
4	50
5	55
6	65
7	75

📌 Task:

Calculate the regression line
Predict productivity for 6.5 hours of sleep

"""

Ex = 4 + 5 + 6 + 7
Ey = 50 + 55 + 65 + 75
Exy = 4*50 + 5*55 + 6*65 + 7*75
Ex2 = 4**2 + 5**2 + 6**2 + 7**2
n = 4

m = (n * Exy - (Ex * Ey))/(n * Ex2 - (Ex **2))
b = (Ey - m * Ex)/n
y = m * 6.5 + b 

print("Slope (m):", m)
print("Intercept (b):", b)
print("Predicted productivity for 6.5 hours of sleep:", y)  

# predicting using model

sleephour = np.array([[4],[5],[6],[7]])
productivityScore = np.array([50,55,65,75])


model = LinearRegression()
model.fit(sleephour,productivityScore)

predicted_sleephour = model.predict([[6.5]])

print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_[0])
print("Predicted productivity for 6.5 hours of sleep using model:", predicted_sleephour[0])