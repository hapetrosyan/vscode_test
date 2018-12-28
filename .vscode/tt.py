import pandas as pd



df = pd.DataFrame(columns=['open', 'close'])

df = df.append({'open': 1, 'close': 2}, ignore_index=True)

print(df)