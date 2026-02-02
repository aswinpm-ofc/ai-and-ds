"""
Question 4: Feature Selection – Iris Dataset
"""

# =========================
# IMPORT LIBRARIES
# =========================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# =========================
# (a) LOAD IRIS DATASET
# =========================
iris = load_iris()

X = iris.data
y = iris.target
feature_names = iris.feature_names

df = pd.DataFrame(X, columns=feature_names)
df["target"] = y

print("Dataset shape:", df.shape)
print(df.head())

# =========================
# (b) EXPLORATORY DATA ANALYSIS (EDA)
# =========================
print("\nDataset Summary:")
print(df.describe())

# Pairplot
sns.pairplot(df, hue="target")
plt.show()

# Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.iloc[:, :-1].corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.show()

# =========================
# TRAIN-TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================
# BASELINE MODEL (ALL FEATURES)
# =========================
svm = SVC(kernel="linear")
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

baseline_accuracy = accuracy_score(y_test, y_pred)
print("\nBaseline Accuracy (All Features):", baseline_accuracy)

# =========================
# (c-1) UNIVARIATE FEATURE SELECTION
# =========================
selector = SelectKBest(score_func=f_classif, k=2)
X_train_uni = selector.fit_transform(X_train, y_train)
X_test_uni = selector.transform(X_test)

selected_uni_features = np.array(feature_names)[selector.get_support()]
print("\nUnivariate Selected Features:", selected_uni_features)

svm.fit(X_train_uni, y_train)
y_pred_uni = svm.predict(X_test_uni)

uni_accuracy = accuracy_score(y_test, y_pred_uni)
print("Accuracy after Univariate Selection:", uni_accuracy)

# =========================
# (c-2) FEATURE IMPORTANCE (RANDOM FOREST)
# =========================
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]

print("\nRandom Forest Feature Importances:")
for i in indices:
    print(feature_names[i], ":", importances[i])

top_features_rf = indices[:2]
X_train_rf = X_train[:, top_features_rf]
X_test_rf = X_test[:, top_features_rf]

svm.fit(X_train_rf, y_train)
y_pred_rf = svm.predict(X_test_rf)

rf_accuracy = accuracy_score(y_test, y_pred_rf)
print("Accuracy using Random Forest Selected Features:", rf_accuracy)

# =========================
# (c-3) RFE WITH SVM
# =========================
rfe = RFE(estimator=SVC(kernel="linear"), n_features_to_select=2)
rfe.fit(X_train, y_train)

selected_rfe_features = np.array(feature_names)[rfe.support_]
print("\nRFE Selected Features:", selected_rfe_features)

X_train_rfe = rfe.transform(X_train)
X_test_rfe = rfe.transform(X_test)

svm.fit(X_train_rfe, y_train)
y_pred_rfe = svm.predict(X_test_rfe)

rfe_accuracy = accuracy_score(y_test, y_pred_rfe)
print("Accuracy after RFE:", rfe_accuracy)

# =========================
# (e) PERFORMANCE COMPARISON
# =========================
print("\n--- MODEL PERFORMANCE COMPARISON ---")
print("All Features Accuracy      :", baseline_accuracy)
print("Univariate Selection Acc   :", uni_accuracy)
print("Random Forest Selection Acc:", rf_accuracy)
print("RFE Selection Acc          :", rfe_accuracy)
