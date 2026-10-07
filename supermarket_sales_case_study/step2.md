import pandas as pd
import numpy as np

df = pd.read_csv("supermarket.csv")
print(df.shape) 

# df.head()
# (8631, 17)
df.info()

```txt
#  #   Column                   Non-Null Count  Dtype  
# ---  ------                   --------------  -----  
#  0   Invoice ID               8631 non-null   str    
#  1   Branch                   8631 non-null   str    
#  2   City                     8631 non-null   str    
#  3   Customer type            8567 non-null   str    
#  4   Gender                   8631 non-null   str    
#  5   Product line             8631 non-null   str    
#  6   Unit price               8631 non-null   float64
#  7   Quantity                 8631 non-null   int64  
#  8   Tax 5%                   8631 non-null   float64
#  9   Total                    8631 non-null   float64
#  10  Date                     8614 non-null   str    
#  11  Time                     8631 non-null   str    
#  12  Payment                  8631 non-null   str    
#  13  cogs                     8631 non-null   float64
#  14  gross margin percentage  8631 non-null   float64
#  15  gross income             8631 non-null   float64
#  16  Rating                   8543 non-null   float64

```