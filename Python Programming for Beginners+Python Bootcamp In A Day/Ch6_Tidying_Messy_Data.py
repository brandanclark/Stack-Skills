#TIDYING MESSY DATA
#using tools we have learned already to clean data
line = '216, Tennis, Russia, gold, 7'
#split to move data into different parts in a list
parts = line.split(',')
#int to convert text to numbers
year = int(parts [0])
#strip to remove extra spaces
discipline = parts[1].strip()
country = parts[2].strip()
medal_type = parts[3].strip()
number_of_medals = int (parts [4])
print (year, discipline, country, medal_type, number_of_medals)

#using IF statement to test for bad data and print error message if data is bad
year = 216
if year < 2000:
  print ('Incorrect year', year)
print ('Done')

#same logic but with a correct year value
year = 2016
if year < 2000:
  print ('Incorrect year', year)
print ('Done')

"""python IF statement has the following
1. the word IF
2. a test, such as 'year < 2000'
3. a colon, after the test
4. an indented block of code, aka the if block
  python will evaluate everything between the IF and the colon. IF the test succeeds, Python will run the IF block code, if not the IF block is skipped
  if test returns 0, IF block is skipped, if test returns non-zero number, IF block is run
"""
#notice below, only the first IF block is run
if 5:
  print ("executing the first' 'if' block")
if 0:
  print ("executing the second 'if' block")

#can also use variable or calculation for a test
if 5*2-10:
  print ("First 'if' block")
if 5*3-10:
  print ("Second 'if' block")
print ('done')

#if block itself must be one or more lines of code, all indented with the same number of spaces
name = 'Fred'
if name:
  print('Hello', name)
name = ''
if not name:
  print('Hello stranger')

#if block ends just before non-empty line without an indentation
#any code after the if block is over is run, if the test fails or not
if True:
  print ('first line')
  print ('second line')
  print ('third line')
print ('done, final line')

#use the else block to execute something else when the test fails
name = 'Bob'
if name:
  print ('Hello', name)
else:
  print ('Hello stranger')
print(name)

#nested if blocks
#can nest multiple if blocks into one code
name = ''
if name == 'Fred':
  print('Hi Fred')
else:
  if name:
    print('Hi', name, 'welcome')
  else:
    print('Hello stranger')
print(name)

#can also use elif to do the same thing but with fewer indentation
name = 'Sue'
if name == 'Fred':
  print('Hi fred')
elif name == 'Sue':
  print('Hi Sue')
elif name:
  print('Hi', name, 'welcome')
else:
  print('Hellow stranger')

