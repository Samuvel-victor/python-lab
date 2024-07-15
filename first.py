import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate random data
X = np.random.rand(100, 2)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.labels_

# Plot the data points and cluster centers
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')
plt.show()
//asasd djv fdj vjsd j