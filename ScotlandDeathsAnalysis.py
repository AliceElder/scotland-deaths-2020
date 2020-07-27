import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as dates

deaths_age_sex_csv = '.\\Data\\deaths_hb_agesex_21072020.csv'

original_df = pd.read_csv(deaths_age_sex_csv)
df = original_df[(original_df['AgeGroupQF'] == 'd') & (original_df['SexQF'] == 'd')]

#Add Columns for more date data
prev_month = ''
week_number = 0
formatted_dates_list = []
months_list = []
week_numbers = []
for ymd in df['WeekEnding']:
    formatted_date = datetime.strptime(str(ymd), '%Y%m%d').strftime('%m/%d/%Y')
    month = datetime.strptime(str(ymd), '%Y%m%d').strftime('%B')
    formatted_dates_list.append(formatted_date)
    months_list.append(month)

df['Formatted Date'] = formatted_dates_list
df['Month'] = months_list


df = df.groupby(['WeekEnding','Month'])['Deaths','Average20152019'].sum().reset_index()

df['WeekEnding'] = pd.to_datetime(df['WeekEnding'], format='%Y%m%d')

print(df)

ax = df.plot(x='WeekEnding',y=['Deaths','Average20152019'])
ax.set(xlabel='Month', ylabel='Deaths')
plt.show()
