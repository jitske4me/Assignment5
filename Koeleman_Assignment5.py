# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:51:12 2018

@author: Jitske
"""


import json
import csv

with open('conflict_data_full_lined.json') as file:
    conflict_data = json.load(file)

for entry in range(len(conflict_data)):
    info[entry][]



"""
Need:
    id
    relid
    year
    conflict_name
    side_a
    side_b
    source_article
    latitude
    longitude
    country
    region
    date_start
    date_end
    deaths_a
    deaths_b
"""




with open('conflict_data_full_lined.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerows(conflict_data)