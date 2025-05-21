import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('Data/Thursday_Sampled_Balanced.csv')

# Select features and target
features = [
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Packet Length Mean'
]
X = df[features]
y = df['Flow Duration']  # Continuous variable

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("📈 Linear Regression Results:")
print(f"Mean Squared Error (MSE): {mse:,.2f}")
print(f"R-squared (R²): {r2:.4f}")

# Plot predicted vs actual
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.xlabel("Actual Flow Duration")
plt.ylabel("Predicted Flow Duration")
plt.title("Predicted vs Actual Flow Duration")
plt.grid(True)
plt.tight_layout()
plt.show()
