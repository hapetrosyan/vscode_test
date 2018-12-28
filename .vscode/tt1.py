
import datetime
import pandas as pd
import numpy as np

todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')

columns = ['A','B', 'C']

df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0) # with 0s rather than NaNs
data = np.array([np.arange(10)]*3).T
df = pd.DataFrame(data, index=index, columns=columns)

print(df)