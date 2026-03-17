import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Load the Dataset
df = pd.read_csv("titanicdataset/train.csv")
print(df.head())

#Getting the Information about the dataset
print(df.info())

print(df.describe())

#Checking the null values
print("Null Values In the Dataset: ")
print(df.isnull().sum())

#If any Null values It will be replaced by 0
print("Values After Replacing Null Values: ")
print(df.fillna(0))

#Age Column has 177 null values, we can replace it with using the fillna method
print("Age column updated with mean Values: ")
df["Age"] = df["Age"].fillna(df["Age"].mean().astype("int64"))
print(df["Age"])

#Cabin column has 687 null values, we can replace it with using the fillna method
print("Cabin column updated with 'Unknown' values: ")
df["Cabin"] = df["Cabin"].fillna("Unknown")
print(df["Cabin"])

#Embarked column has 2 null values, we can replace it eith the fillna method
print("Embarked column update with 0 values: ")
df["Embarked"] = df["Embarked"].fillna(0)
print(df["Embarked"])

#Finfing the duplicated in the Dataset
print("Duplicated values in the dataset: ")
print(df.duplicated().sum())

#Graphical Representation of the dataset
#Bar Graph For the Survival Count
plt.bar(df["Survived"].value_counts().index, df["Survived"].value_counts().values)
plt.xlabel("Survived")
plt.ylabel("Count")
plt.title("Survival Count")
plt.legend(["Not Survived","Survived"])
plt.show()

#Histogram Graph for the Age Distribution
plt.hist(df["Age"], bins=20, color="green")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()

#Pie Chart for the Gender Distribution
plt.pie(df["Sex"].value_counts().values, labels=df["Sex"].value_counts().index,autopct="%1.1f%%",colors=["blue","green"])
plt.title("Gender Distribution")
plt.show()

#Using the seaborn Library to Create a Bar Plot
sns.barplot(x="Pclass",y="Survived",data=df)
plt.title("Survival Rate By Passenger Class")
plt.show()

#Using the seaborn library to create the histogram for the age Distribution
sns.histplot(df["Age"],bins=20,color="orange")
plt.title("Age Distribution")
plt.show()



