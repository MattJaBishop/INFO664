import urllib.request

#adding ?$limit= to URL helps to bypass the 1000 limit that the Socrata API has on CSV pulls by default:
url = 'https://data.cityofnewyork.us/resource/9n66-rbk3.csv?$limit=10000'
csv = urllib.request.urlopen(url).read()
with open('annualreport.csv', 'wb') as fx:
    fx.write(csv)