# 🚢 Titanic Data Analysis Project

## 📌 Overview
This project performs data preprocessing and exploratory data analysis (EDA) on the Titanic dataset to understand patterns related to passenger survival.

---

## 📂 Dataset
- Dataset: Titanic (`train.csv`)
- Contains passenger details like age, class, gender, etc.

---

## 🧹 Data Preprocessing
- Checked dataset info and statistics
- Identified missing values
- Handled missing data:
  - Age → filled with mean
  - Cabin → filled with "Unknown"
  - Embarked → filled with 0
- Checked duplicate values

---

## 📊 Exploratory Data Analysis
Visualizations created:
- Survival count (bar chart)
- Age distribution (histogram)
- Gender distribution (pie chart)
- Survival rate by passenger class (Seaborn barplot)
- Age distribution (Seaborn histogram)

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn
python your_script_name.py
