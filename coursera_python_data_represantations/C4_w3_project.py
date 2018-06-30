"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """

    country_r = {}
    country_n = set()
    for country in plot_countries.keys():
        if plot_countries[country]:
            if plot_countries[country] in gdp_countries:
                country_r[country] = plot_countries[country]
            else:
                country_n.add(country)

#    print(country_r), print(country_n)

    return country_r, country_n


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """


    gdpfile   = gdpinfo["gdpfile"]
    xxx       = gdpinfo["country_name"]
    # delimiter = gdpinfo["separator"]
    # quotechar = gdpinfo["quote"]

    gdpdata = {}
    with open(gdpfile, newline='') as csvfile:
        gdpfile_read = csv.DictReader(csvfile)
        for row in gdpfile_read:
            rowid = row[xxx]
            gdpdata[rowid] = row

#    print(gdpdata)
    country_gdp     = {}
    country_non     = set()
    country_gdp_non = set()

    # print(gdpdata)
    # print(gdpdata["Country1"]["2000"])
    # print(gdpdata["Country2"]["2000"])

    for country_code in plot_countries:
        print (country_code)
        country_name = plot_countries[country_code]
        print (country_name)
        if country_name in gdpdata:
            print(country_name, "is in gdpinfo!")
            if gdpdata[country_name][str(year)] == "":
                country_gdp_non.add(country_code)
            else:
                country_gdp[country_code] = math.log(float(gdpdata[country_name][str(year)]),10)
        else:
            country_non.add(country_code)

    # print("country gdp", country_gdp)
    # print("country non", country_non)
    # print("country gdp non", country_gdp_non)


    return country_gdp, country_non, country_gdp_non


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    return


def test_render_world_map():
    """
    Test the project code for several years.
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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
#reconcile_countries_by_name({'no': 'Norway', 'us': 'United States', 'pr': 'Puerto Rico'}, {'United States': {'Country Name': 'United States', 'Country Code': 'USA'}, 'Norway': {'Country Name': 'Norway', 'Country Code': 'NOR'}})
#build_map_dict_by_name({'separator': ',', 'quote': '"', 'min_year': 2000, 'country_code': 'Code', 'max_year': 2005, 'country_name': 'Country Name', 'gdpfile': 'gdptable1.csv'}, {'C1': 'Country1', 'C4': 'Country4', 'C2': 'Country2', 'C5': 'Country5', 'C3': 'Country3'}, '2003')
