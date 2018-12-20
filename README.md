# NYC HIV/AIDS Resource Dashboard
## Final Project for Pratt Institute's Programming for Cultural Heritage Course

Project Overview

This dashboard includes facts and figures related to HIV/AIDS data available through NYC Open Data. This dashboard also includes charts that provide location and contact information for HIV testing sites and HIV/AIDS services locations across the city's five boroughs. The facts and figures are only available for the years 2011 through 2015 through NYC Open Data: more recent data has not yet been digitized in a scrapable format (PDF documents exist for them, but I hope to pull that data once it becomes available through NYC Open Data).


Process

Data was first pulled from NYC Open Data through a call to the Socrata API. Three CSV files were pulled:

- DOHMH HIV/AIDS Annual Report: https://data.cityofnewyork.us/Health/DOHMH-HIV-AIDS-Annual-Report/fju2-rdad

- HIV Testing Locations: https://data.cityofnewyork.us/Health/HIV-Testing-Locations/72ss-25qh

- DOHMH HIV Service Directory: https://data.cityofnewyork.us/dataset/DOHMH-HIV-Service-Directory/pwts-g83w

Data was next cleaned using the Pandas library through various functions. Once cleaned, new CSV Files were created and then pulled into Microsoft Power BI to be visualized. The completed visualization was then embedded into a WordPress site, which can be found here here: 


Tools

- Python Libraries:
	- urllib.request: Extensible library for opening URLs.
	- Pandas: Python data analysis library.

- Microsoft Power BI: Data visualization software with free and paid versions.

- WordPress: A free and open-source content management system (CMS) for hosting web content.


Notes for those running and editing files:

The RunProgram.py file will run all other Python files (pulling new CSV files and cleaning them). Opening the the NYCHIVServicesDashboard.pbix in the most recent version of Power BI Desktop and hitting the refresh button will call the most currently created clean CSV files that RunProgram.py produced. Also, please be aware that servicelocations.csv and testinglocations.csv are the pre-cleaned versions of those files - annualreport.csv was clean from the beginning.