# =====================================================
# IMPORT LIBRARIES
# =====================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# LOAD DATASET
# =====================================================
df = pd.read_excel("retail_sales_100_rows (1).xlsx")

print("\n--- DATASET PREVIEW ---")
print(df.head())

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# =====================================================
# NUMPY ARRAY CREATION FROM DATASET
# =====================================================
quantity = np.array(df['Quantity'])
price = np.array(df['Price'])
sales = np.array(df['Total_Sales'])

print("\n--- NUMPY ARRAYS ---")
print("Quantity:", quantity[:5])
print("Price:", price[:5])
print("Sales:", sales[:5])

# =====================================================
# ARRAY CREATION METHODS (PPT COVERED)
# =====================================================
print("\n--- ARRAY CREATION METHODS ---")

arr_list = np.array([10, 20, 30])
print("Using list:", arr_list)

print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))
print("Arange:", np.arange(1, 10, 2))
print("Linspace:", np.linspace(1, 10, 5))
print("Logspace:", np.logspace(1, 3, 5))
print("Random:", np.random.rand(5))
print("Empty:", np.empty(5))

# =====================================================
# MATHEMATICAL OPERATIONS (ON DATASET)
# =====================================================
print("\n--- MATHEMATICAL OPERATIONS ---")

print("Addition (Quantity + Price):", quantity + price)
print("Subtraction (Price - Quantity):", price - quantity)
print("Multiplication (Quantity * Price):", quantity * price)
print("Division (Sales / Quantity):", sales / quantity)

# =====================================================
# NUMPY FUNCTIONS
# =====================================================
print("\n--- NUMPY FUNCTIONS ---")

print("Total Sales:", np.sum(sales))
print("Product of Quantities:", np.prod(quantity))
print("Min Sales:", np.min(sales))
print("Max Sales:", np.max(sales))
print("Sorted Sales:", np.sort(sales))

# =====================================================
# STATISTICAL OPERATIONS
# =====================================================
print("\n--- STATISTICAL ANALYSIS ---")

print("Mean:", np.mean(sales))
print("Median:", np.median(sales))
print("Standard Deviation:", np.std(sales))
print("Variance:", np.var(sales))

# =====================================================
# POWER & ROOT
# =====================================================
print("\n--- POWER & ROOT ---")

print("Square Root of Sales:", np.sqrt(sales))
print("Square of Quantity:", np.power(quantity, 2))

# =====================================================
# TRIGONOMETRIC FUNCTIONS
# =====================================================
print("\n--- TRIGONOMETRIC ---")

print("Sin:", np.sin(quantity))
print("Cos:", np.cos(quantity))
print("Tan:", np.tan(quantity))

# =====================================================
# COMPARISON OPERATIONS
# =====================================================
print("\n--- COMPARISON ---")

print("Sales > 500:", sales > 500)
print("Sales < 200:", sales < 200)
print("Sales == 300:", sales == 300)

# =====================================================
# LOGICAL OPERATIONS
# =====================================================
print("\n--- LOGICAL ---")

cond1 = sales > 200
cond2 = sales < 800

print("AND:", np.logical_and(cond1, cond2))
print("OR:", np.logical_or(cond1, cond2))
print("NOT:", np.logical_not(cond1))

# =====================================================
# INDEXING & SLICING
# =====================================================
print("\n--- INDEXING ---")

print("First 5 Sales:", sales[:5])
print("Last 5 Sales:", sales[-5:])
print("Every 2nd Value:", sales[::2])

# =====================================================
# RESHAPING
# =====================================================
print("\n--- RESHAPING ---")

reshaped = sales.reshape(20, 5)
print("Reshaped Array:\n", reshaped)

# =====================================================
# AXIS OPERATIONS
# =====================================================
print("\n--- AXIS OPERATIONS ---")

print("Row-wise Sum:", np.sum(reshaped, axis=1))
print("Column-wise Sum:", np.sum(reshaped, axis=0))

# =====================================================
# PANDAS DATA HANDLING
# =====================================================
print("\n--- PANDAS OPERATIONS ---")

print("Dataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nUnique Categories:")
print(df['Category'].unique())

# Groupby
category_sales = df.groupby('Category')['Total_Sales'].sum()
city_sales = df.groupby('City')['Total_Sales'].sum()
payment_sales = df.groupby('Payment_Mode')['Total_Sales'].sum()

print("\nCategory Sales:\n", category_sales)
print("\nCity Sales:\n", city_sales)
print("\nPayment Sales:\n", payment_sales)

# =====================================================
# SORTING & FILTERING
# =====================================================
print("\n--- SORTING & FILTERING ---")

sorted_df = df.sort_values(by='Total_Sales', ascending=False)
print("Top 10 Sales:\n", sorted_df.head(10))

high_sales = df[df['Total_Sales'] > 500]
print("\nHigh Sales (>500):\n", high_sales)

# =====================================================
# FEATURE ENGINEERING
# =====================================================
print("\n--- FEATURE ENGINEERING ---")

df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

print("Monthly Sales:\n", monthly_sales)

# =====================================================
# PIVOT TABLE
# =====================================================
print("\n--- PIVOT TABLE ---")

df['Month'] = df['Date'].dt.month

category_sales = df.groupby('Category')['Total_Sales'].sum()
city_sales = df.groupby('City')['Total_Sales'].sum()
payment_sales = df.groupby('Payment_Mode')['Total_Sales'].sum()
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)


# =====================================================
# CORRELATION
# =====================================================
print("\n--- CORRELATION ---")

print(df.corr(numeric_only=True))

# =====================================================
# VISUALIZATION
# =====================================================

# ==========================================
# 1. TOP 10 PRODUCTS (BAR CHART)
# ==========================================
plt.figure()
product_sales.head(10).plot(kind='bar')
plt.title("Top 10 Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# ==========================================
# 2. SALES DISTRIBUTION (HISTOGRAM)
# ==========================================
plt.figure()
plt.hist(df['Total_Sales'], bins=10)
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()

# ==========================================
# 3. PRICE VS SALES (SCATTER PLOT)
# ==========================================
plt.figure()
plt.scatter(df['Price'], df['Total_Sales'])
plt.title("Price vs Total Sales")
plt.xlabel("Price")
plt.ylabel("Total Sales")
plt.show()


# =====================================================
print("\n✅ ALL OPERATIONS COMPLETED SUCCESSFULLY")
# =====================================================
