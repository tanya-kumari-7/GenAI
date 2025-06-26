import pandas as pd

# Sample data: age and salary of potential car buyers
data = {
    'buyer_id': list(range(1, 11)),
    'age': [22, 25, 47, 52, 46, 56, 26, 48, 33, 40],
    'estimated_salary': [25000, 27000, 70000, 75000, 72000, 80000, 30000, 68000, 35000, 60000]
}

df = pd.DataFrame(data)
print(df)


from sklearn.cluster import KMeans
# Select features for clustering

X = df[['age', 'estimated_salary']]

# Create KMeans model
kmeans = KMeans(n_clusters=3, random_state=0)
# Fit model
kmeans.fit(X)
# Assign clusters to original dataframe
df['cluster'] = kmeans.labels_
print(df)

# Import necessary libraries
import matplotlib.pyplot as plt
# Plot the clusters
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['estimated_salary'], c=df['cluster'], cmap='viridis', s=100)
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.title('K-Means Clustering of Car Buyers')
# Save the plot to a file
plt.savefig('kmeans_clustering_car_buyers.png')
plt.show()
