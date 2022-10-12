#Ch 11 : Breaking up Larger Programs and Functions
#main reasons to use functions
#help you not repeat yourself
#break down a large problem into small parts or steps
#test each function individually
#long stretches of code can be hard to follow, specific functions can be named specifically

#defining a function using def, teaching python how to do something new
#function definition consists with a function header and a function block
#after colon is the function block which is executed when the function is called
def say_hello():
  print ('Hello')

#using ('calling') the function
say_hello ()

#function parameters
#parameters are variables passed into a function to be used by that function
#function below but relies on results paramater for which code was never provided
"""
def print_unique_values (results, fieldname):
  unique_values = set ()
  for result in results:
    value = result [fieldname]
    unique_values.add (value)
  print (fieldname, unique_values)

print_unique_values (results, 'year')
print_unique_values (results, 'discipline')
print_unique_values (results, 'number_of_medals')
"""

#simple function showing how parameters work
#define the function
#when defined, this function is completely seperate from the outside world
#when it is called, it knows it will receive some information in the shape of the variable some_text
#variable some_text only exists within this function
def print_twice (some_text):
  print (some_text)
  print (some_text)
  
#set the parameter of some_text to be 'Hello'
print_twice ('Hello')

#when we pass another parameter of text, the new text is then printed twice
print_twice ('Good')

#can also pass in a variable name
greeting = 'How are you?'
print_twice (greeting)

#local versus global variables
#below we create two different variables called number
def count_to_five ():
  #here is created a local variable within the function, which we set to 0
  number = 0
  while number <= 5:
    print (number)
    number = number + 1

  print ('At the end of count_to_five, number is', number)

#here we create a global variable which we set to 1234
number = 1234
count_to_five()
print ('Back in the main code, number is', number)

#in the above code, we take the following steps:
"""
1 (Line 54, plus lines 56-59) Define a new function, called ‘count_to_five’.
2 (Line 64) Create a global variable called ‘number’ with a value of 1234.
3 (Line 65) Call the ‘count_to_five’ function.
4 (Line 56) Create a local variable called ‘number’ with a value of 0.
◦ Note that we now have two variables called ‘number’, one global and one local.
5 (Line 58) Print the local ‘number’ variable. This is currently zero, so this prints a 0.
6 (Line 59) Increase the local ‘number’ variable by one. It is now 1.
7 (Line 58) Again, print the local ‘number’ variable. This is one, so this prints a 1.
8 (Lines 57 - 59) The ‘while’ loop is run four more times, until the test ‘number <= 5’ fails. This test fails when number is 6, because ‘6 <= 5’ is not True.
◦ Each time another number is printed. This prints out 2, 3, 4 and 5.
9 (Line 61) The local ‘number’ variable is now ‘6’. This prints the text “At the end of count_to_five, number is 6”.
10 (After line 61) The function is done. The last line of the function (line 61) has been run. Python exits the count_to_five function. Any local variables created within this function are deleted automatically.
11 (Line 63) Python continues after the line where the function was called. It prints some text and the value of ‘number’. We’re no longer within a function, so we can only see the global variables. The local ‘number’ variable was deleted, as described in the previous step. So Python prints the global ‘number’ variable. This started with a value of 1234
"""

#positional and keyword parameters
#parameters that can be passed in by name to avoid confusion
def say_something_friendly (name, time_of_day):
  print ('Good', time_of_day, ',', name)

say_something_friendly('Sue', 'morning')
say_something_friendly('John', 'evening')

#what happens if we get confused and mistake the name and time of day in the function call?
say_something_friendly('morning', 'Sue')
#Python does not care that we got the parameters backwards and prints it no matter what

#if we want to make sure we get it right, we can use the name of parameters when calling the function
say_something_friendly(name = 'Sue', time_of_day = 'morning')
say_something_friendly(name = 'John', time_of_day = 'evening')

#mis-order of parameter names when calling the function will still work correctly
say_something_friendly(time_of_day = 'night', name = 'Bernie')

#return statements

#code below to create the results parameter
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

results = []

for line in lines:
  parts = line.split(',')
  
  year = int(parts[0])
  discipline = parts[1].strip()
  country = parts[2].strip()
  medal_type = parts[3].strip()
  number_of_medals = int(parts[4])

  single_result = {}
  single_result['year'] = year
  single_result['discipline'] = discipline
  single_result['country'] = country
  single_result['medal_type'] = medal_type
  single_result['number_of_medals'] = number_of_medals

  results.append(single_result)

for result in results:
  year = result['year']
  if year < 100:
    year += 2000
    result['year'] = year

def print_unique_values (results, fieldname):
  unique_values = set ()
  for result in results:
    value = result [fieldname]
    unique_values.add (value)
  print (fieldname, unique_values)

print_unique_values (results, 'year')
print_unique_values (results, 'discipline')
print_unique_values (results, 'number_of_medals')
#end creating results parameter

#return statement example
#function that breaks up raw text into dictionaries so we can get each value using a key
#return statement exits the function and returns some result
#code not working due to bad data 
"""
def process_line (line):
  parts = line.split (',')
  single_result = {
    'year': int (parts [0]),
    'discipline': parts [1].strip(),
    'country': parts [2].strip(),
    'medal_type': parts [3].strip(),
    'number_of_medals': int(parts [4])
  }
  return single_result

input_file = open ('raw_data/results.txt')
lines = input_file.readlines ()
input_file.close ()

results = []
for line in lines:
  single_result = process_line (line)
  results.append (single_result)

print (len (results))
print (results [0])
"""

#working with .json files
#add the indent=4 to create good looking readable data
import json
with open ('clean_data/results.json', 'w') as json_file:
  json.dump (results, json_file, indent=4)

#once we have the .json file, we can write a new script that analyzes the .json script and prints out some information
#open and load the .json file
#loop through the results
#add the number of medals where year == 2012
total_2012 = 0
for result in results:
  if result ['year'] == 2012:
    total_2012 += result ['number_of_medals']

print (total_2012, 'medals were awarded in 2012')

