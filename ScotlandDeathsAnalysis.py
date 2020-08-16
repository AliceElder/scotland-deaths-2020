import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import seaborn as sns

#Load data
deaths_age_sex_csv = 'https://www.opendata.nhs.scot/dataset/5a9ecd07-fcd0-433c-94be-771eb4e0a691/resource/733aad2d-5420-4966-bc34-386a3475623f/download/deaths_hb_agesex_21072020.csv'
# For an offline version please see:  '.\\Data\\deaths_hb_agesex_21072020.csv'
deaths_hb_simd_csv = 'https://www.opendata.nhs.scot/dataset/5a9ecd07-fcd0-433c-94be-771eb4e0a691/resource/98648584-4a34-4374-832c-d3f50b6edd80/download/deaths_hb_simd_21072020.csv'
# For an offline version please see:  '.\\Data\\deaths_hb_simd_21072020.csv'

#Output files
monthly_deaths_png = '.\\Graphs\\monthly-deaths.png'
deaths_by_simd_png = '.\\Graphs\\deaths-by-simd.png'

#Load data into dataframes
df = pd.read_csv(deaths_age_sex_csv)
df = df[(df['AgeGroupQF'] == 'd') & (df['SexQF'] == 'd')]
df_simd = pd.read_csv(deaths_hb_simd_csv)

#Add Columns for more date data
formatted_dates_list = []
months_list = []
for ymd in df['WeekEnding']:
    formatted_date = datetime.strptime(str(ymd), '%Y%m%d').strftime('%m/%d/%Y')
    month = datetime.strptime(str(ymd), '%Y%m%d').strftime('%B')
    formatted_dates_list.append(formatted_date)
    months_list.append(month)
df['Formatted Date'] = formatted_dates_list
df['Month'] = months_list

#Show the number of deaths per week
df = df.groupby(['WeekEnding','Month'])[['Deaths','Average20152019']].sum().reset_index()
df['WeekEnding'] = pd.to_datetime(df['WeekEnding'], format='%Y%m%d')
df_simd['WeekEnding'] = pd.to_datetime(df_simd['WeekEnding'], format='%Y%m%d')
df_simd = df_simd.pivot_table(index='WeekEnding',columns='SIMDQuintile')['Deaths']

#Plot graph showing deaths in 2020 against deaths over the last 4 years
ax = df.plot(x='WeekEnding',y=['Deaths','Average20152019'])
ax.set(xlabel='Month', ylabel='Deaths')
plt.title('Deaths in Scotland')
ax.legend(["Deaths in 2020", "Average deaths per year 2015-2019"]);
plt.tight_layout()
ax.figure.savefig(monthly_deaths_png)
ax.clear()
plt.close(ax.figure)

#Plot a graph showing the number of deaths in 2020 by SIMD
ax = df_simd.plot()
ax.set(xlabel='Month', ylabel='Deaths')
plt.title('Deaths in Scotland by SIMD Quintile')
plt.tight_layout()
ax.figure.savefig(deaths_by_simd_png)
ax.clear()
plt.close(ax.figure)
