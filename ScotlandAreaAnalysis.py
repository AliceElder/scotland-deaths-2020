import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as dates
import numpy as np
import seaborn as sns

#Load data
cases_ca = 'https://www.opendata.nhs.scot/dataset/b318bddf-a4dc-4262-971f-0ba329e09b87/resource/427f9a25-db22-4014-a3bc-893b68243055/download/trend_ca_20200809.csv'
pop_density_ca = '.\\Data\\mid-year-pop-est-19-time-series-2_1981-2019.csv'
land_area_ca = '.\\Data\\land_area_ca_2014.csv'

#Output files
cases_by_area_png = '.\\Graphs\\cases-by-area.png'
cases_by_area_labelled_png = '.\\Graphs\\cases-by-area-labelled.png'

#Load data into dataframes
df_cases = pd.read_csv(cases_ca)
df_cases = df_cases[['CA','CumulativePositive','CumulativeDeaths']]
df_cases_pivot = df_cases.groupby(['CA']).max()

df_popdensity = pd.read_csv(pop_density_ca, skiprows = 2, nrows=35, thousands=',')
df_popdensity.dropna(how="all", inplace=True)
df_popdensity = df_popdensity[['Code','Persons','2019']]
df_popdensity.rename(columns={"Persons": "CouncilArea", "Code": "CA", "2019": "PopDensity"}, inplace=True)
df_popdensity['PopDensity'] = df_popdensity['PopDensity'].astype(int)

df_landarea = pd.read_csv(land_area_ca)
df_landarea = df_landarea[['FeatureCode','Value']]
df_landarea.rename(columns={"FeatureCode": "CA", "Value": "LandArea"}, inplace=True)

#Combine into one dataframe
df_combined_pd = pd.merge(df_popdensity, df_cases_pivot, on='CA')
df_combined_pd = pd.merge(df_combined_pd, df_landarea, on='CA')
#print(df_combined_pd)

#Plot Graphs
ax = sns.scatterplot(x='CumulativePositive', y='PopDensity', data=df_combined_pd, size='LandArea', hue='CouncilArea', sizes=(10, 2000), alpha=0.4, legend=False)
ax.set(ylim=(0, 700000),xlim=(0, 3000),xlabel='Number of Cases', ylabel='Population Density')
plt.title('Number of Cases by Council Area')
plt.tight_layout()
ax.figure.savefig(cases_by_area_png)
#plt.show()

for line in df_combined_pd.index:
    if (df_combined_pd.CouncilArea[line] == 'Glasgow City' or df_combined_pd.CouncilArea[line] == 'Highland'):
        ax.text(df_combined_pd.CumulativePositive[line], df_combined_pd.PopDensity[line], df_combined_pd.CouncilArea[line], ha='right', va='center', size='small', color='black')
ax.figure.savefig(cases_by_area_labelled_png)
ax.clear()
plt.close(ax.figure)

#Glasgow v Highlands
df_GLA_HIG = df_combined_pd[['CouncilArea','CumulativePositive', 'PopDensity', 'LandArea']]
df_GLA_HIG = df_GLA_HIG.loc[(df_GLA_HIG['CouncilArea'] == 'Glasgow City') | (df_GLA_HIG['CouncilArea'] == 'Highland')]
print(df_GLA_HIG)
