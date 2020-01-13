import csv

import Property


# Imports properties from the Properties.csv file
def import_properties():
    with open("Properties.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        prop_list = []
        for row in reader:
            if line_count == 0:
                # Ignore the header
                line_count += 1
            else:
                if row[11] == "Railroad":
                    # call railroad constructor
                    pass
                elif row[11] == "Utility":
                    # call utility constructor
                    pass
                else:
                    # call regular constructor
                    pass
        return prop_list


# Imports spaces from the Spaces.csv file
def import_spaces():
    with open("Spaces.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        spaces = []
        for row in reader:
            spaces.append({'name': row[0], 'ownable': False, 'owner': None, 'freq': 0})
