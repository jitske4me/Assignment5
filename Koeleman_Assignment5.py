# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:51:12 2018

@author: Jitske
"""

## Import JSON and CSV Package 
import json
import csv

## Load in the data 
with open('conflict_data_full_lined.json') as file:
    conflict_data = json.load(file)


## Make empty sets to see who the actors are (so we know how the US is identified)
unique_side_a = set()
unique_side_b = set()

## Make empty list to add the data we want to analyze in R to
conflict_data_Iraq = []
for entry in range(len(conflict_data)):
    
    ## We only want the conflicts in Iraq
    if conflict_data[entry]['country'] == 'Iraq':
        
        ## Add side a/b to the set 
        unique_side_a.add(conflict_data[entry]['side_a'])
        unique_side_b.add(conflict_data[entry]['side_b'])
        
        
        ## Make a list of lists
        ## [year,conflict_name, side_a] etc
        ## Only if the US was an actor 
        #if conflict_data[entry]['side_a'] == 'Australia, United Kingdom, United States of America':
        conflict_data_Iraq += [[conflict_data[entry]['year'], 
                               conflict_data[entry]['conflict_name'],
                               conflict_data[entry]['side_a'],
                               conflict_data[entry]['side_b'],
                               #conflict_data[entry]['source_article'],
                               conflict_data[entry]['latitude'],
                               conflict_data[entry]['longitude'],
                               conflict_data[entry]['country'],
                               conflict_data[entry]['deaths_a'],
                               conflict_data[entry]['deaths_b']
                               ]]



## Open the output CSV file we want to write to
with open('preprocessed_conflict_data.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['year', 
                        'conflict_name', 
                        'side_a', 
                        'side_b', 
                        'latitude',
                        'longitude',
                        'country',
                        'deaths_a',
                        'deaths_b'])
    for sublist in range(len(conflict_data_Iraq)):
        csvwriter.writerow(conflict_data_Iraq[sublist])
    
    # Actually write the data to the CSV file here.
    # You can use the same csvwriter.writerow command to output the data 
    #   as is used above to output the headers.

"""
Need:
    year
    conflict_name
    side_a
    side_b
    #source_article
    latitude
    longitude
    country
    #date_start
    #date_end
    deaths_a
    deaths_b
"""

