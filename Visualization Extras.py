import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load the dataset (replace 'CO2_Emissions.csv' with your uploaded dataset name)
df = pd.read_csv('CO2_Emissions.csv')

# 2. Check for missing/null values and handle them
print("--- Checking Missing/Null Values ---")
print(df.isnull().sum())

# Drop null values if present
df = df.dropna()

# 3. Check details of the dataset (Data types, non-null counts, structure)
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# 4. Create a new dataframe with mean values grouped by 'Fuel Type'
# (numeric_only=True ensures non-numeric columns don't break the mean calculation)
grouped_df = df.groupby('Fuel Type').mean(numeric_only=True)

# 5. Reset the index of the new dataframe and update it
grouped_df = grouped_df.reset_index()

print("\n--- Grouped Data Frame (Mean Values) ---")
print(grouped_df)

# 6. Create a barplot for 'Fuel Type' and 'Average CO2 Emissions'
plt.figure(figsize=(10, 6))
plots = sns.barplot(
    x='Fuel Type',
    y='CO2 Emissions(g/km)',
    data=grouped_df,
    palette='teal',
)

# 7. Annotate the bars of the plot using Matplotlib
for bar in plots.patches:
    plots.annotate(
        format(bar.get_height(), '.2f'),
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        ha='center',
        va='center',
        size=11,
        xytext=(0, 8),
        textcoords='offset points',
    )

# Formatting the plot
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Average CO2 Emissions (g/km)', fontsize=12)
plt.title('Average CO2 Emissions by Fuel Type', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()
