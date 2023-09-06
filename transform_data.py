import pandas as pd

sales_df = pd.read_csv("sales_data.csv")
marketing_df = pd.read_csv("marketing_data.csv")

print("Sales Data:")
print(sales_df.head())

print("\nMarketing Data:")
print(marketing_df.head())

sales_df.dropna(inplace=True)
marketing_df.dropna(inplace=True)

sales_df["month"] = pd.to_datetime(sales_df["date"]).dt.to_period("M")
marketing_df["month"] = pd.to_datetime(marketing_df["date"]).dt.to_period("M")

marketing_df["ROI"] = marketing_df["conversions"] / marketing_df["clicks"]

sales_df.to_csv("transformed_sales_data.csv", index=False)
marketing_df.to_csv("transformed_marketing_data.csv", index=False)

sales_df = pd.read_csv("sales_data.csv")
