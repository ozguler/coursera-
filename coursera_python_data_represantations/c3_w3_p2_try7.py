"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

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
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
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
    print("Inside filter_by_year statistics is", statistics)
    print("Inside filter_by_year year is", year)
    print("Inside filter_by_year yearid is", yearid)

    batting = []
    # print(type(yearid))
    # print(yearid)
    # print(str(yearid))
    # str_yearid = yearid
    # yearidx = '"'+yearid+'
    # print(yearidx)


    for item in statistics:

        if item[yearid] == str(year):
            batting.append(item)


    # print("Batting is", batting)
    return batting

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
    # print("info is", info)
    # print("statistics is", statistics)
    # print("formula is", formula)
    # print("numplayers is", numplayers)

    player = info['playerid']

    stat_list = []
    for item in statistics:
        # print(item)
        stat_list.append((item[player], formula(info,item)))
    #
    stat_list.sort(key = lambda pair:pair[1], reverse = True)
    # #    print(stat_list[0:numplayers])
    # print(stat_list)
    top_players = stat_list[0:numplayers]
    print(top_players)
    return top_players

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

    separator = info['separator']
    quote = info['quote']
    # print("info is", info)
    # print("top_ids_and_stats is", top_ids_and_stats)
    file_master = info['masterfile']
    stats = read_csv_as_list_dict(file_master,separator, quote)
    firstname = info['firstname']
    lastname = info['lastname']
    playerid = info['playerid']
    string_ret = []

    for player_tup in top_ids_and_stats:
        for row in stats:
            if row[playerid] == player_tup[0]:
                #   print(row['nameFirst'], " ", row["nameLast"])
                string_ret.append(('{0:.3f} --- {1} {2}'.format(player_tup[1],row[firstname],row[lastname])))

    return (string_ret)



def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    print("info is", info)
    print("formula is", formula)
    print("numplayer is", numplayers)
    print("year is", year)


    master_file = info['masterfile']
    batting_file = info['battingfile']
    yearidx = info['yearid']
    separator = info['separator']
    quote = info['quote']
    top_players = []

    statistics = read_csv_as_list_dict(batting_file,separator,quote)
    info_sub = filter_by_year(statistics, year, yearidx)
#   print(info_sub)
    top_players = top_player_ids(info,info_sub, formula, numplayers)
#   print(top_players)
    # player_info = read_csv_as_list_dict(master_file, separator,quote)
    top_player_names = lookup_player_names(info, top_players)

    print(top_player_names)
    return top_player_names


##
## Part 2: Functions to compute top batting statistics by career
##

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    agg_stats = {}

    for row in statistics:
        if row[playerid] in agg_stats:
            for item in range(0,len(fields)):
                agg_stats[row[playerid]][fields[item]] += int(row[fields[item]])
        else:
            agg_stats[row[playerid]]={}
            for item in range(0,len(fields)):
                agg_stats[row[playerid]][fields[item]] = 0
                agg_stats[row[playerid]][playerid]= row[playerid]

            for item in range(0,len(fields)):
                agg_stats[row[playerid]][fields[item]] += int(row[fields[item]])

    return agg_stats




    # return {}


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    print("info is", info)
    print("formula is", formula)
    print("numplayers is", numplayers)

    batting_file = info['battingfile']
    master_file = info['masterfile']
    separator = info['separator']
    quote = info['quote']
    playerid = info['playerid']

    statistics = read_csv_as_list_dict(master_file, separator, quote)
    agg_stats = []
    players = []
    battingfields = info['battingfields']

    agg_stats = aggregate_by_player_id(statistics,playerid, battingfields)
    top_players = top_player_ids(info_stats, agg_stats, formula, numplayers)
    lookup_player_names(info,top_players)

    return []


##
## Provided testing code
##

def test_baseball_statistics():
    """
    Simple testing code.
    """

    #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    baseballdatainfo = {"masterfile": "Master_2016.csv",   # Name of Master CSV file
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

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


compute_top_stats_career({'masterfile': 'master1.csv', 'battingfile': 'batting1.csv', 'separator': ',', 'quote': '"',
'playerid': 'player', 'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year',
'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles', 'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks',
'battingfields': ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']},
batting_average, 4)
