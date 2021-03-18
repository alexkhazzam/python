import csv
import json
import copy

populatedTable = []


with open('people.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')

    with open('state_to_region.json') as f:
        data = json.load(f)

    def trimElements(r):
        def helper(el):
            r[el] = r[el].strip()
        rangeLoop(r, helper)
        return r

    def populateRowWithPlaceholders(r):
        return r + (['None'] * (5 - len(r)))  # Instead of while loop

    def fetchStatePosition(r):
        pos = None
        # Would be too confusing to use rangeLoop() as a helper function here
        for el in range(0, len(r)):
            if (r[el] in data.keys()):
                pos = el
                break
        return pos

    def populateRegion(r, p):
        r[3] = r[p]
        r[4] = data[r[p]]
        return r

    def populateEmptyStrings(r):
        def helper(el):
            if (r[el] == '' or r[el] == 'None'):
                r[el] = 'None'
        rangeLoop(r, helper)
        return r

    def rangeLoop(r, callback):
        for el in range(0, len(r)):
            callback(el)

    def run():
        for r in readcsv:
            r = trimElements(r)
            r = populateRowWithPlaceholders(r)

            statePos = fetchStatePosition(r)

            if (statePos):
                r = populateRegion(r, statePos)
            r = populateEmptyStrings(r)

            populatedTable.append(r)

    run()

with open('populated-people.csv', 'w') as csvfile:
    csvriter = csv.writer(csvfile)
    for row in populatedTable:
        csvriter.writerow(row)
