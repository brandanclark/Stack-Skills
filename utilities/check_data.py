"""
# Helps you to check the data in 'raw_data' folder
# Run it to see the unique years, disciplines, etc
# and look through the results to see if any of the data looks wrong
"""

with open('../raw_data/results.txt') as input_file:
    lines = input_file.readlines()

results = []

for line in lines:
    parts = line.split(',')

    single_result = {
        'year': int(parts[0]),
        'discipline': parts[1].strip(),
        'country': parts[2].strip(),
        'medal_type': parts[3].strip(),
        'number_of_medals': int(parts[4])
    }

    results.append(single_result)

medal_types = set()
for result in results:
    medal_types.add(result['medal_type'])
print(medal_types)

years = set()
for result in results:
    years.add(result['year'])
print(years)

disciplines = set()
for result in results:
    disciplines.add(result['discipline'])
print(disciplines)

countries = set()
for result in results:
    countries.add(result['country'])
print(countries)

number_of_medals = set()
for result in results:
    number_of_medals.add(result['number_of_medals'])
print(number_of_medals)
