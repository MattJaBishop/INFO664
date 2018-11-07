import csv

PopulationData = []

with open('New_York_City_Population_by_Borough__1950_-_2040.csv', 'r') as f:
	reader = csv.DictReader(f)
	for row in reader:
		PopulationData.append(row)

for a in PopulationData:
	print(a)

for a in PopulationData:
	print(a.keys())

def readable_format(PopulationData):
	for a in PopulationData:
		for key, value in a.items():
			print(key + ": ", value)
		print('\n')

readable_format(PopulationData)