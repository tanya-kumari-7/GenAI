import pandas as pd

# Create a small mock dataset
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'annual_income': [25000, 30000, 50000, 55000, 60000, 85000, 90000, 95000, 100000, 105000],
    'spending_score': [20, 25, 30, 60, 65, 80, 85, 90, 35, 40]
}

df = pd.DataFrame(data)
print(df)

from sklearn.cluster import KMeans

# Select features for clustering
X = df[['annual_income', 'spending_score']]

# Create KMeans model
kmeans = KMeans(n_clusters=3, random_state=0)

# Fit model
kmeans.fit(X)

# Assign clusters to original dataframe
df['cluster'] = kmeans.labels_

print(df)


import matplotlib.pyplot as plt
# Plot the clusters
plt.figure(figsize=(10, 6))
plt.scatter(df['annual_income'], df['spending_score'], c=df['cluster'], cmap='viridis', s=100)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('K-Means Clustering of Customers')
# Save the plot to a file
plt.savefig('kmeans_clustering_customers.png')
plt.show()


