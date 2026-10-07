import pandas as pd
import numpy as np

df = pd.read_csv("supermarket.csv")
print(df.shape) 
# df.head()
# (8631, 17)
# df.info()
print(df.isnull().sum())

```txt
# (8631, 17)
# Invoice ID                  0
# Branch                      0
# City                        0
# Customer type              64
# Gender                      0
# Product line                0
# Unit price                  0
# Quantity                    0
# Tax 5%                      0
# Total                       0
# Date                       17
# Time                        0
# Payment                     0
# cogs                        0
# gross margin percentage     0
# gross income                0
# Rating                     88
# dtype: int64

``
