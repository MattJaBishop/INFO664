import urllib.request

url = 'https://data.cityofnewyork.us/resource/fqke-ix7c.csv'
csv = urllib.request.urlopen(url).read()
with open('testinglocations.csv', 'wb') as fx:
    fx.write(csv)