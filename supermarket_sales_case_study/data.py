import pandas as pd
import numpy as np

df = pd.read_csv("supermarket.csv")
print(df.shape) 
# df.head()
# (8631, 17)
# df.info()
#print(df.isnull().sum())
# audit = pd.DataFrame({
#     "missing_count": df.isnull().sum(),
#     "missing_percent": (df.isnull().mean() * 100).round(2),
# })
# print(audit[audit.missing_count > 0])
# print("exact duplicate rows:", df.duplicated().sum())   # 150
# audit.head()


# rows_in = len(df)
# df = df.drop_duplicates()

# df["quantity_clean"] = pd.to_numeric(df["Quantity"], errors="coerce")
# df["unit_price_clean"] = pd.to_numeric(df["Unit price"], errors="coerce")
# df["order_date"] = pd.to_datetime(df["Date"], errors="coerce")

# # stores = pd.read_csv("supermarket.csv")
# # canonical = {name.strip().lower(): name for name in stores["store_name"]}
# # df["store_name_clean"] = df["store_name"].str.strip().str.lower().map(canonical)
# # print("unmapped store names:", df["store_name_clean"].isna().sum())

# #(8631, 17)








