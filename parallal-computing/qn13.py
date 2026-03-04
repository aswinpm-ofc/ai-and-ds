import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

# ==========================
# Load Dataset
# ==========================
data = load_iris()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ==========================
# Individual Classifiers
# ==========================
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(),
    "Naive Bayes": GaussianNB(),
    "SVM": SVC(),
    "Random Forest": RandomForestClassifier(n_estimators=100)
}

print("\n===== Individual Model Accuracy =====\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name}: {acc:.4f}")

# ==========================
# Voting Classifier (Ensemble)
# ==========================
voting = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression(max_iter=200)),
        ('dt', DecisionTreeClassifier()),
        ('svm', SVC())
    ],
    voting='hard'
)

voting.fit(X_train, y_train)
y_pred_vote = voting.predict(X_test)
vote_acc = accuracy_score(y_test, y_pred_vote)

print("\n===== Ensemble Model Accuracy =====\n")
print(f"Voting Classifier: {vote_acc:.4f}")
