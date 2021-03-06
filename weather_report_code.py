# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:26:38 2019

@author: Ayush Das
"""

import pandas as pd

dataset = pd.read_csv('country-capitals.csv')

capitalLatitude = list(dataset['CapitalLatitude'])
capitaLongitude = list(dataset['CapitalLongitude'])
countryName = list(dataset['CountryName'])
capitalName = list(dataset['CapitalName'])

import requests

source = requests.get('https://api.darksky.net/forecast/d4387196621d5db9b64386336cd76060/9.55,44.05')

source.status_code

data = source.json()

import csv

csv_file = open('weather_report.csv','w')

csv_writer = csv.writer(csv_file)

headers = ['Country','Capital','Capital_Latitude','Capital_Longitude','Timezone'] + list(data['currently'].keys())

csv_writer.writerow(headers)


for i in range(len()):
        source = requests.get('https://api.darksky.net/forecast/d4387196621d5db9b64386336cd76060/'+capitalLatitude[i]+','+str(capitaLongitude[i]))
        data = source.json()
        csv_writer.writerow([countryName[i],capitalName[i],capitalLatitude[i],capitaLongitude[i],data['timezone']]+list(data['currently'].values()))
        
csv_file.close()        