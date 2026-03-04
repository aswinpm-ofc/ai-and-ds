import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import skfuzzy as fuzz
from sklearn.datasets import make_blobs
from scipy.spatial.distance import cdist

# Generate dataset
X, y = make_blobs(n_samples=300, centers=3, random_state=42)
k = 3

# ==========================
# 1️⃣ K-MEANS
# ==========================
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# ==========================
# 2️⃣ MANUAL K-MEDOIDS
# ==========================
def k_medoids(X, k, max_iter=100):
    medoids = X[np.random.choice(len(X), k, replace=False)]
    
    for _ in range(max_iter):
        distances = cdist(X, medoids)
        labels = np.argmin(distances, axis=1)
        
        new_medoids = []
        for i in range(k):
            cluster_points = X[labels == i]
            if len(cluster_points) == 0:
                continue
            distances_in_cluster = cdist(cluster_points, cluster_points)
            medoid_index = np.argmin(distances_in_cluster.sum(axis=1))
            new_medoids.append(cluster_points[medoid_index])
        
        new_medoids = np.array(new_medoids)
        
        if np.all(medoids == new_medoids):
            break
            
        medoids = new_medoids
        
    return labels

kmedoids_labels = k_medoids(X, k)

# ==========================
# 3️⃣ FUZZY C-MEANS
# ==========================
cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(
    X.T, c=k, m=2, error=0.005, maxiter=1000
)

fcm_labels = np.argmax(u, axis=0)

# ==========================
# VISUALIZATION
# ==========================
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels)
plt.title("K-Means")

plt.subplot(1, 3, 2)
plt.scatter(X[:, 0], X[:, 1], c=kmedoids_labels)
plt.title("K-Medoids (Manual)")

plt.subplot(1, 3, 3)
plt.scatter(X[:, 0], X[:, 1], c=fcm_labels)
plt.title("Fuzzy C-Means")

plt.tight_layout()
plt.savefig("clustering_output.png")
print("Plot saved as clustering_output.png")