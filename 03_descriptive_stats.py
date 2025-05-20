import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu mẫu
df = pd.read_csv('Thursday_Sampled_Balanced.csv')

# --- CÁC CỘT QUAN TÂM ---
columns_of_interest = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Packet Length Mean'
]

# --- THỐNG KÊ MÔ TẢ TỔNG QUAN ---
print("📊 Thống kê mô tả tổng thể:")
print(df[columns_of_interest].describe())

# --- THỐNG KÊ THEO NHÃN ---
print("\n📊 Trung bình theo nhãn (BENIGN vs ATTACK):")
print(df.groupby('Label')[columns_of_interest].mean())

# --- BIỂU ĐỒ BOXPLOT ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='Label', y='Packet Length Mean', data=df)
plt.title('So sánh độ dài gói tin trung bình giữa BENIGN và ATTACK')
plt.xlabel('Label (0 = BENIGN, 1 = ATTACK)')
plt.ylabel('Packet Length Mean')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# --- BIỂU ĐỒ HISTOGRAM ---
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Flow Duration', hue='Label', bins=50, kde=True, element='step')
plt.title('Phân phối Flow Duration theo nhãn')
plt.xlabel('Flow Duration')
plt.ylabel('Số dòng')
plt.tight_layout()
plt.show()
