import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load the CO2 Emissions dataset
# (Replace 'CO2_Emissions.csv' with your dataset file name)
df = pd.read_csv('CO2_Emissions.csv')

# Display the first few rows
print("--- Dataset Sample ---")
print(df.head())

# 2. Check for null values and handle them
print("\n--- Checking for Null Values ---")
print(df.isnull().sum())

# Drop missing values if any exist
df = df.dropna()

# 3. Check details of the dataset (Data types, Non-null counts, etc.)
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# 4. Try different themes in Seaborn on a countplot for 'Fuel Type'
themes = ['white', 'dark', 'whitegrid', 'darkgrid', 'ticks']

for theme in themes:
    sns.set_style(theme)
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Fuel Type', data=df)
    plt.title(f"Fuel Type Countplot - Theme: {theme}")
    plt.show()

# 5. Set the theme to 'white' and remove spines (despine)
sns.set_style('white')
plt.figure(figsize=(8, 5))
sns.countplot(x='Fuel Type', data=df)
sns.despine()
plt.title('Fuel Type Countplot with Despined Spines')
plt.show()

# 6. Set custom palette of choice
sns.set_style('whitegrid')
plt.figure(figsize=(8, 5))
sns.countplot(x='Fuel Type', data=df, palette='viridis')
plt.title('Fuel Type Countplot with Viridis Palette')
plt.show()

# 7. Set custom bar color of choice
plt.figure(figsize=(8, 5))
sns.countplot(x='Fuel Type', data=df, color='teal')
plt.title('Fuel Type Countplot with Custom Color (Teal)')
plt.show()

# 8. Try scaling figure styles (paper, notebook, talk, poster)
contexts = ['paper', 'notebook', 'talk', 'poster']

for ctx in contexts:
    sns.set_style('whitegrid')
    sns.set_context(ctx)
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Fuel Type', data=df, palette='Set2')
    plt.title(f"Figure Scaling Context: {ctx}")
    plt.show()

# 9. Set scale to 'poster', reduce font size to 0.8, and rotate xticks
sns.set_style('whitegrid')
sns.set_context('poster', font_scale=0.8)

plt.figure(figsize=(10, 6))
sns.countplot(x='Fuel Type', data=df, palette='magma')
plt.xticks(rotation=45)
plt.title('Poster Context with Rotated Ticks & 0.8 Font Scale')
plt.tight_layout()
plt.show()
