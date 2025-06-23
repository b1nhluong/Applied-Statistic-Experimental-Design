import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu mẫu
df = pd.read_csv('Data/Thursday_Sampled_Balanced.csv')

# --- CÁC CỘT QUAN TÂM ---
columns_of_interest = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Packet Length Mean'
]

# --- THỐNG KÊ MÔ TẢ TỔNG QUAN ---
print("📊 Overall Descriptive Statistics:")
print(df[columns_of_interest].describe())

# --- THỐNG KÊ THEO NHÃN ---
print("\n📊 Mean by Label (BENIGN vs ATTACK):")
print(df.groupby('Label')[columns_of_interest].mean())

# --- BIỂU ĐỒ BOXPLOT ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='Label', y='Packet Length Mean', data=df)
plt.title('Comparison of Average Packet Length between BENIGN and ATTACK')
plt.xlabel('Label (0 = BENIGN, 1 = ATTACK)')
plt.ylabel('Packet Length Mean')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# --- BIỂU ĐỒ HISTOGRAM ---
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Flow Duration', hue='Label', bins=50, kde=True, element='step')
plt.title('Distribution of Flow Duration by Label')
plt.xlabel('Flow Duration')
plt.ylabel('Number of Records')
plt.tight_layout()
plt.show()
