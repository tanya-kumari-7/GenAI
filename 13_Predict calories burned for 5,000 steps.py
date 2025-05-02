"""
🚶 Q7. Steps Walked vs Calories Burned

Steps (in 1000s) (x)	Calories Burned (y)
2	80
4	150
6	210
📌 Task:

Find the regression equation
Predict calories burned for 5,000 steps
"""

Ex = 2 + 4 + 6
Ey = 80 + 150 + 210
Exy = 2 * 80 + 4 * 150 + 6 * 210
Ex2 = 2 **2 + 4 **2 + 6 ** 2 
n = 3

m = (n * Exy - (Ex * Ey))/(n * Ex2 - (Ex ** 2))

b = (Ey - m * Ex)/n 

y = m * 5000 + b