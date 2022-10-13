#Chapter 12: Summarizing and Presenting Results
#creating a table of number of medals won by year and country
#sorted by year and number of medals won

#load the data

#code below to create the results parameter
#get results into a dictionary
lines = """2012, Swimming, Netherlands, gold, 1
2008, Swimming, Japan, silver, 3
2016, Volleyball, Germany, silver, 1
2004, Tennis, Finland, gold, 6
2012, Tennis, Sweden, bronze, 1
2016, Tennis, China, silver, 6
2016, Athletics, Norway, bronze, 0
2004, Rowing, China, bronze, 0
2016, Cycling, Russia, gold, 3
2012, Volleyball, Denemark, silver, 6
2004, Synchronized Swimming, Japan, bronze, 5
2012, Football / Soccer, Czechoslovakia, bronze, 2
2016, Football / Soccer, Russia, silver, 5
8, Gymnastics, Bulgaria, silver, 3
2004, Tennis, Austria, bronze, 6
2004, Football / Soccer, Soviet Union, silver, 2
2008, Athletics, Canada, bronze, 0
2016, Gymnastics, Bulgaria, gold, 3
2008, Tennis, Belgium, silver, 6
2008, Gymnastics, Sweden, gold, 1
2016, Rowing, United States, s, 0
2008, Gymnastics, Germany, gold, 6
2016, Tennis, Australia, silver, 2
2004, Cycling, Norway, bronze, 3
2004, Swimming, China, silver, 5
2004, Gymnastics, Sweden, bronze, 0
212, Tennis, Austria, bronze, 1
2008, Rowing, Romania, silver, 2
2016, Football / Soccer, Finland, bronze, 0
2016, Gymnastics, Czechoslovakia, gold, 2
2012, Athletics, Austria, gold, 5
2004, Tennis, East Germany, silver, 1
2012, Rowing, Denemark, silver, 1
2012, Rowing, Bulgaria, silver, 5
2004, Athletics, China, bronze, 3
2016, Gymnastics, West Germany, bronze, 2
2004, Football / Soccer, South Korea, bronze, 0
2012, Rowing, Sweden, silver, 0
2008, Swimming, Austria, g, 3
2004, Volleyball, Finland, silver, 4
2012, Synchronized Swimming, Great Britain, g, 0
2012, Cycling, Czechoslovakia, silver, 5
2012, Volleyball, Austria, gold, 5
2016, Cycling, Belgium, gold, 6
2008, Cycling, United States, bronze, 0
2008, Modern Pentathlon, Denemark, gold, 5
2004, Rowing, Great Britain, silver, 6
2004, Football / Soccer, Denemark, gold, 6
2012, Tennis, Hungary, silver, 1
2008, Football / Soccer, Romania, silver, 5
2004, Synchronized Swimming, Russia, bronze, 0
2016, Rowing, Finland, bronze, 1
2004, Cycling, Canada, silver, 0
2016, Football / Soccer, Belgium, silver, 4
2004, Synchronized Swimming, Romania, bronze, 6
2008, Tennis, Netherlands, silver, 4
2012, Gymnastics, Soviet Union, bronze, 0
2016, Swimming, Denemark, gold, 2
2008, Volleyball, Belgium, gold, 2
2004, Swimming, East Germany, silver, 2
2008, Rowing, Soviet Union, silver, 0
2008, Synchronized Swimming, Commonwealth of Independent States, gold, 2
2012, Modern Pentathlon, Great Britain, silver, 0
2012, Swimming, South Korea, gold, 1
2008, Volleyball, Russia, silver, 4
2016, Rowing, Australia, silver, 5
2008, Synchronized Swimming, United States, gold, 2
2012, Swimming, Austria, gold, 4
2012, Volleyball, Belgium, gold, 4
2016, Modern Pentathlon, Italy, silver, 1
2004, Swimming, Belgium, gold, 3
2008, Gymnastics, Romania, silver, 1
2016, Tennis, Finland, silver, 4
2012, Gymnastics, Finland, silver, 5
2008, Football / Soccer, Norway, gold, 3
2016, Tennis, Soviet Union, silver, 0
2008, Cycling, Cuba, silver, 3
2016, Cycling, China, bronze, 4
2004, Volleyball, Hungary, bronze, 3
2004, Cycling, Denemark, gold, 5
2008, Rowing, Switzerland, silver, 2
2004, Athletics, Denemark, gold, 1
2008, Synchronized Swimming, Finland, silver, 6
2008, Rowing, Finland, bronze, 1
4, Synchronized Swimming, China, bronze, 2
2008, Cycling, Russia, g, 1
2004, Volleyball, South Korea, gold, 5
2016, Football / Soccer, Commonwealth of Independent States, gold, 6
2008, Athletics, Switzerland, silver, 2
2008, Volleyball, Norway, gold, 4
2008, Cycling, Australia, silver, 3
2004, Modern Pentathlon, West Germany, silver, 6
2012, Football / Soccer, South Korea, g, 6
2016, Tennis, West Germany, bronze, 3
2004, Rowing, Cuba, bronze, 3
2004, Gymnastics, Great Britain, silver, 6
2008, Football / Soccer, Australia, bronze, 4
2008, Tennis, Australia, gold, 2
2004, Synchronized Swimming, Switzerland, silver, 6
2016, Cycling, Romania, silver, 4
2012, Athletics, France, gold, 3
2004, Tennis, Italy, bronze, 3
2016, Football / Soccer, Turkey, gold, 0
2004, Synchronized Swimming, Romania, silver, 2
2012, Synchronized Swimming, Sweden, gold, 3
2012, Volleyball, Australia, silver, 0
2008, Synchronized Swimming, Belgium, gold, 0
2016, Football / Soccer, East Germany, silver, 0
2016, Swimming, Netherlands, bronze, 1
2012, Volleyball, Germany, gold, 1
2016, Modern Pentathlon, Finland, gold, 5
2008, Synchronized Swimming, Switzerland, bronze, 0
2016, Volleyball, France, silver, 0
2012, Modern Pentathlon, Great Britain, gold, 5
2012, Cycling, Denemark, bronze, 3
2016, Tennis, Russia, gold, 0
2016, Volleyball, Soviet Union, gold, 5
2004, Rowing, Romania, bronze, 0
2008, Swimming, Netherlands, silver, 3
2016, Swimming, South Korea, silver, 6
2016, Swimming, Great Britain, gold, 6
2008, Volleyball, Bulgaria, bronze, 6
2008, Swimming, Switzerland, bronze, 1
2016, Cycling, Switzerland, silver, 6
2004, Rowing, Japan, gold, 6
2008, Swimming, Norway, bronze, 5
2012, Athletics, Finland, silver, 4
2004, Modern Pentathlon, Netherlands, silver, 3
2004, Synchronized Swimming, East Germany, bronze, 4
2004, Swimming, Switzerland, bronze, 0
2016, Synchronized Swimming, Belgium, gold, 5
2004, Modern Pentathlon, Canada, bronze, 2
2016, Gymnastics, Romania, gold, 0
2008, Cycling, Canada, bronze, 1
2004, Gymnastics, Norway, bronze, 1
2012, Athletics, Turkey, gold, 5
2004, Modern Pentathlon, Finland, bronze, 3
2004, Tennis, Australia, bronze, 4
2012, Rowing, Germany, gold, 6
2008, Athletics, China, gold, 6
2004, Rowing, Turkey, silver, 3
2012, Synchronized Swimming, Sweden, silver, 0
2012, Rowing, Great Britain, bronze, 3
2008, Swimming, Australia, bronze, 6
2012, Rowing, Soviet Union, s, 4
2012, Rowing, Great Britain, gold, 2
2004, Tennis, Turkey, silver, 6
2004, Football / Soccer, Japan, silver, 3
2004, Swimming, Czechoslovakia, gold, 5
2004, Swimming, East Germany, bronze, 4
2004, Athletics, Germany, silver, 0
2016, Football / Soccer, Switzerland, silver, 0
2004, Swimming, Australia, bronze, 4
2004, Volleyball, Russia, silver, 2
2008, Volleyball, Finland, bronze, 5"""
lines = lines.split('\n')
years, disciplines, countries, medal_types, number_of_medals = [], [], [], [], []

