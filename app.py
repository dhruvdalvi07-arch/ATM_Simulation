import numpy as np
import pandas as pd

#1. Numpy: High-speed arrays and vector math
prices = np.array([120, 250, 400, 150, 600])
discounted = prices * 0.9 #10% discount applied to all instantly!

print("=== NumPy Output ===")
print("Original Prices:", prices)
print("after 10% Discount:", discounted)
print("Average Price:", np.mean(discounted))

#2. Pandas: structed data tables (DataFrames)
data ={
    "Item": ["Earbuds", "Laptop Bags", "Monitor", "keyboard", "Desk Chair"],
    "Original_Price": prices,
    "Discounted_Price": discounted,
}

df = pd.DataFrame(data)
df["Savings"] = df["Original_Price"] - df["Discounted_Price"]

print("\n=== Pandas DataFrame ===")
print(df)
