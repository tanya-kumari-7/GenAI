"""
🎯 Q8. Study Time vs Test Score

Time (Hours) (x)	Score (%) (y)
1.5	45
2.5	55
3.5	65
4.5	75
📌 Task:

Calculate m and b

Predict test score for 3 hours of study
"""

Ex = 1.5 + 2.5 + 3.5 +4.5
Ey = 45 + 55 + 65 + 75
Exy = 1.5 * 45 + 2.5 * 55 + 3.5 * 65 + 4.5 * 75
Ex2 = 1.5 **2 + 2.5 **2 + 3.5 **2 + 4.5 **2
n = 4

m = ( n * Exy - (Ex * Ey))/(n * Ex2 - (Ex **2))
print("Slope (m):", m)

b = ( Ey - m * Ex)/n
print("Intercept (b):", b)
y = m * 3 + b
print("Predicted test score for 3 hours of study:", y)

# prediction Using model

hours = np.array([[1.5], [2.5], [3.5], [4.5]])
score = np.array([45, 55, 65, 75])

model = LinearRegression()
model.fit(hours, score)
predicted_score = model.predict([[3]])
print("Predicted test score for 3 hours of study using model:", predicted_score[0])