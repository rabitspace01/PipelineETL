import pandas as pd


sales_df = pd.read_csv("transformed_sales_data.csv")
marketing_df = pd.read_csv("transformed_marketing_data.csv")

#ver ventas
print("Sales Data:")
print(sales_df.head())

#ver marketing
print("\nMarketing Data:")
print(marketing_df.head())

