import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

print("First 5 rows of the dataset:")
print(df.head())

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

plt.figure(figsize=(15, 10))
df[numeric_columns].hist(figsize=(15, 10), bins=20, color="skyblue")
plt.suptitle("Histograms of Numeric Features")
plt.show()

for column in numeric_columns:
    plt.figure(figsize=(8, 5))
    sns.kdeplot(df[column], shade=True, color="green")
    plt.title(f"Distribution (KDE) of {column}")
    plt.xlabel(column)
    plt.ylabel("Density")
    plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df[numeric_columns])
plt.title("Boxplots of Numeric Features")
plt.show()
