# Importing LinearRegression
from sklearn.linear_model import LinearRegression

# Importing numpy
import numpy as np

# Creating a simple dataset
X = np.array([[1], [2], [3], [4], [5]])  # Features
y = np.array([2, 4, 6, 8, 10])           # Labels (targets)

# Creating the model
model = LinearRegression()

# Training the model
model.fit(X, y)

# Predicting a new value
prediction = model.predict(np.array([[6]]))
print(f"Prediction for 6: {prediction[0]}")
