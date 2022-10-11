"""
Prints out a results table
of the number of medals
by country and type of medal
"""
import data_store
import sorted_data


def get_country_totals(results, country):
    """
    For one country, e.g. China, get the number of medals, split by gold/silver/bronze
    Return this as a dictionary {medal_type: number}
    """
    country_totals = {'gold': 0, 'silver': 0, 'bronze': 0}
    for result in results:
        if result['country'] != country:
            continue
        number_of_medals = result['number_of_medals']
        medal_type = result['medal_type']
        country_totals[medal_type] += number_of_medals
    return country_totals


def print_country_line(results, country):
    """
    Prints a nicely formatted results line for one country
    Extracts the information first, then prints it
    Uses fixed-width columns to make sure the results line up correctly
    """
    totals = get_country_totals(results, country)
    total_number_of_medals = sum(totals.values())

    country_line = f'{country:35}| {totals["gold"]:6} | {totals["silver"]:6} | ' + \
                    f'{totals["bronze"]:6} | ' + \
                    f'{total_number_of_medals:4}'
    print(country_line)


results = data_store.load_data()
sorted_countries = sorted_data.order_countries_by_total_medal_counts(results)

# Print the table header
first_line = f'{"year":35}|  gold  | silver | bronze | totals'
print(first_line)
print(f'{"country":35}|        |        |        |')
print("-" * len(first_line))

# Print the lines for the individual countries
for country in sorted_countries:
    print_country_line(results, country)
