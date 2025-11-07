import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Configuration
n_samples = 50000   # number of total rows (make larger if you want slower/longer training)
n_features = 6      # number of feature columns
np.random.seed(42)

# Generate random input features (values between 0 and 100)
X = np.random.rand(n_samples, n_features) * 100

# True underlying weights (controls the relation between features and target)
true_weights = np.array([3.4, -2.8, 4.1, 1.5, 0.8, 2.3])
bias = 10.0

# Add some noise for realism
noise = np.random.randn(n_samples) * 10

# Linear target function: y = Xw + b + noise
y = X.dot(true_weights) + bias + noise

# Build DataFrame
columns = [f"feature_{i+1}" for i in range(n_features)]
df = pd.DataFrame(X, columns=columns)
df["target"] = y

# Split into 76% train and 24% test
train_df, test_df = train_test_split(df, test_size=0.24, random_state=42)

# Save to CSV
train_df.to_csv("train_data.csv", index=False)
test_df.to_csv("test_data.csv", index=False)

print(f"✅ Created dataset with {n_samples} samples and {n_features} features.")
print(f"   Training data: {len(train_df)} rows → train_data.csv")
print(f"   Testing data : {len(test_df)} rows → test_data.csv")
