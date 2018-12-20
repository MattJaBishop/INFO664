import pandas as pd

data = pd.read_csv('servicelocations.csv')

#Drops rows with no borough names:
data = data.dropna(subset = ['borough'])

#Renames address column title to street:
data = data.rename(columns = {'address':'street', 'address_2':'street 2', 'facilityname':'facility_name', 'zipcode':'zip_code', '_2010_census_tract':'2010_census_tract', 'phone':'phone_number'})

#Converts first letters of each word to uppercase in borough names:
data['borough'] = data['borough'].str.title()

data.to_csv('servicelocationsclean.csv', encoding='utf-8')