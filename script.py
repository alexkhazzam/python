import csv
import copy
import json

editedLists = []

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

    def elementExists(el):
        return el in data.keys()

    for list in readCSV:
        list = copy.deepcopy(trimList(list))

        if (len(list) == 5):
            for i in range(0, 5):
                # Assuming that list[i] is in position 3 when row length = 5
                if (elementExists(list[i])):
                    list[i + 1] = data[list[i]]
        else:
            while (len(list) != 5):
                list.append('')
            for i in range(0, 5):
                if (elementExists(list[i])):  # Not so efficient...but it will work
                    list[4] = data[list[i]]
                    list[3] = list[i]
                    list[i] = None
                    break  # No need to keep looping once state found
                # If state not found => continue and do not touch row

        editedLists.append(list)

with open('people.csv', 'w') as csvfile:
    csvWriter = csv.writer(csvfile)
    for list in editedLists:
        csvWriter.writerow(list)
