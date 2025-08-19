# ===================================================================
''' STEP:-1 Imports
    STEP:-2 Prepare the Data
    STEP:-3 Feature Engineering : creating, transforming, Encoding categorical variables,or selecting the variables (features)
    STEP:-4 Do Exploratory Data Analysis
    STEP:-5 Train-Test Split
    STEP:-6 Choose & Train Models
    STEP:-7 Evaluate Performance
    STEP:-8 Deploy for Real-time Predictions 
'''
# ===================================================================

import pandas as pd
# from datetime import datetime 
# import lightgbm as lgb
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report, roc_auc_score
# from sklearn.preprocessing import LabelEncoder

# ===================================================================
'''
About My learning Till Here:
This will be under supervised learning, as we are going to provide it with labeled data so it 
can learn patterns and then make predictions for new datasets.
'''
# ===================================================================

# Load your dataset
data = pd.read_csv(r"C:\Users\Admin\Downloads\MF_churn_Working_data.csv") 

# Explore the Data
data.shape
data.head(5)
data.tail(5)
data.info()
data.describe()
data.sample(5)
data.describe(include='object')
data.columns
data.dtypes
data.select_dtypes(include='object').columns
data.select_dtypes(include='float64').columns
data.isnull().sum()
data.isnull().mean()*100
data[data.isnull().any(axis=1)]
data.nunique()
data['occupation'].unique()
data.duplicated().sum()
# data.drop_duplicates(inplace=True)
data['occupation'].value_counts()
data['occupation'].value_counts(normalize=True) * 100
data['Age'].min()
data['Age'].max() 
data['Age'].mean()
data['Age'].median()
data['Age'].std()

# ===================================================================
# ===================================================================
