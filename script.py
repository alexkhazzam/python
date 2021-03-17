import sqlite3
import csv
import json
import copy

populatedTable = []


with open('people.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')

    with open('state_to_region.json') as f:
        data = json.load(f)

    def trimElements(l):
        for el in range(0, len(l)):
            l[el] = l[el].strip()
        return copy.deepcopy(l)

    elPos = 0
    for row in readcsv:
        while(len(row) != 5):
            row.append('None')
        for el in range(0, len(trimElements(row))):
            if (elPos != 0):  # No need to loop through header row
                if (row[el] in data.keys()):
                    row[3] = row[el]
                    row[3 + 1] = data[row[el]]
                elif (row[el] == '' or row[el] == 'None'):
                    # Note that None is the same as leaving the cell blank; this is simply for readability purposes
                    row[el] = 'None'
            else:
                break
        elPos += 1
        populatedTable.append(row)

with open('populated-people.csv', 'w') as csvfile:
    csvriter = csv.writer(csvfile)
    for row in populatedTable:
        csvriter.writerow(row)
