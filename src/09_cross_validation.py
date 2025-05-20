import pandas as pd
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

# Load data
df = pd.read_csv('Thursday_Sampled_Balanced.csv')

# Select features and target
features = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Packet Length Mean'
]
X = df[features]
y = df['Label']

# Create pipeline: scaling + logistic regression
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(max_iter=1000))
])

# Define 5-fold cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Perform cross-validation for accuracy
scores = cross_val_score(pipeline, X, y, cv=cv, scoring='accuracy')

print("📊 Logistic Regression Cross-Validation Results:")
print(f"Fold Accuracies: {np.round(scores, 4)}")
print(f"Mean Accuracy: {scores.mean():.4f}")
print(f"Standard Deviation: {scores.std():.4f}")
