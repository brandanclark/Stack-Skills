"""
Prints out a results table
of the number of medals
by country and year
"""
import json


def order_countries_by_total_medal_counts(results):
    """
    Returns a list of all countries,
    sorted by their overall total number of medals.
    The country with the largest number of medals is listed first
    """

    # Create a dictionary which counts the number of medals for each country
    totals = {}
    for result in results:
        country = result['country']
        number_of_medals = result['number_of_medals']
        if country not in totals:
            totals[country] = 0
        totals[country] += number_of_medals

    # Create a list of tuples from the previous list, for instance
    # [ (347, 'China'), (432, 'France'), etc]
    # This makes it easier to sort the data in the next step
    totals_as_list = []
    for country, number_of_medals in totals.items():
        totals_as_list.append((number_of_medals, country))

    # Sort the list of tuples, in reverse order
    # The entry (number, country) with the highest number will be first
    totals_as_list.sort(reverse=True)

    # Creates a list of countries (just the country name), in the same order as the previous step
    sorted_countries = []
    for number_of_medals, country in totals_as_list:
        sorted_countries.append(country)
    return sorted_countries


def get_country_totals(results, country):
    """
    For one country, e.g. China, get the number of medals, split by year
    Return this as a dictionary {year: number}
    """
    country_totals = {2004: 0, 2008: 0, 2012: 0, 2016: 0}
    for result in results:
        if result['country'] != country:
            continue
        number_of_medals = result['number_of_medals']
        year = result['year']
        country_totals[year] += number_of_medals
    return country_totals


def print_country_line(results, country):
    """
    Prints a nicely formatted results line for one country
    Extracts the information first, then prints it
    Uses fixed-width columns to make sure the results line up correctly
    """
    totals = get_country_totals(results, country)
    total_number_of_medals = sum(totals.values())

    country_line = f'{country:35}| {totals[2004]:4} | {totals[2008]:4} | ' + \
                    f'{totals[2012]:4} | {totals[2016]:4} | ' + \
                    f'{total_number_of_medals:4}'
    print(country_line)


def load_data():
    """
    Returns the clean results from the json file
    """
    with open('../clean_data/results.json') as json_file:
        results = json.load(json_file)
    return results


results = load_data()
sorted_countries = order_countries_by_total_medal_counts(results)

# Print the table header
first_line = f'{"year":35}| 2004 | 2008 | 2012 | 2016 | totals'
print(first_line)
print(f'{"country":35}|      |      |      |      |')
print("-" * len(first_line))

# Print the lines for the individual countries
for country in sorted_countries:
    print_country_line(results, country)
