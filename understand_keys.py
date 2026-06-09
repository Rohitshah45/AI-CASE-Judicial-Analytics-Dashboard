import pandas as pd

state = pd.read_csv("cases_state_key.csv")
district = pd.read_csv("cases_district_key.csv")

print(state.head())
print("\n")
print(district.head())
print("\nState Columns:")
print(state.columns)

print("\nDistrict Columns:")
print(district.columns)