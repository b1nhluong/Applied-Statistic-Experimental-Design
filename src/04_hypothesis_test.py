import pandas as pd
from scipy.stats import ttest_ind

# Load the balanced dataset
df = pd.read_csv('Data/Thursday_Sampled_Balanced.csv')

# Split data by label
benign = df[df['Label'] == 0]
attack = df[df['Label'] == 1]

# List of features to test
features_to_test = ['Packet Length Mean', 'Flow Bytes/s']

for feature in features_to_test:
    benign_values = benign[feature]
    attack_values = attack[feature]
    
    # Perform independent two-sample T-test
    t_stat, p_value = ttest_ind(benign_values, attack_values, equal_var=False)
    
    print(f"📊 T-test for feature: {feature}")
    print(f"T-statistic = {t_stat:.4f}")
    print(f"P-value = {p_value:.4e}")
    
    if p_value < 0.05:
        print("✅ Statistically significant difference between BENIGN and ATTACK.\n")
    else:
        print("❌ No significant difference found.\n")
