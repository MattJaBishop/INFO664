import urllib.request

url = 'https://data.cityofnewyork.us/resource/9n66-rbk3.csv'
csv = urllib.request.urlopen(url).read()
with open('annualreport.csv', 'wb') as fx:
    fx.write(csv)