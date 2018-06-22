"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import random

##
## Provided code from Week 3 Project
##

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
    table = []
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
#            print row
            table.append(row)
    return table


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
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table

##
## Provided formulas for common batting statistics
##

# Typical cutoff used for official statistics
MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


##
## Part 1: Functions to compute top batting statistics by year
##

def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    table = []
    for row in statistics:
        if row["yearID"] == str(yearid):
            table.append(row)
    return table


def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    stat_list = []
    for row in statistics:
        stat_list.append((row['playerID'], formula(info,row)))

    stat_list.sort(key = lambda pair:pair[1], reverse = True)
    return stat_list[0:numplayers]


def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """




##
## Provided testing code
##



#Test Script to test Part1 Function1 Filter_by_year
statistics = read_csv_as_list_dict("/Users/ozguler/Downloads/gitrepo/coursera_python_data_represantations/Batting_2016.csv",","," ")
#print(statistics)
x = filter_by_year(statistics, 1977, 1977 )
#print(x)

#Test Script to test Part1 Function2 top_player_ids
#statistics = read_csv_as_list_dict("/Users/ozguler/Downloads/gitrepo/coursera_python_data_represantations/Batting_2016.csv",","," ")
info =              {"masterfile": "Master_2016.csv",   # Name of Master CSV file
                    "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                    "separator": ",",                  # Separator character in CSV files
                    "quote": '"',                      # Quote character in CSV files
                    "playerid": "playerID",            # Player ID field name
                    "firstname": "nameFirst",          # First name field name
                    "lastname": "nameLast",            # Last name field name
                    "yearid": "yearID",                # Year field name
                    "atbats": "AB",                    # At bats field name
                    "hits": "H",                       # Hits field name
                    "doubles": "2B",                   # Doubles field name
                    "triples": "3B",                   # Triples field name
                    "homeruns": "HR",                  # Home runs field name
                    "walks": "BB",                     # Walks field name
                    "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

tpid = top_player_ids(info, x, batting_average, 5)
print(tpid)

x  = read_csv_as_list_dict("/Users/ozguler/Downloads/gitrepo/coursera_python_data_represantations/Master_2016.csv",","," ")
lookup_player_names(x, tpid)
