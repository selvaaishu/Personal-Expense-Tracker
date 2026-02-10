import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders if not exist
os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv(r"C:\Users\Reference\Downloads\dataset\personal_expense_dataset.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# Check missing values
print("\nMissing values:\n", df.isnull().sum())

# Expense columns (based on your dataset)
expense_cols = ["Food", "Groceries", "Transport", "Entertainment", "Shopping",
                "Rent", "Bills", "Healthcare", "Education"]

# Total expense by category
category_totals = df[expense_cols].sum().sort_values(ascending=False)

print("\nTotal Spending by Category:\n", category_totals)

# Chart 1: Bar chart (Category totals)
plt.figure(figsize=(10,5))
category_totals.plot(kind="bar")
plt.title("Total Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("visualizations/category_spending.png")
plt.show()

# Total expense per month (Year + Month)
df["YearMonth"] = df["Year"].astype(str) + "-" + df["Month"].astype(str)

monthly_totals = df.groupby("YearMonth")["Total_Exp"].sum()

print("\nMonthly Total Expenses:\n", monthly_totals)

# Chart 2: Line chart (Monthly expenses)
plt.figure(figsize=(10,5))
monthly_totals.plot(kind="line", marker="o")
plt.title("Monthly Total Expenses Trend")
plt.xlabel("Month")
plt.ylabel("Total Expense")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/monthly_expenses.png")
plt.show()

# Insights
highest_category = category_totals.index[0]
highest_value = category_totals.iloc[0]

print("\nINSIGHTS:")
print(f"1. Highest spending category is {highest_category} with total {highest_value:.2f}")
print(f"2. Month with highest spending is {monthly_totals.idxmax()} with {monthly_totals.max():.2f}")
print(f"3. Average monthly spending: {monthly_totals.mean():.2f}")
