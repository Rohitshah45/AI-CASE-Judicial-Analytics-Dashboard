import pandas as pd

df = pd.read_csv("cases_2018.csv")

print("Rows:", len(df))
print("Pending:", df['date_of_decision'].isna().sum())
print("Disposed:", df['date_of_decision'].notna().sum())
pending = df[df['date_of_decision'].isna()]

state_summary = (
    pending.groupby('state_code')
    .size()
    .reset_index(name='pending_cases')
)

state_summary.to_csv('state_summary.csv', index=False)


print(state_summary.head())

district_summary = (
    pending.groupby(['state_code','dist_code'])
    .size()
    .reset_index(name='pending_cases')
)

district_summary.to_csv('district_summary.csv', index=False)

print("District Summary Created")
court_summary = (
    pending.groupby('judge_position')
    .size()
    .reset_index(name='pending_cases')
    .sort_values('pending_cases', ascending=False)
)

court_summary.to_csv('court_summary.csv', index=False)

print("Court Summary Created")
print(court_summary.head())