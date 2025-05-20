# 📊 Applied Statistics Project – Network Attack Detection (Thursday Dataset)

## 🎯 Objective
This project uses statistical techniques to analyze and model network flow data, with the goal of identifying cyber-attacks using the Thursday subset of a well-known intrusion detection dataset.

---

## 📁 Dataset
- **Original**: `Thursday_Cleaned_WebAttacks.csv` (~170,000 rows)
- **Cleaned & balanced**: `Thursday_Sampled_Balanced.csv` (4,326 rows, balanced BENIGN vs ATTACK)

Features include `Flow Duration`, `Total Packets`, `Flow Bytes/s`, `Packet Length Mean`, and more.

---

## ✅ Project Workflow

### 🧼 Step 2 – Data Cleaning
- Removed invalid rows (`Destination Port = 0`)
- Dropped rows with zero packets sent/received
- Filled missing values with column means
- Encoded label: `BENIGN → 0`, `ATTACK → 1`
- Balanced the dataset (2,163 rows per class)

---

### 📊 Step 3 – Descriptive Statistics

#### Boxplot: Packet Length Mean (BENIGN vs ATTACK)
Shows clear separation between benign and attack traffic.

![Figure 1 – Boxplot](./Figure_1.png)

#### Histogram: Flow Duration by Label
Attack flows tend to be much shorter.

![Figure 2 – Histogram](./Figure_2.png)

#### Correlation Heatmap
Visual overview of feature relationships.

![Figure 3 – Correlation Heatmap](./Figure_3.png)

---

### 🧪 Step 4 – Hypothesis Testing

Two-sample T-tests confirm statistically significant differences:

| Feature              | T-statistic | P-value         | Conclusion                           |
|----------------------|-------------|------------------|--------------------------------------|
| Packet Length Mean   | 21.51       | 7.3e-97          | ✅ Significant difference             |
| Flow Bytes/s         | 10.41       | 8.7e-25          | ✅ Significant difference             |

---

### 🤖 Step 5 – Logistic Regression

Logistic regression was trained using 5 standardized features. The model performs well:

#### Confusion Matrix
![Figure 4 – Confusion Matrix](./Figure_4.png)

#### Classification Report:
- Accuracy: **90%**
- Precision (ATTACK): **86%**
- Recall (ATTACK): **96%**
- F1-score (overall): **0.90**

---

### 📈 Step 6 – Evaluation & Visualization

#### Boxplot by Predicted Label
Attack predictions show low packet length mean.

![Figure 5 – Predicted Boxplot](./Figure_5.png)

---

## 📂 Project Files

| File Name                        | Description |
|----------------------------------|-------------|
| `03_descriptive_stats.py`        | Performs basic statistics and plots (boxplot, histogram) |
| `04_hypothesis_test.py`          | Runs T-tests on key features to check statistical significance |
| `05_logistic_regression_clean.py`| Builds and evaluates logistic regression (with scaling) |
| `06_evaluate_present.py`         | Visualizes model results (confusion matrix, predicted boxplot) |
| `Thursday_Sampled_Balanced.csv`  | Cleaned, balanced dataset used in all analysis |
| `README.md`                      | Project summary and documentation |
| `Figure_1.png` to `Figure_5.png` | Visualizations included in this report |

---
