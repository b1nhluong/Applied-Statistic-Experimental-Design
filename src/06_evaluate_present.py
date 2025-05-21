import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# --- ĐỌC DỮ LIỆU ---
df = pd.read_csv('Data/Thursday_Sampled_Balanced.csv')

# --- CHỌN BIẾN ĐẦU VÀO & CHUẨN HÓA ---
features = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Packet Length Mean'
]
X = df[features]
y = df['Label']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- TRAIN / TEST SPLIT ---
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# --- HUẤN LUYỆN LẠI MÔ HÌNH ---
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# --- ĐÁNH GIÁ: CONFUSION MATRIX ---
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["BENIGN", "ATTACK"], yticklabels=["BENIGN", "ATTACK"])
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Dự đoán")
plt.ylabel("Thực tế")
plt.tight_layout()
plt.show()

# --- IN CHỈ SỐ PHÂN LOẠI ---
print("📈 Classification Report:")
print(classification_report(y_test, y_pred))

# --- VẼ BOXPLOT: ĐỘ DÀI GÓI TIN THEO DỰ ĐOÁN ---
df_test = pd.DataFrame(X_test, columns=features)
df_test['Actual'] = y_test.values
df_test['Predicted'] = y_pred

plt.figure(figsize=(8, 5))
sns.boxplot(x='Predicted', y='Packet Length Mean', data=df_test)
plt.title('Phân phối độ dài gói tin theo dự đoán của mô hình')
plt.xlabel('Dự đoán (0 = BENIGN, 1 = ATTACK)')
plt.ylabel('Packet Length Mean (scaled)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
