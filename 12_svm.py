import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Create a small dataset with 2 numeric features
# Example data points where each point has 2 features and a sentiment label
# Feature 1 could represent "positivity score" and Feature 2 "intensity score"
data = np.array([
    [1.5, 2.0, 1],  # Positive sentiment
    [1.0, 1.0, 1],  # Positive sentiment
    [2.0, 2.5, 1],  # Positive sentiment
    [2.5, 1.5, 1],  # Positive sentiment
    [3.0, 1.0, 0],  # Negative sentiment
    [3.5, 0.5, 0],  # Negative sentiment
    [4.0, 1.0, 0],  # Negative sentiment
    [4.5, 1.5, 0]   # Negative sentiment
])

# Separate features and labels
X = data[:, :2]  # First two columns are features
y = data[:, 2]   # Last column is the label (1 for positive, 0 for negative)

# Step 2: Train the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(X, y)

# Step 3: Evaluate the model
y_pred = svm_model.predict(X)
print("Accuracy:", accuracy_score(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))

# Step 4: Visualize the Decision Boundary
# Create a mesh to plot the decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# Predict on each point of the mesh to determine decision boundaries
Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary and data points
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.2, cmap='coolwarm')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k', s=100)
plt.xlabel("Feature 1 (e.g., Positivity Score)")
plt.ylabel("Feature 2 (e.g., Intensity Score)")
plt.title("SVM Decision Boundary on 2-Feature Sentiment Data")
plt.show()
