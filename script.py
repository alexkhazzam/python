import csv
import copy
import json

with open('people.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    with open('state_to_region.json') as f:
        data = json.load(f)
