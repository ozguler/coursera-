import csv


def dictparse(csvfilename, keyfield):
    table = {}

    with open("/users/ozguler/Downloads/numbers.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile, skipinitialspace = "True", delimiter= " ")
        for line in csvreader:
            table[line[keyfield]] = line
    return table




print(dictparse("/users/ozguler/Downloads/numbers.csv", 'Sehir'))
