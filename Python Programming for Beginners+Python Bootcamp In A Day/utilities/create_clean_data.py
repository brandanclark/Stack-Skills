"""
Loads the raw data from ../raw_data/results.txt

Replaces abbreviated medal types with the full version, e.g. 'g' to 'gold'
Ditto for abbreviated years, e.g. 12 to 2012

Saves the results in ../clean_data/results.json for easy use in creating medal tables
"""

import json


def final_data_check(results):
    """
    Checks there are no serious issues with the data.
    If this check fails, the script will stop
        and show an error message
    """
    for result in results:
        if (result['medal_type'] not in ['gold', 'silver', 'bronze']) or \
                result['year'] not in [2004, 2008, 2012, 2016]:
            print('Incorrect result:', result)
            print('results.json NOT created')
            print('Fix the error in ../raw_data/results.txt')
            print('And try again')
            print('Note: there may be multiple errors')

            # This line stops the code completely
            exit(1)


def clean_results(results):
    """
    Fixes abbreviated medal types and years
    """
    for result in results:
        if result['medal_type'] == 'b':
            result['medal_type'] = 'bronze'
        elif result['medal_type'] == 's':
            result['medal_type'] = 'silver'
        elif result['medal_type'] == 'g':
            result['medal_type'] = 'gold'

        if result['year'] < 2000:
            result['year'] += 2000


def process_lines(lines):
    """
    Converts the data from a list of strings, e.g.
    2008, Athletics, France, gold, 5

    To a list of dictionaries, e.g.
    {'year': 2012, 'discipline': 'Swimming', 'country': 'Netherlands', 'medal_type': 'gold', 'number_of_medals': 1}
    """
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

    return results


input_file = open('../raw_data/results.txt')
lines = input_file.readlines()
input_file.close()

results = process_lines(lines)

clean_results(results)

final_data_check(results)

with open('../clean_data/results.json', 'w') as json_file:
    json.dump(results, json_file)

print('Clean results created in ../clean_data/results.json')
