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
                    prop = Property.RailroadProperty(row[0], row[1], row[5], row[6],
                                                     row[7], row[8], row[10], row[11])

                elif row[11] == "Utility":
                    prop = Property.UtilityProperty(row[0], row[1], row[5], row[6],
                                                    row[10], row[11])

                else:
                    prop = Property.Property(row[0], row[1], row[2], row[3], row[4], row[5],
                                             row[6], row[7], row[8], row[9], row[10], row[11])
                prop_list.append(prop)
        return prop_list


# Imports spaces from the Spaces.csv file
def import_spaces():
    with open("Spaces.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        spaces = []
        for row in reader:
            spaces.append({'name': row[0], 'ownable': row[1], 'owner': None, 'freq': 0})
    return spaces