def process_line (line):
  parts = line.split(',')
  single_result = {
    'year': int  (parts [0]),
    'discipline': parts [1].strip (),
    'country': parts [2].strip (),
    'medal_type': parts [3].strip(),
    'number_of_mdeals': int (parts [4])
  }
  return single_result

input_file = open ('raw_data/results.txt')
lines = input_file.readlines ()
input_file.close ()

import json
with open ('clean_data/results.json') as json_file:
  results = json.load(json_file)

#create totals as a dictionary
  #country names as the key
  #total number of names as the values
totals = {}
for result in results:
  country = result['country']
  number_of_medals = result ['number_of_medals']
#check to see if a country is in the dictionary
  if country not in totals:
    totals [country] = number_of_medals
#add medals to the new country
  else:
    totals [country] += number_of_medals

#print totals dictionary
print(totals)

#sort by number of medals
#cannot sort a dictionary in python so must use a list instead
#create sorted list of country names
country_names = list (totals)
country_names.sort()
print(country_names)

#we want to sort the countries not by names but by number of medals
#first we turn our totals dictionary into a list of tuples with country and number of medals
totals_as_list = []
for country, number_of_medals in totals.items ():
  totals_as_list.append ( (number_of_medals, country))
#now sort the list, using reverse = true
totals_as_list.sort(reverse=True)
print (totals_as_list)

