"""
Function(s) to sort the data in different ways
"""


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
