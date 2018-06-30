"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    # print("file name is", filename)
    # print("separator is",separator)
    # print("quote is", quote)

    list_strings = []
    fields = []

    with open(filename, newline='') as csvfile:
        file_read = csv.reader(csvfile, delimiter = separator, quotechar = quote)
        for row in file_read:
            # print(row)
            list_strings.append(row)
    # print(list_strings[0])

    # print(list_strings[0])
    # for item in list_strings[0]:
    #     print(item)
    #     fields.append(item)
    #     print(fields)
    # print("fields is", fields)

    return list_strings[0]


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """


    # print("file name is", filename)
    # print("separator is",separator)
    # print("quote is", quote)

    file_dict = []
    with open(filename, newline='') as csvfile:
        file_read = csv.DictReader(csvfile, delimiter = separator, quotechar = quote)
        for row in file_read:
            file_dict.append(row)

    # print(file_dict)
    return file_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    # print("file name is",filename)
    # print("keyfield is",keyfield)
    # print("separator is",separator)
    # print("quote is", quote)

    file_dict = {}
    with open(filename, newline='') as csvfile:
        file_read = csv.DictReader(csvfile, delimiter = separator, quotechar = quote)
        for row in file_read:
            rowid = row[keyfield]
            file_dict[rowid] = row

    print(file_dict)
    return file_dict


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """

    pass


# read_csv_as_list_dict('table1.csv', ',', '"')
# read_csv_as_nested_dict('table1.csv', 'Field1', ',', '"')
# read_csv_fieldnames('table1.csv', ',', '"')
