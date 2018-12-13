import requests
from sodapy import Socrata
import csv
#import urllib.request

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
	"pOrwgowOicplQPUkBKEQLfDPN",
	username="mattjabishop@gmail.com",
	password="beDZ5@na")

#client = Socrata("https://data.cityofnewyork.us/resource/xy49-4pwd.csv", None)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("9n66-rbk3", limit=10000)

# This bit of code will write the result of the query to testoutput.csv

with open('testoutput.csv', 'wb') as fx:
    fx.write(csv)

#with open('testoutput.csv', 'wb') as file:
#	filewriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)