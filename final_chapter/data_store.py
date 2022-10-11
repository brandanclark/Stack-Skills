"""
Function(s) to load the clean data, ready for creating tables etc
"""
import json


def load_data():
    """
    Returns the clean results from the json file
    """
    with open('../clean_data/results.json') as json_file:
        results = json.load(json_file)
    return results
