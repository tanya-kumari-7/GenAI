# 📌 1. Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs

# 📌 2. Generate Sample Data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)

# 📌 3. Visualize Data
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Sample Data")
plt.show()

# 📌 4. Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# 📌 5. Predict Clusters
y_kmeans = kmeans.predict(X)

# 📌 6. Visualize Clusters + Centroids
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, c='red', marker='X', label='Centroids')
plt.title("KMeans Clusters + Centroids")
plt.legend()
plt.show()

# 📌 7. Elbow Method to Find Optimal K
inertia_list = []

K_range = range(1, 11)
for k in K_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42)
    kmeans_temp.fit(X)
    inertia_list.append(kmeans_temp.inertia_)

plt.plot(K_range, inertia_list, 'bo-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Elbow Method - Optimal K')
plt.show()

# 📌 8. Silhouette Score (for K=4)
score = silhouette_score(X, y_kmeans)
print(f"Silhouette Score for K=4: {score:.3f}")
