
---

# ✅ **README – Commit 2 (Model + Evaluation Update)**
Update your README in the **second commit**:

```markdown
# 🚢 Titanic Survival Prediction Project

## 📌 Overview
This project analyzes the Titanic dataset, performs data preprocessing and visualization, and builds a machine learning model to predict passenger survival.

---

## 📂 Dataset
- Dataset: Titanic (`train.csv`)
- Features include passenger class, age, family details, gender, etc.

---

## 🧹 Data Preprocessing
- Handled missing values:
  - Age → mean
  - Cabin → "Unknown"
  - Embarked → 0
- Checked duplicates

---

## 📊 Exploratory Data Analysis
- Bar chart (Survival count)
- Histogram (Age distribution)
- Pie chart (Gender distribution)
- Seaborn barplot (Survival by class)
- Seaborn histogram (Age)

---

## 🤖 Machine Learning Model
- Model: Logistic Regression
- Features used:
  - Pclass
  - Age
  - SibSp
  - Parch

### Train-Test Split
- 80% training
- 20% testing

---

## 📈 Model Evaluation
- Accuracy Score
- Classification Report
- Confusion Matrix

### 🔷 Confusion Matrix Visualization
- Heatmap created using Seaborn
- Shows prediction performance clearly

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python your_script_name.py
