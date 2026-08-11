import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

print("First 5 rows of the dataset:")
print(df.head())

categorical_columns = df.select_dtypes(include=["object"]).columns
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for column in categorical_columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=column, data=df, palette="Set2")
    plt.title(f"Countplot of {column}")
    plt.xticks(rotation=45)
    plt.show()

for cat_col in categorical_columns:
    for num_col in numeric_columns:
        plt.figure(figsize=(8, 5))
        sns.barplot(x=cat_col, y=num_col, data=df, palette="husl", ci=None)
        plt.title(f"Barplot of {num_col} by {cat_col}")
        plt.xticks(rotation=45)
        plt.show()

for cat_col in categorical_columns:
    for num_col in numeric_columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=cat_col, y=num_col, data=df, palette="coolwarm")
        plt.title(f"Boxplot of {num_col} by {cat_col}")
        plt.xticks(rotation=45)
        plt.show()
