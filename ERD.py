#   Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  

#  Load the Dataset
df = pd.read_csv("C:\\Users\\PMYLS\\Downloads\\dataset.internship\\retail_sales_dataset.csv")
print("Column Names:", df.columns)

#   Clean the Data
df.drop_duplicates(inplace=True)           # Remove duplicates
df.dropna(inplace=True)                    # Drop missing rows
df['Date'] = pd.to_datetime(df['Date'])    # Convert 'Date' column to datetime format

#   Descriptive Statistics
print(" Descriptive Stats:")
print(df.describe())
print("Most Common Gender:", df['Gender'].mode()[0])

#  Time Series Data Prep (for line chart)
df.set_index("Date", inplace=True)
monthly_sales = df["Total Amount"].resample("ME").sum()

# VISUALIZATION part

# Bar Chart - Total Sales by Product Category
plt.figure(figsize=(10, 6))
sns.barplot(x="Product Category", y="Total Amount", data=df, estimator=sum, palette="pastel", legend=False)
plt.title("Total Sales by Product Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly Sales Trend (Line Chart)
monthly_sales = df["Total Amount"].resample("ME").sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(marker='o', linestyle='-', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
#  HEATMAP: Correlation between Numeric Columns
df.reset_index(inplace=True)  # Reset index for heatmap
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=["number"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.title(" Correlation Heatmap")
plt.tight_layout()
plt.show()

#   Final Summary in Terminal
print("\n Business Insights:")
print("1. Peak sales occur in the holiday season (Oct–Dec).")
print("2. Clothing & Beauty are top-selling product categories.")
print("3. Males slightly spend more than females.")
print("4. Target Adult and Young age groups for maximum sales.")