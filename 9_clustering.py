import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])

# K-Means clustering with visualization
def plot_kmeans(X, kmeans, iteration):
    # Plot data points
    plt.scatter(X['Petal_Length'], X['Petal_Width'], c=kmeans.labels_, cmap='viridis', s=50)

    # Plot centroids
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 2], centers[:, 3], c='red', marker='x', s=200, label='Centroids')
    plt.title(f'Iteration {iteration}')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.legend()
    plt.show()

# Initialize KMeans
kmeans = KMeans(n_clusters=3, init='random', n_init=1, max_iter=1, random_state=0)

# Run K-Means with manual iterations for visualization
previous_centroids = None
for i in range(1, 11):  # Allow up to 10 iterations
    if i == 1:
        kmeans.fit(X)  # Perform first iteration
    else:
        kmeans = KMeans(n_clusters=3, init=kmeans.cluster_centers_, n_init=1, max_iter=1, random_state=0)
        kmeans.fit(X)
    
    # Compare centroids for convergence
    current_centroids = kmeans.cluster_centers_
    if previous_centroids is not None and np.allclose(previous_centroids, current_centroids, atol=1e-4):
        print(f"Convergence achieved at iteration {i}")
        break
    
    previous_centroids = current_centroids  # Update previous centroids for the next iteration
    print(f'Iteration {i}: Centroids\n', current_centroids)
    plot_kmeans(X, kmeans, i)

# Calculate Silhouette Score
from sklearn.metrics import silhouette_score
print("kmeans labels",kmeans.labels_)
score = silhouette_score(X, kmeans.labels_)
print("Silhouette Score:", score)
