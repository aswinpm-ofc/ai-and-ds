"""
mnist_logistic_regression.py

Question 2: Classification (Hard)

a. Build a logistic regression model to classify handwritten digits from MNIST
b. Evaluate using accuracy, precision, recall, and F1-score
c. Fine-tune hyperparameters using GridSearchCV
d. Visualize the decision boundary using PCA
"""

# =========================
# IMPORT LIBRARIES
# =========================
import numpy as np
import matplotlib.pyplot as plt

# OPTIONAL: Hide convergence warnings (uncomment if needed)
# import warnings
# from sklearn.exceptions import ConvergenceWarning
# warnings.filterwarnings("ignore", category=ConvergenceWarning)

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.decomposition import PCA


# =========================
# LOAD MNIST DATASET
# =========================
print("Loading MNIST dataset...")
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)
y = y.astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# =========================
# (a) LOGISTIC REGRESSION TRAINING (WITH PROGRESS)
# =========================
print("\nTraining Logistic Regression model (simulated progress):")

iteration_steps = [200, 500, 1000, 1500, 2000, 2500, 3000]
progress_acc = []

for i, iters in enumerate(iteration_steps):
    model = LogisticRegression(
        max_iter=iters,
        solver='lbfgs',
        tol=1e-4
    )
    model.fit(X_train, y_train)

    y_pred_temp = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred_temp)
    progress_acc.append(acc)

    percent = int((i + 1) / len(iteration_steps) * 100)
    print(f"Progress: {percent}% | max_iter={iters} | Accuracy={acc:.4f}")

print("\nFinal model trained.")


# =========================
# (b) MODEL EVALUATION
# =========================
print("\nEvaluating final model...")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# =========================
# (c) HYPERPARAMETER TUNING
# =========================
print("\nPerforming Grid Search CV...")

param_grid = {
    'C': [0.1, 1, 10],
    'solver': ['lbfgs', 'saga']
}

grid = GridSearchCV(
    LogisticRegression(max_iter=3000, tol=1e-4),
    param_grid,
    cv=3,
    scoring='accuracy',
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best CV Accuracy:", grid.best_score_)

best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test)

print("Test Accuracy after tuning:", accuracy_score(y_test, y_pred_best))


# =========================
# (d) DECISION BOUNDARY VISUALIZATION
# =========================
print("\nVisualizing decision boundary using PCA...")

# Reduce dimensionality to 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_train)

# Train model on PCA-reduced data
model_2d = LogisticRegression(
    solver='lbfgs',
    max_iter=3000,
    tol=1e-4
)
model_2d.fit(X_pca, y_train)


def plot_decision_boundary(X, y, model):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300)
    )

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=5)
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.title("Decision Boundary (Logistic Regression on MNIST)")
    plt.show()


# Plot using subset for clarity
plot_decision_boundary(X_pca[:5000], y_train[:5000], model_2d)

print("\nProgram completed successfully.")
