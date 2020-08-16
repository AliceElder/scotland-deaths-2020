## Motivation
In the year 2020 the Coronavirus swept the globe. The disease has been detected in more than 200 countries, and there are over 5 million reported cases.

This project explores how the pandemic affected Scotland, answers the following questions:
- Has Scotland passed the peak?
- Are areas of deprivation more impacted by Coronavirus?
- Which areas have been most affected and why?

## Results
The following conclusions can be drawn from the data:
- The peak number of deaths in Scotland happened in April.
- The more deprived an area is, the more people are likely to die of coronavirus.
- There are considerably more cases in densely populated areas than in sparsely populated areas.
- There is no correlation between the land area of a concil area, and the number of cases.

An article on the results can be found [here](https://medium.com/@aliceelder/flattening-the-curve-the-impact-of-covid-19-in-scotland-85fdaa30a74c)

## Files
This project contains both a Jupyter Notebook (ScotlandDeaths2020.ipynb), and python file versions of the project (ScotlandDeathsAnalysis.py, ScotlandAreaAnalysis.py). The same content is contained in both.

## Libraries
The following libraries were used:
- pandas
- matplotlib.pyplot
- datetime
- numpy
- seaborn

## Acknowledgements
Thanks to NHS Scotland, the Scottish government, and the National Records of Scotland for providing the data for this project.

### Data Sources Used
The following data sources are used in this project:
| Data Source Name | Data Source Location | Type | URL |
|-----------|---------------|-------------|-----|
| Deaths By Health Board, Age and Sex | opendata.nhs.scot | url to live data | https://www.opendata.nhs.scot/dataset/5a9ecd07-fcd0-433c-94be-771eb4e0a691/resource/733aad2d-5420-4966-bc34-386a3475623f/download/deaths_hb_agesex_04082020.csv |
| Deaths By Deprivation | opendata.nhs.scot | url to live data | https://www.opendata.nhs.scot/dataset/5a9ecd07-fcd0-433c-94be-771eb4e0a691/resource/98648584-4a34-4374-832c-d3f50b6edd80/download/deaths_hb_simd_04082020.csv |
| Daily Case Trends By Council Area  | opendata.nhs.scot | url to live data | https://www.opendata.nhs.scot/dataset/b318bddf-a4dc-4262-971f-0ba329e09b87/resource/427f9a25-db22-4014-a3bc-893b68243055/download/trend_ca_20200810.csv |
| Land Area (based on 2011 Data Zones) | statistics.gov.scot | downloaded csv file | https://statistics.gov.scot/data/land-area-2011-data-zone-based |
| Mid-2019 Population Estimates Scotland | nrscotland.gov.uk | downloaded csv file | https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/population/population-estimates/mid-year-population-estimates/mid-2019 |

## Authors
This project was created by Alice Elder.
