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
import matplotlib.pyplot as plt
import seaborn as sns


# ===================================================================
'''
About My learning Till Here:
This will be under supervised learning, as we are going to provide it with labeled data so it 
can learn patterns and then make predictions for new datasets.
'''
# ===================================================================

# Load your dataset
data = pd.read_csv(r"C:\Users\Admin\Downloads\MF_churn_Working_data.csv") 

# Remove display limits
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)


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
data.select_dtypes(include='float64').columns
data.isnull().sum()
data.isnull().mean()*100
data[data.isnull().any(axis=1)]
data.nunique()
data['occupation'].unique()
data.duplicated().sum()

# data.drop_duplicates(inplace=True)
data.select_dtypes(include='object').columns
data['gross_annual_income']
data['dob'] = pd.to_datetime(data['dob'], format="%Y-%m-%d")
data['dob'].dtype
data['is_nri'].value_counts()
data['is_nri'] = data['is_nri'].fillna("True")
data['is_nri'].value_counts()
data['dt_first_investment']
data['dt_first_investment'] = pd.to_datetime(
    data['dt_first_investment'],
    format="mixed"
)
data['user_dt_created']
data['user_dt_created'] = pd.to_datetime(
    data['user_dt_created'],
    format="mixed"
)

data['gold_investment_date']
data['gold_investment_date'] = pd.to_datetime(
    data['gold_investment_date'],
    format="mixed"
)
data['nps_investment_date']
data['nps_investment_date'] = pd.to_datetime(
    data['nps_investment_date'],
    format="mixed"
)
date_list = ["Last_Investment_on","SIP_first_investment","SIP_Last_investment","Lumsum_first_investment","Lumsum_Last_investment"]
def change_colum_datetime(date_list):
    for x in date_list:
        data[x] = pd.to_datetime(
            data[x],
            format="mixed"
        )
change_colum_datetime(date_list)
for x in date_list:
    data[x]
data['occupation'].value_counts(normalize=True) * 100
data['Age'].min()
data['Age'].max() 
data['Age'].mean()
data['Age'].median()
data['Age'].std()

data['churn'] = (data['Investment_tenure_since_last_investment_in_months'] > 6).astype(int)
corr_matrix = data.corr(numeric_only=True)
'''
+1 → perfect positive relationship (when X ↑, Y ↑ proportionally)
-1 → perfect negative relationship (when X ↑, Y ↓ proportionally)
0 → no linear relationship

Importance of corr_matrix:
    1. It's helpful in feature selection 
        If two features are very highly correlated (>0.85), they give duplicate information.
        we can keep just one of them in the model.
    2. correlation with churn with each column 
    3. If features are too correlated with each other, models like Logistic Regression may become unstable.
        In that case, we can drop/reduce features.
'''
print(corr_matrix)
corr_matrix.to_csv(r"C:\Users\Admin\Downloads\correlation_matrix2.csv")


plt.figure(figsize=(12,10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

# ===================================================================
# ===================================================================
