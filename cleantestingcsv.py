import pandas as pd

#Creates function to truncate zip codes to 5 digits:
def truncate_zip(val):
    return val[:5]
data = pd.read_csv('testinglocations.csv', converters={'zip_code': truncate_zip})

#Drops rows with no borough names:
data = data.dropna(subset=['borough'])

#Renames address column title to street:
data = data.rename(columns = {'address':'street'})

#Converts first letters of each word to uppercase in borough names:
data['borough'] = data['borough'].str.title()

data.to_csv('testinglocationsclean.csv', encoding='utf-8')