import pandas as pd
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_excel(r"D:\Data Analytics\Python_Excel_Project\sales_transaction.xlsx", 
                   sheet_name="Transaction_data", engine="openpyxl")

print("File loaded:", df.shape)


# Cleaning
df.columns = df.columns.str.strip().str.lower()
print("Step 1: Normalized column names:\n", df.columns)

df["category"] = df["category"].fillna("No category")
print("\nStep 2: Filled missing values in 'category':\n", df["category"].isnull().sum(), "nulls remaining")

for c in ["customer name","product","category"]:
    df[c] = df[c].astype(str).str.strip()
print("\nStep 3: Stripped whitespace from 'customer name', 'product', and 'category'.")

df["unit price"] = df["unit price"].astype(int)
print("\nStep 4: Converted 'unit price' to int:\n", df["unit price"].head())

df.drop_duplicates(inplace=True)

print("\nStep 6: Null value count after cleaning:\n",df.isnull().sum())

df['email'] = df['email'].str.replace('[at]', '@', regex=False)
print("\nStep 7: Replaced '[at]' with '@' in 'email':\n", df['email'].head())

# Analysis
print("Counts of categories:\n", df["category"].value_counts())
print("condition:/n",df[df["total price"]>15000])
print("max value:/n",df["total price"].max())
print("min value:/n",df["total price"].min())
print("\nTop 5 Product:\n", df.sort_values(by="total price", ascending=False).head(5))

# Visualization
df["total price"].plot(kind="hist", bins=10)
plt.title("Product Total Price")
plt.show()

#df["category"].value_counts().plot(kind="bar")
#plt.title("Product Total Price")
#plt.show()

df["category"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Product Count per Category")
plt.show()