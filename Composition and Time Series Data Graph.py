import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Load the dataset (replace 'CO2_Emissions.csv' with your uploaded file name)
df = pd.read_csv('CO2_Emissions.csv')

# Display first few rows
print("--- Initial Data ---")
print(df.head())

# 2. Check for missing/null values and handle them
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# Drop missing values if any exist
df = df.dropna()

# 3. Check details of the dataset (data types, non-null count, memory usage)
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# 4. Pie Chart for 'Fuel Type' with wedgeprops
plt.figure(figsize=(8, 8))
fuel_counts = df['Fuel Type'].value_counts()

plt.pie(
    fuel_counts,
    labels=fuel_counts.index,
    autopct='%.2f%%',
    labeldistance=1.15,
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
)
plt.title('Composition of Fuel Types')
plt.show()

# 5. Pie Chart for 'Vehicle Class'
plt.figure(figsize=(10, 10))
vehicle_counts = df['Vehicle Class'].value_counts()

plt.pie(vehicle_counts, labels=vehicle_counts.index, autopct='%.2f%%')
plt.title('Distribution of Vehicle Classes')
plt.show()

# 6. Line Plot for CO2 Emissions readings over time/entries
plt.figure(figsize=(12, 6))
plt.plot(df['CO2 Emissions(g/km)'], color='tab:red', linewidth=1)

plt.xlabel('Reading Index')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('CO2 Emissions Across All Vehicle Readings')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
