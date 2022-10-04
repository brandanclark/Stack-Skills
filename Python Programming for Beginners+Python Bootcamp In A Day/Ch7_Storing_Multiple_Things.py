#CHAPTER 7: STORING MULTIPLE THINGS
#python offers different types of collections to store multiple things
#lists, tuples, dictionaries and sets

#store all valid years in one list
#lists start and end with []
valid_years = [2004, 2008, 2012, 2016]
year = 2016

#check to see if something is in a list using IN
if year in valid_years:
  print (year, 'is correct')
else:
  print (year, 'is incorrect')

year = 216
if year in valid_years:
  print (year, 'is correct')
else:
  print (year, 'is incorrect')

#deleting items in a list
#to delete an item in a list we use del
del valid_years [0]
print (valid_years)

#tuples are used a lot in Python, very similar to lists but cannot be changed
#below is what happens when you change a list
numbers = [0, 1, 2, 3, 4, 5]
numbers [2] = 22
print(numbers)

#tuples use round brackets instead of square
numbers = (0, 1, 2, 3, 4, 5)
print(numbers)

#changing a tuple causes errors
#numbers [2] = 22
print(numbers)

#how to write long python lines
#to break up a long line, use  {}
#this only works if performing a valid process
discipline_definitions = {}
discipline_definitions ['Athletics'] = ('collecting of sporting events' +
'that involve competitive running'                 'jumping, throwing and walking')
print(discipline_definitions)

#dictionaries
#create a dictionary. dictionaries have two elements, a key and a value
#syntax for a dictionary is {'key':'value', 'key1': 'value1'}
shapes = {'ball' : 'round', 'box' : 'square', 'bottle': 'cylinder', 'paper' : 'flat', 'string' : 'line', 'pyramid' : 'triangle', 'apple' : 'round'}
print (shapes)

#use .keys method to do something with all keys
for key in shapes.keys():
  print(key)

#use .values() to do something with values
for values in shapes.values():
  print(values)

#when you want both keys and values, use .items()
for key, value in shapes.items():
  print ('a', key, 'has a', value, 'shape')

#how do we use dictionaires to better store results?

#list functions
numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#to find the location/index of an element in a list
print (numbers.index (50))
#to delete an element in a list
del numbers [3]
print (numbers)

#sets
#sets are similar to lists, but each only contain unique values