#drop the medal numbers and just have our sorted list of countries
sorted_countries = []
for number_of_medals, country in totals_as_list:
  sorted_countries.append (country)
print (sorted_countries)

#everything to get a list of countries sorted by medal counts in a single function
#can now pass in a set of results and have it ordered by medal count
def order_countries_by_total_medal_counts (results):
  totals = {}
  for result in results:
    country = result ['country']
    number_of_medals = result ['number_of_medals']
    if country not in totals:
      totals [country] = 0
    totals [country] += number_of_medals

  totals_as_list = []
  for country, number_of_medals, in totals.items ():
    totals_as_list.append ( (number_of_medals, country))

  totals_as_list.sort (reverse=True)

  sorted_countries = []
  for number_of_mdeals, country in totals_as_list:
    sorted_countries.append (country)
  return sorted_countries
  
#with open ('clean_data/results.json') as json_file:
#  results = json.load (json_file)

sorted_countries = order_countries_by_total_medal_counts (results)

print (sorted_countries)

#with open ('clean_data/results.json') as json_file:
#  results = json.load (json_file)

#now let's write code to get results for one country and one year
#starts as a dictionary with no totals
def get_country_totals (country):
  country_totals = {2004: 0, 2008: 0, 2012: 0, 2016: 0}
  for result in results:
    if result ['country'] != country:
      continue
    number_of_medals = result ['number_of_medals']
    year = result ['year']
    country_totals [year] += number_of_medals
  return country_totals

#test by printing for one country
print (get_country_totals ('Netherlands'))

#run for all countries in sorted_countries list
for country in sorted_countries:
  totals = get_country_totals (country)
  print (country, totals)

#to create a good looking table, we need to know how large to make it
#create a list with the length of each country name
#then find largest value
name_lengths = []
for country in sorted_countries:
  name_lengths.append (len(country))
print (max (name_lengths))

#set first_column_width
first_column_width = max (name_lengths) + 1
print(first_column_width)

#print out the header
header = 'year'.ljust (35) + '| 2004 | 2008 | 2012 | 2016 | Totals'
print(header)

#easier way to do this
#formated string literals, aka f-strings
#f-strings are like blueprints with slots for filling in some information
#anything in curly brackets is calculated and then filled in
some_calculation = f'5 times 3 = {5*3}'
print(some_calculation)

#use these to specify the width of a slot for each line of the table
first_line = f'{"year":35} | 2004 | 2008 | 2012 | 2016 | totals'
print(first_line)
second_line = f'{"country":35} |      |      |      |      |'
print(second_line)
third_line = "-" * len (first_line)
print(third_line)

#make function to print line for country
def print_country_line (results, country):
  totals = get_country_totals (country)
  total_number_of_medals = sum (totals.values())

  country_line = f'{country:35} | {totals[2004]:4} | {totals[2008]:4} |' + \
                  f'{totals[2012]:4}  | {totals[2016]:4} |' + \
                  f'{total_number_of_medals:4}'
                                
  print(country_line)

#use function to print results for all countries
for country in sorted_countries:
  print_country_line (results, country)
                              