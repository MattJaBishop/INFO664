# NYC HIV/AIDS Resources Dashboard
## Final Project for Pratt Institute's Programming for Cultural Heritage Course

Project Overview

This dashboard includes facts and figures related to NYC HIV/AIDS data available through NYC Open Data. This dashboard also includes charts that provide location and contact information for HIV testing sites and HIV/AIDS services locations across the city's five boroughs. The facts and figures are only available for the years 2011 through 2015 through NYC Open Data: more recent data has not yet been digitized in a scrapable format (PDF documents exist for them, but I hope to pull that data once it becomes available through NYC Open Data).


Process

Data was first pulled from NYC Open Data through a call to the Socrata API. Three CSV files were pulled:

- DOHMH HIV/AIDS Annual Report: https://data.cityofnewyork.us/Health/DOHMH-HIV-AIDS-Annual-Report/fju2-rdad

- HIV Testing Locations: https://data.cityofnewyork.us/Health/HIV-Testing-Locations/72ss-25qh

- DOHMH HIV Service Directory: https://data.cityofnewyork.us/dataset/DOHMH-HIV-Service-Directory/pwts-g83w

Data was next cleaned using the Pandas library through various functions. Once cleaned, new CSV Files were created and then pulled into Microsoft Power BI to be visualized. The completed visualization was then included as a link on a WordPress site (when I get a paid version of this WordPress site, I will embed it using the iframe plugin).

Link to WordPress site: https://mattjabishop.wordpress.com/2018/12/19/nyc-hiv-aids-service-and-facts-dashboard/

Link to dashboard: https://app.powerbi.com/view?r=eyJrIjoiZjk1ZjJhODYtODgxOS00NTlkLTllZDUtOWRhZTdlYTkzNzQ4IiwidCI6ImVmYTRjNzcwLTM2NzgtNDA3MS05YWZhLWNjMzFmMDg2MWVkZCIsImMiOjZ9
(Please note that a proper dashboard title is only included on the WordPress site: my intention was to have it embedded rather than linked, and the linked dashboard would be too small to view with a noticeable title included there.)


Tools

- Python Libraries:
	- urllib.request: Extensible library for opening URLs.
	- Pandas: Python data analysis library.

- Microsoft Power BI: Data visualization software with free and paid versions.

- WordPress: A free and open-source content management system (CMS) for hosting web content.

- Sublime Text: Text editor used to create my python scripts.


Notes for those running and editing files:

The RunProgram.py file will run all other Python files (pulling new CSV files and cleaning them). Opening NYCHIVServicesDashboard.pbix in the most recent version of Power BI Desktop and hitting the refresh button will call the most currently created clean CSV files that RunProgram.py produced. Also, please be aware that servicelocations.csv and testinglocations.csv are the pre-cleaned versions of those files - annualreport.csv was clean from the beginning.