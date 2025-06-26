from sklearn.cluster import KMeans
import pandas as pd

# 🍦 Our simple ice cream data
data = {
    'ice_cream_per_week': [2, 3, 10, 11, 5, 1],
    'money_spent': [100, 150, 1000, 1100, 400, 90]
}

df = pd.DataFrame(data)

# 🧠 Create KMeans with 2 clusters (K=2)
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(df)

# 👀 Show which cluster each person belongs to
df['cluster'] = kmeans.labels_

print(df)
