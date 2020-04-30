import requests
import pandas as pd
from pandas import read_html

# open the page with the disclaimer just to get the cookies
disclaimer = "https://flow.gassco.no/disclaimer"
disclaimerdummy = requests.get(disclaimer)

# open the actual page and use the cookies from the fake page opened before
actualpage = "https://flow.gassco.no/disclaimer/acceptDisclaimer"
actualpage2 = requests.get(actualpage, cookies=disclaimerdummy.cookies)

# store the content of the actual page in text format
actualpagetext = (actualpage2.text)

# identify relevant data sources by looking at the 'msgTable' class in the webpage code
# This is where the five tables with the realtime data can be found
gasscoflow = read_html(actualpagetext, attrs={"class": "msgTable"})

# create the dataframes for the two relevant tables
Table0 = pd.DataFrame(gasscoflow[0])
Table1 = pd.DataFrame(gasscoflow[1])
Table2 = pd.DataFrame(gasscoflow[2])
Table3 = pd.DataFrame(gasscoflow[3])
Table4 = pd.DataFrame(gasscoflow[4])

# create csv files
Table0.to_csv('./data/GsscUnplannedEventsExitTerminals.csv', index=0, encoding="ISO-8859-1")
Table1.to_csv('./data/GsscUnplannedEventsFieldsAndProcessingPlants.csv', index=0, encoding="ISO-8859-1")
Table2.to_csv('./data/GsscPlannedEventsExitTerminals.csv', index=0, encoding="ISO-8859-1")
Table3.to_csv('./data/GsscPlannedEventsFieldsAndProcessingPlants.csv', index=0, encoding="ISO-8859-1")
Table4.to_csv('./data/GsscAggregatedChangedAvailabilityFieldsAndProcessingPlants.csv', index=0, encoding="ISO-8859-1")
