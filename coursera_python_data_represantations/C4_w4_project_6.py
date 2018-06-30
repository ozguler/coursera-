"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal
import random


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """

    code = {}
    codefile = codeinfo['codefile']
    plot_code = codeinfo['plot_codes']
    data_code = codeinfo['data_codes']

    code_list = []
    with open(codefile, newline='') as csvfile:
        codefile_read = csv.DictReader(csvfile, quotechar=codeinfo['quote'])
        for row in codefile_read:
            code_list.append(row)

    conversion = {}

    for item in code_list:
        conversion[item[plot_code]] = item[data_code]

    # print(conversion)
    return conversion


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    print(codeinfo)
    print(plot_countries)
    print(gdp_countries)
    mapper = {}
    unmatched = set()
    for key in plot_countries.keys():
        found = 0
        for item in gdp_countries:
            if plot_countries[key] == gdp_countries[item]['Country Name']:
                mapper[key] = item
                found = 1
        if found == 1:
            pass
        else:
            unmatched.add(key)


    #
    # print(mapper)
    # print(unmatched)
    return mapper, unmatched


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """

    print("gdpinfo",gdpinfo)
    print("codeinfo",codeinfo)
    print("plotcountries", plot_countries)
    print("year", year)

    codex = gdpinfo['country_code']
    gdpfile = gdpinfo['gdpfile']
    gdp_dict = {}

    # with open(gdpfile, newline='') as csvfile:
    #      gdpfile_read = csv.DictReader(csvfile, quotechar=gdpinfo['quote'])
    #      for row in gdpfile_read:
    #          rowid = row[codex]
    #          gdp_dict[rowid] = row

    with open(gdpfile, newline='') as csvfile:
        gdpfile_read = csv.DictReader(csvfile, quotechar=gdpinfo['quote'])
        for row in gdpfile_read:
            rowid = str(row[codex]).lower()
            gdp_dict[rowid] = row


    codefile = codeinfo['codefile']
    code_list = []
    with open(codefile, newline='') as csvfile:
        codefile_read = csv.DictReader(csvfile, quotechar=codeinfo['quote'])
        for row in codefile_read:
            code_list.append(row)

    print("gdp_dict is", gdp_dict)
    print("code_list is", code_list)


    #code mapper
    #convert cd2 to cd3



    mapper = {}

    plot_codes = codeinfo['plot_codes']
    data_codes = codeinfo['data_codes']

    print("plotcodes is", plot_codes)
    print("datacodes is",data_codes)

    not_in_gdpdata = set()

    """Create a mapper that will map plot_codes to data_codes
    plot_countries maps pygal codes to country names (e.g c1 is a country name)

    mapper -> plot_codes=Cd2 to data_codes=Cd3
    c1 - > ABC, c2 -> DEF, c3 ->GHI, c4 ->JKL
    What we ultimately would like to do is...
    map


    """

    for item in plot_countries:
        for item2 in code_list:
            if item2[plot_codes] == plot_countries[item]:
#                mapper[plot_countries[item]] = item2[data_codes]
                mapper[item] = item2[data_codes]

    print("Mapper is", mapper)
#plot_countries'de olup code.csv'de olmayanlari direk not_in_gdpdata
#ya ekliyoruz.


    for item in plot_countries:
        # print(item)
        if item in mapper.keys():
            print(item, "is in mapper")
            pass
        else:
            print(item, "is not in mapper, going into not_in_gdpdata")
            not_in_gdpdata.add(item)



#gdplist'i Code'a gore bir dict sekline donusturelim...
    gdp_data = {}
    no_data_in_year = set()

    for item in mapper:
        lower_mapper = str(mapper[item]).lower()
        print(lower_mapper)
        if  lower_mapper in gdp_dict:
            # print(item, "is in gdp_dict")
            # print(gdp_dict[lower_mapper])
            # print("year is of type",type(year))
            # print(gdp_dict[lower_mapper][year])
            # print(gdp_dict_row[
            if gdp_dict[lower_mapper][year]:
                gdp_data[item] = math.log(float(gdp_dict[lower_mapper][year]),10)
            else:
                no_data_in_year.add(item)
        else:
            print(item, "is not in gdp_dict")
            not_in_gdpdata.add(item)





    # print(codex)
    # print("mapper is", mapper)




#The first set contains the country codes from plot_countries that were not
#found in the GDP data file.

# The second set contains the country
# codes from plot_countries that were found in the GDP data file, but
# have no GDP data for the specified year.









    #math.log(x,10)

    # for item in plot_countries:
    #     mapper[plot_countries[item]] =

    print("gdp_data",gdp_data)
    print("not_in_gdpdata", not_in_gdpdata)
    print("no_data_in_year",no_data_in_year)
    return gdp_data, not_in_gdpdata, no_data_in_year



def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    return


def test_render_world_map():
    """
    Test the project code for several years
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

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")
