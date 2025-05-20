import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('Thursday_Sampled_Balanced.csv')

# --- CHỌN CÁC BIẾN ĐẦU VÀO ---
features = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Packet Length Mean'
]
X = df[features]
y = df['Label']

# --- CHUẨN HÓA DỮ LIỆU ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- CHIA TẬP TRAIN / TEST ---
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# --- HUẤN LUYỆN MÔ HÌNH ---
model = LogisticRegression()
model.fit(X_train, y_train)

# --- DỰ ĐOÁN ---
y_pred = model.predict(X_test)

# --- ĐÁNH GIÁ MÔ HÌNH ---
print("📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n📈 Classification Report:")
print(classification_report(y_test, y_pred))

# --- VẼ CONFUSION MATRIX ---
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["BENIGN", "ATTACK"], yticklabels=["BENIGN", "ATTACK"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
