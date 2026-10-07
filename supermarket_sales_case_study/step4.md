import pandas as pd
import numpy as np

df = pd.read_csv("supermarket.csv")
print(df.shape) 
# df.head()
# (8631, 17)
# df.info()

#print(df.isnull().sum())
audit = pd.DataFrame({
    "missing_count": df.isnull().sum(),
    "missing_percent": (df.isnull().mean() * 100).round(2),
})
print(audit[audit.missing_count > 0])
print("exact duplicate rows:", df.duplicated().sum())   # 150
audit.head()


```txt

(8631, 17)
               missing_count  missing_percent
Customer type             64             0.74
Date                      17             0.20
Rating                    88             1.02
exact duplicate rows: 30

```
