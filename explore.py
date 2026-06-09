import pandas as pd

df = pd.read_csv("cases_2018.csv")

print(sorted(df['state_code'].unique()))
