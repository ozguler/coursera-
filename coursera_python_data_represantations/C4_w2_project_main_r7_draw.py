
"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """

    table = {}
    with open(filename, newline="") as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter= separator, quotechar= quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
#    print(table)
    return(table)


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output:
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    gdpdata_mutate = []

    for key in gdpdata.keys():

        if gdpdata[key] == "":
#            tuple_ = (int(key),float(0))
#            tuple_ = ()
            pass
        else:
            if ((int(key) >= gdpinfo["min_year"]) & (int(key) <= gdpinfo["max_year"])):
                tuple_ = (int(key), float(gdpdata[key]))
                gdpdata_mutate.append(tuple_)

    gdpdata_mutate_sorted = sorted(gdpdata_mutate, key = lambda tup: tup[0])
#    print(gdpdata_mutate_sorted)
    return (gdpdata_mutate_sorted)


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """


    filename = gdpinfo['gdpfile']
    keyfield = gdpinfo['country_name']
    separator = gdpinfo['separator']
    quote = gdpinfo['quote']
    min_year = gdpinfo['min_year']
    max_year = gdpinfo['max_year']


    gdp_table = read_csv_as_nested_dict(filename, keyfield, separator, quote)
    #write code to turn gdp_table into "gdpdata" - tuples for each individual co
#    print(gdp_table[])

#    for country in country_list:
#        if country in gdp_table:
#            print("x")

    gdpdata = {}
    dictx = {}
    gdpcoos = {}
    for country in country_list:
        if country in gdp_table:
            dict_row = {}
            for year in range(min_year, max_year+1):
                dictx[year] = gdp_table[country][str(year)]
#            print(dictx)
#            print(year, dictx[year])
            gdpdata[country] = dictx
            dictx = {}
            gdpcoos[country] = build_plot_values(gdpinfo, gdpdata[country])
        else:
            gdpcoos[country] = []


    return (gdpcoos)


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """


    plot_dict = build_plot_dict(gdpinfo,country_list)
    print(plot_dict)

    xy_chart =pygal.XY(stroke = False)
    xy_chart.title = plot_file

    for country in country_list:
        xy_chart.add(country,plot_dict[country])

    xy_chart.render_to_file("/Users/ozguler/Downloads/gitrepo/coursera_python_data_represantations/xy_chart.svg")
    xy_chart.render_in_browser()
    return


def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
                   "isp_gdp_xy_uk+usa.svg")


# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

# test_render_xy_plot()

gdpinfox = {
       "gdpfile": "/Users/ozguler/Downloads/gitrepo/coursera_python_data_represantations/table4.csv",
        "gdpfile": "/Users/ozguler/Downloads/gitrepo/coursera_python_data_represantations/isp_gdp.csv",
        "keyfield": "Country Name",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

#gdpinfo = {
#        "gdpfile": "isp_gdp.csv",        # Name of the GDP CSV file
#        "separator": ",",                # Separator character in CSV file
#        "quote": '"',                    # Quote character in CSV file
#        "min_year": 1960,                # Oldest year of GDP data in CSV file
#        "max_year": 2015,                # Latest year of GDP data in CSV file
#        "country_name": "Country Name",  # Country name field name
#        "country_code": "Country Code"   # Country code field name
#    }
#gdpinfo2 = {   #used for function build_plot_values
#        "gdpfile": '',
#        "keyfield": "Country Name",
#        "separator": '', 'quote': '',
#        "quote": '"',
#        "min_year": 1980,
#        "max_year": 2000,
#        "country_name": 'Country Name',
#        "country_code": 'Code'
#    }


#x = read_csv_as_nested_dict(gdpinfox["gdpfile"],gdpinfox["keyfield"],gdpinfox[
#"separator"],gdpinfox["quote"])
#read_csv_as_nested_dict(gdpinfox["gdpfile"],'Field, 1', ',', "'")
#read_csv_as_nested_dict('table4.csv', '1', ',', "'")
#print(build_plot_values({'separator': '', 'quote': '', 'min_year': 1980, 'country_code': 'Code',
#'max_year': 2000, 'country_name': 'Country Name', 'gdpfile': ''}, {'1985': '10',
#'1995': '30', '1990': '20'}))
#(build_plot_values({'gdpfile': '', 'min_year': 2001, 'country_code': 'Code',
#'quote': '', 'country_name':
#'Country Name', 'separator': '', 'max_year': 2015},
#{'2005': '4', '2010': '', '2008': '7', '2002': '1', '2003': '2', '2007': '',
#'2009': '8', '2013': '', '2001': '', '2011': '10', '2015': '14', '2012': '11',
#'2014': '13', '2004': '', '2006': '5'}))
#print(x["Turkey"])
#coos = build_plot_values(gdpinfox,x["Turkey"])
#print(coos)

#print(build_plot_dict(gdpinfox,["Brazil","Turkey","x"]))
render_xy_plot(gdpinfox,["Brazil","Turkey","Greece","France"],"GDP Data")
