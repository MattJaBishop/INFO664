import urllib.request

url = 'https://data.cityofnewyork.us/resource/jty7-wc2y.csv'
csv = urllib.request.urlopen(url).read()
with open('servicelocations.csv', 'wb') as fx:
    fx.write(csv)