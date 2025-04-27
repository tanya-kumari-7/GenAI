""" 
    🧠 Task: Predict Student Score from Hours Studied
    🎯 Goal: Predict how much a student will score in an exam based on how many hours they studied.
"""



import numpy as np
# Importing the required libraries
from sklearn.linear_model import LinearRegression
import numpy as np

# Creating the dataset
''' The dataset consists of hours studied and the corresponding scores obtained by the students in an exam.
    The dataset is represented as a 2D array for hours and a 1D array for scores.
    The hours array is a 2D array with shape (6, 1) and the scores array is a 1D array with shape (6,).
    The hours array contains the number of hours studied by the students and the scores array contains the corresponding scores obtained by the students.
    The dataset is as follows:
    Hours studied: 1, 2, 3, 4, 5, 6
    Scores obtained: 30, 50, 65, 70, 75, 85 '''


hours = np.array([[1], [2], [3], [4], [5], [6]])
print(hours)
scores = np.array([30, 50, 65, 70, 75, 85])
print(scores)

# Creating the model
# Train the model using the dataset
""" The LinearRegression class is used to create a linear regression model.
    The fit method is used to train the model using the dataset.
    The model is trained using the hours array as the input and the scores array as the output. """

model = LinearRegression()
model.fit(hours, scores)

# Making predictions : Predicting the score for a student who studied for 3.5 hours
""" 
    The predict method is used to make predictions using the trained model.
    The input to the predict method is the number of hours studied by the student.
    The output of the predict method is the predicted score for the student. 
"""

predicted_score = model.predict(np.array([[3]]))
print(f"Predicted score for a student who studied for 3 hours: {predicted_score[0]}")

# Manual calculation of the predicted score

"""
    y = mx + b

    where 
    y is the predicted score, (The depending variable)
    m is the slope of the line, (relationship between x and y , if x incrersed how much y will increase)
    x is the number of hours studied, (The independent variable)
    b is the y-intercept.(intercept of the line with y axis)

"""
 
# The slope of the line is calculated using the formula:
#          m = (n * Σ(xy) - Σx * Σy) / (n * Σ(x^2) - (Σx)^2)

"""
    ∑x = 1 + 2 + 3 = 6
    ∑y = 30 + 50 + 65 = 145
    ∑xy = 1*30 + 2*50 + 3*65 = 30 + 100 + 195 = 325
    ∑x^2 = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
    n = 6 (number of data points)

"""

Ex = 1 + 2 + 3 + 4 + 5 + 6 
Ey = 30 + 50 + 65 + 70 + 75 + 85
Exy = 1*30 + 2*50 + 3*65 + 4*70 + 5*75 + 6*85
Ex2 = 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2
n = 6

m_slop = (n * Exy - (Ex * Ey)) / (n * Ex2 - (Ex**2))
print(f"Slope of the line: {m_slop}")

Intercept = (Ey - m_slop * Ex)/ n
print(f"Intercept of the line: {Intercept}")


y = m_slop * 3 + Intercept
print(f"Predicted score for a student who studied for 3 hours: {y}")