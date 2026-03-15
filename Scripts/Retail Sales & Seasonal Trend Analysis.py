# ===============================================================
# Retail Sales & Seasonal Trend Analysis
# Author: Hrishikesh Murudkar
#
# Description:
# This project analyzes retail and warehouse sales data to
# identify seasonal trends, product performance, and supplier
# contributions. The analysis includes data exploration,
# visualization, and key business insights.
#
# Tools Used:
# Python, Pandas, NumPy, Matplotlib, Seaborn
# ===============================================================


# =========================
# 1. Import Libraries
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# 2. Load Dataset
# =========================

df = pd.read_csv("Retail & Warehouse Sales_Cleaned.csv")

print("\nFirst 5 Rows:")
print(df.head())


# =========================
# 3. Dataset Overview
# =========================

print("\nDataset Shape:", df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# =========================
# 4. Data Quality Check
# =========================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# =========================
# 5. Feature Engineering
# =========================

# Create Quarter column from Month
df['Quarter'] = (df['MONTH'] - 1) // 3 + 1

print("\nUpdated Dataset Preview:")
print(df.head())


# =========================
# 6. Monthly Sales Trend
# =========================

monthly_sales = df.groupby('MONTH')['TOTAL_SALES'].sum()

plt.figure(figsize=(8,5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()


# =========================
# 7. Sales by Item Type
# =========================

item_sales = df.groupby('ITEM_TYPE')['TOTAL_SALES'].sum().sort_values()

plt.figure(figsize=(8,5))
item_sales.plot(kind='bar')

plt.title("Total Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Sales")

plt.show()


# =========================
# 8. Top 10 Suppliers
# =========================

top_suppliers = df.groupby('SUPPLIER')['TOTAL_SALES'].sum() \
                  .sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
top_suppliers.plot(kind='bar')

plt.title("Top 10 Suppliers by Total Sales")
plt.xlabel("Supplier")
plt.ylabel("Total Sales")

plt.show()


# =========================
# 9. Retail vs Warehouse Sales
# =========================

sales_channels = df[['RETAIL_SALES','WAREHOUSE_SALES']].sum()

plt.figure(figsize=(6,4))
sales_channels.plot(kind='bar')

plt.title("Retail vs Warehouse Sales Comparison")
plt.ylabel("Sales Value")

plt.show()


# =========================
# 10. Quarterly Sales Trend
# =========================

quarter_sales = df.groupby('Quarter')['TOTAL_SALES'].sum()

plt.figure(figsize=(8,5))
quarter_sales.plot(kind='bar')

plt.title("Quarterly Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")

plt.show()


# =========================
# 11. Heatmap Analysis
# =========================

pivot_table = df.pivot_table(
    values='TOTAL_SALES',
    index='ITEM_TYPE',
    columns='MONTH',
    aggfunc='sum'
)

plt.figure(figsize=(10,6))
sns.heatmap(pivot_table, cmap='coolwarm')

plt.title("Sales Heatmap by Item Type and Month")

plt.show()


# =========================
# 12. Key Insights
# =========================

print("\n================ KEY INSIGHTS ================\n")

# Highest sales month
highest_sales_month = df.groupby('MONTH')['TOTAL_SALES'].sum().idxmax()
print(f"• The month with the highest sales is Month {highest_sales_month}.")

# Top product category
top_category = df.groupby('ITEM_TYPE')['TOTAL_SALES'].sum().idxmax()
print(f"• The top performing product category is: {top_category}.")

# Top supplier
top_supplier = df.groupby('SUPPLIER')['TOTAL_SALES'].sum().idxmax()
print(f"• The supplier contributing the highest sales is: {top_supplier}.")

# Sales channel comparison
sales_channels = df[['RETAIL_SALES','WAREHOUSE_SALES']].sum()

if sales_channels['RETAIL_SALES'] > sales_channels['WAREHOUSE_SALES']:
    print("• Retail sales contribute more to overall revenue than warehouse sales.")
else:
    print("• Warehouse sales contribute more to overall revenue than retail sales.")


# =========================
# 13. Conclusion
# =========================

print("\n================ CONCLUSION ================\n")

print("This project analyzed retail and warehouse sales data to identify trends, seasonal patterns, and key contributors to revenue.")

print("The analysis highlighted the months with peak sales, the most profitable product categories, and the suppliers contributing significantly to overall sales.")

print("Such insights help businesses improve inventory planning, strengthen supplier relationships, and align marketing strategies with high-demand periods.")


# =========================
# 14. Business Insights
# =========================

print("\n================ BUSINESS INSIGHTS ================\n")

total_sales = df['TOTAL_SALES'].sum()
print("Total Sales:", round(total_sales,2))

monthly_sales = df.groupby('MONTH')['TOTAL_SALES'].sum()
print("\nMonthly Sales Summary:")
print(round(monthly_sales,2))

category_sales = df.groupby('ITEM_TYPE')['TOTAL_SALES'].sum()
print("\nSales by Product Category:")
print(round(category_sales,2))

top_products = df.groupby('ITEM_DESCRIPTION')['TOTAL_SALES'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products by Sales:")
print(round(top_products,2))