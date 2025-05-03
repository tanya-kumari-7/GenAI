"""
🎯 Q4. Temperature vs Ice Cream Sales
Temperature (°C)	Sales ($)
20	200
22	240
25	300
30	400

📌 Task:

Calculate m and b
Predict sales at 27°C


"""

Ex = 20 + 22 + 25 + 30 
Ey = 200 + 240 + 300 + 400
Exy =  20*200 + 22*240 + 25*300 +30*400
Ex2 = 20**2 + 22**2 + 25**2 + 30**2
n = 4

m = (n * Exy - (Ex * Ey))/( n * Ex2 - (Ex**2))
b = ( Ey - m * Ex)/n
y = m * 27 +BACKUP


temp = np.array([[20],[22],[25],[30]])
sales = np.array([200,240,300,400])

model = LinearRegression()
model.fit(temp,sales)

predicted_sales = model.predict([[27]])