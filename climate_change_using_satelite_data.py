# -*- coding: utf-8 -*-
"""Climate change using satelite data

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V47oyyLd8TjMhvQGAb5_2MHeef1XSdWw
"""

#step 1 - declaring required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#step 2 - importing dataset
df = pd.read_csv('/GLB.Ts+dSST.csv', skiprows=1)

print(df.head())

# step 3 - cleaning data set
df.columns = df.columns.str.strip()


df = df[['Year', 'J-D']]
df.columns = ['Year', 'TempAnomaly']

df.dropna(inplace=True)
df = df[df['TempAnomaly'] != '***']
df['Year'] = df['Year'].astype(int)
df['TempAnomaly'] = pd.to_numeric(df['TempAnomaly'], errors='coerce')
df.dropna(inplace=True)
df.head()

# step 4- using scatter plot for representing temperature over time
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['TempAnomaly'], color='tomato', s=15, alpha=0.7)
plt.title('📈 Global Temperature Anomaly Over Time (Scatter Plot)')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# step 5 - representing Line Chart for  Global Temperature Anomaly Over Time

plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['TempAnomaly'], color='blue', label='Temp Anomaly')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Global Temperature Anomaly Over Time (Satellite Data)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# step 6 - representing Line Chart for Linear Trend Line

x = df['Year']
y = df['TempAnomaly']
m, b = np.polyfit(x, y, 1)

plt.figure(figsize=(12, 6))
plt.plot(x, y, color='skyblue', label='Temp Anomaly')
plt.plot(x, m*x + b, color='red', linestyle='--', label=f'Trend Line ({m:.4f}°C/year)')
plt.title('Trend in Global Temperature Anomaly')
plt.xlabel('Year')
plt.ylabel('Anomaly (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# step 7- Bar Chart for  Decade-Wise Average Temperature Anomaly


df['Decade'] = (df['Year'] // 10) * 10
decade_avg = df.groupby('Decade')['TempAnomaly'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(decade_avg['Decade'], decade_avg['TempAnomaly'], width=8, color='orange', edgecolor='black')
plt.xlabel('Decade')
plt.ylabel('Average Temp Anomaly (°C)')
plt.title('Decade-wise Average Temperature Anomaly')
plt.grid(True)
plt.tight_layout()
plt.show()

#step 8 - Histogram for representing Frequency of Temperature Anomalies
plt.figure(figsize=(10, 5))
plt.hist(df['TempAnomaly'], bins=20, color='green', edgecolor='black')
plt.xlabel('Temperature Anomaly (°C)')
plt.ylabel('Frequency')
plt.title('Distribution of Annual Temperature Anomalies')
plt.grid(True)
plt.tight_layout()
plt.show()

#step 9-Compare Pre vs Post-1970

before_1970 = df[df['Year'] < 1970]['TempAnomaly'].mean()
after_1970 = df[df['Year'] >= 1970]['TempAnomaly'].mean()

print(f"Average Temperature Anomaly before 1970: {before_1970:.3f}°C")
print(f"Average Temperature Anomaly after 1970: {after_1970:.3f}°C")

