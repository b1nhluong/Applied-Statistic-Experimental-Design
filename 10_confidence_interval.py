import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

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

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Add constant for intercept
X_const = sm.add_constant(X_scaled)

# Fit logistic regression using statsmodels
logit_model = sm.Logit(y, X_const)
result = logit_model.fit(disp=0)

# Show coefficients with 95% confidence intervals
summary_df = result.summary2().tables[1]
ci = result.conf_int(alpha=0.05)
summary_df['CI Lower'] = ci[0]
summary_df['CI Upper'] = ci[1]

print("📈 Logistic Regression Coefficients with 95% Confidence Intervals:")
print(summary_df[['Coef.', 'Std.Err.', 'z', 'P>|z|', 'CI Lower', 'CI Upper']])
