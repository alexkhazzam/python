import sqlite3
import csv
import json
import copy

editedLists = []

#Populating "Region" cell before storing in database (NOT required)****************#


def trimList(list):
    for i in range(0, len(list)):
        list[i] = list[i].strip()
    return list


with open('people.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')

    with open('state_to_region.json') as f:
        data = json.load(f)

    rPos = 4
    sPos = 3

    elPos = 0
    for l in readcsv:
        l = trimList(l)

        def regionExists(pos=3):
            return (l[pos] in data.keys())

        if (len(l) == 5 and elPos != 0):  # No need to check region for first row (header section)
            if (regionExists() and (l[rPos] == '')):
                l[rPos] = data[l[sPos]]
        else:
            while(len(l) != 5):
                # Note that NULL is the same as leaving the cell blank; this is simply for readability purposes
                l.append('NULL')
            for i in range(0, len(l)):
                def nullifyEl():
                    l[i] = 'NULL'

                if (regionExists(i)):
                    l[rPos] = data[l[i]]
                    l[sPos] = l[i]
                    nullifyEl()
                    break
                if (l[i] == ''):
                    nullifyEl()

        elPos += 1
        editedLists.append(l)

with open('people.csv', 'w') as csvfile:
    csvriter = csv.writer(csvfile)
    for i in editedLists:
        csvriter.writerow(i)
