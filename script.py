import csv
import copy
import json

with open('people.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    with open('state_to_region.json') as f:
        data = json.load(f)

    def trimList(list):
        currentElement = 0
        for element in list:
            list[currentElement] = element.strip()
            currentElement += 1
        return list

    for list in readCSV:
        list = copy.deepcopy(trimList(list))

        if (len(list) == 5):
            for i in range(0, 5):
                if (list[i] in data.keys()):
                    # Assuming that list[i] is in position 3 when row length = 5
                    list[i + 1] = data[list[i]]
