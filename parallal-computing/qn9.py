import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings("ignore")

# ==============================
# Load Dataset
# ==============================
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset Loaded Successfully")
print("Original Shape:", X.shape)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Cross validation setup
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
classifier = RandomForestClassifier(random_state=42)


# ==============================
# Function to evaluate model
# ==============================
def evaluate_model(X_transformed, name):
    scores = cross_val_score(classifier, X_transformed, y, cv=cv)
    print(f"{name} Accuracy: {scores.mean():.4f}")
    return scores.mean()


print("\n========== CASE 1: 2 FEATURES ==========")

# PCA (2 components)
pca_2 = PCA(n_components=2)
X_pca_2 = pca_2.fit_transform(X_scaled)
acc_pca_2 = evaluate_model(X_pca_2, "PCA (2 components)")

# LDA (2 components)
lda_2 = LinearDiscriminantAnalysis(n_components=2)
X_lda_2 = lda_2.fit_transform(X_scaled, y)
acc_lda_2 = evaluate_model(X_lda_2, "LDA (2 components)")

# SVD (2 components)
svd_2 = TruncatedSVD(n_components=2)
X_svd_2 = svd_2.fit_transform(X_scaled)
acc_svd_2 = evaluate_model(X_svd_2, "SVD (2 components)")

# TSNE (2 components)
tsne_2 = TSNE(n_components=2, random_state=42)
X_tsne_2 = tsne_2.fit_transform(X_scaled)
acc_tsne_2 = evaluate_model(X_tsne_2, "TSNE (2 components)")


print("\n========== CASE 2: 3 FEATURES ==========")

# PCA (3 components)
pca_3 = PCA(n_components=3)
X_pca_3 = pca_3.fit_transform(X_scaled)
acc_pca_3 = evaluate_model(X_pca_3, "PCA (3 components)")

# LDA (max 2 components for Iris because classes-1 = 2)
# So we keep 2 components (cannot make 3)
print("LDA supports maximum 2 components for Iris dataset")

# SVD (3 components)
svd_3 = TruncatedSVD(n_components=3)
X_svd_3 = svd_3.fit_transform(X_scaled)
acc_svd_3 = evaluate_model(X_svd_3, "SVD (3 components)")

# TSNE (3 components)
tsne_3 = TSNE(n_components=3, random_state=42)
X_tsne_3 = tsne_3.fit_transform(X_scaled)
acc_tsne_3 = evaluate_model(X_tsne_3, "TSNE (3 components)")


print("\n========== INFERENCE ==========")

print("""
1. LDA generally performs best because it is supervised 
   and maximizes class separability.

2. PCA and SVD preserve variance but are unsupervised.

3. t-SNE is mainly for visualization and may not always 
   give highest classification accuracy.

4. Increasing from 2 to 3 components slightly improves
   performance for PCA and SVD.

5. LDA is limited to (number_of_classes - 1) components.
""")
