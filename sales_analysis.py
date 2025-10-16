import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("/content/sales datasets.xlsx")

print(df.head())
print(df.info())
print(df.describe())
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)

df['Check'] = df['Quantity'] * df['Unit Price']
df['Match'] = df['Check'] == df['Total Sale']
print(df['Match'].value_counts())

print(df.isnull().sum())
df.dropna(inplace=True)

employee_sales = df.groupby('Employee')['Total Sale'].sum().sort_values(ascending=False)
employee_quantity = df.groupby('Employee')['Quantity'].sum().sort_values(ascending=False)

product_quantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
product_revenue = df.groupby('Product')['Total Sale'].sum().sort_values(ascending=False)
product_avg_price = df.groupby('Product')['Unit Price'].mean().sort_values(ascending=False)

df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Total Sale'].sum().sort_values()

employee_sales.plot(kind='bar', title='Total Sales per Employee', color='orange')
plt.xlabel('Employee')
plt.ylabel('Total Sale')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

product_quantity.plot(kind='bar', title='Quantity Sold per Product', color='green')
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

monthly_revenue.plot(kind='line', title='Monthly Revenue Trend', marker='o', color='blue')
plt.xlabel('Month')
plt.ylabel('Total Sale')
plt.grid(True)
plt.tight_layout()
plt.show()

employee_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6), title='Sales Contribution per Employee')
plt.ylabel('')
plt.tight_layout()
plt.show()
