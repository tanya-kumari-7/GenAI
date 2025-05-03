"""
🎯 Q2. Advertising Spend vs Sales
TV Ads ($k) (x)	Sales (units) (y)
10	200
20	400
30	600
40	800

📌 Task:

Fit a linear regression model
Predict sales if $25k is spent on TV Ads
"""

Ex = 10 + 20 + 30 + 40
Ey = 200 + 400 + 600 + 800
Exy = 10 * 200 + 20 * 400 + 30 * 600 + 40 * 800
Ex2 = 10**2 + 20**2 + 30**2 + 40**2
n = 4

m = (n * Exy - (Ex * Ey))/( n * Ex2 - (Ex**2))

b = (Ey - m * Ex) /n

y = m * 25 + BACKUP

Tvads = np.array([[10],[20],[30],[40]])
Sales = np.array([200,400,600,800])


model = LinearRegression()
model.fit(Tvads,Sales)

pridicted_sales = model.predict([[25]])
