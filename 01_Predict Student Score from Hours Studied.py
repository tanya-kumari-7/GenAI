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
