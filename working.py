import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import LabelEncoder

# Load your dataset
df = pd.read_csv("mf_investor_data.csv")  # Replace with your data path

# Step 1: Create Churn label (adjust definition as needed)
df['churn'] = (df['Investment_tenure_since_last_investment_in_months'] > 6).astype(int)

# Step 2: Drop identifiers
drop_cols = ['user_key', 'profile_id', 'dob', 'user_dt_created',
             'dt_first_investment', 'gold_investment_date', 
             'nps_investment_date', 'Last_Investment_on',
             'SIP_first_investment', 'SIP_Last_investment',
             'Lumsum_first_investment', 'Lumsum_Last_investment']
df = df.drop(columns=drop_cols)

# Step 3: Encode categorical columns
cat_cols = df.select_dtypes(include=['object', 'bool']).columns
for col in cat_cols:
    df[col] = df[col].astype(str)
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Step 4: Features & Target
X = df.drop(columns=['churn'])
y = df['churn']

# Step 5: Train/Test split (time-based split if possible)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 6: LightGBM model
lgb_train = lgb.Dataset(X_train, y_train)
lgb_test = lgb.Dataset(X_test, y_test, reference=lgb_train)

params = {
    'objective': 'binary',
    'metric': 'auc',
    'boosting_type': 'gbdt',
    'learning_rate': 0.05,
    'num_leaves': 31,
    'verbose': -1
}

model = lgb.train(
    params,
    lgb_train,
    valid_sets=[lgb_train, lgb_test],
    num_boost_round=500,
    early_stopping_rounds=50
)

# Step 7: Predictions & Evaluation
y_pred_proba = model.predict(X_test, num_iteration=model.best_iteration)
y_pred = (y_pred_proba > 0.5).astype(int)

print("ROC AUC:", roc_auc_score(y_test, y_pred_proba))
print(classification_report(y_test, y_pred))

# Step 8: Feature importance
import matplotlib.pyplot as plt
lgb.plot_importance(model, max_num_features=20)
plt.show()
