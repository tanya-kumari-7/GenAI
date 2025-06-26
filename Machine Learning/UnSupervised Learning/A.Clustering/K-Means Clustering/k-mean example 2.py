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

import matplotlib.pyplot as plt

# Plot the data
plt.scatter(df['ice_cream_per_week'], df['money_spent'], c=df['cluster'], cmap='viridis', s=100)

# Label the axes
plt.xlabel('Ice Creams per Week')
plt.ylabel('Money Spent (₹)')
plt.title('K-Means Clustering of Ice Cream Lovers')

# Show plot
plt.show()

