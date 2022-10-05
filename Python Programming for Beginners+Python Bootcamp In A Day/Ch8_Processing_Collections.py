#CHAPTER 8: PROCESSING COLLECTIONS
#a simple for loop
#starts with word for and ends with a colon
#also contains a variable name followed by the word in and then an interable
#indented for block is executed once for each item in the results list
#the first time the for block is run, python gets the first result from the results list
#once the indented for block is done, python goes back to the results variable and then looks for the next result
#at some point the results variable will go
#results is an iterable, a variable that python can iterate over
for character in 'Fred':
  print (character * 10)
  print ('-' * 10)

#more complex for loops: break, continue and else
#code to create random numbers and store in numbers as a list
"""
import random
numbers = [random.randint (0, 50_000_000) 
          for _ in range (1_000_000)]
print (numbers [:10])
"""
#in a for loop, any else block will be executed unless break is executed in the for block
#if 3098213 is found, the if block is executed, then the print statement and the break is executed which exits the loop
#if 3098213 is not found, the if block is not executed and the word found is not printed
"""for number in numbers:
  if number == 3098213:
    print ('Found')
    break
else:
  print ('Not found')
"""

#code using the results dataset that we do not have
"""
alert_count = 0
for result in results:
  number_of_medals = result ['number_of_medals']
  if 0 <= number_of_medals <=6:
    continue
  alert_count +=1
  print (result)
  if alert_count > 5:
    break
"""

#the range function - how to create a list of numbers
#lets create a numbered list
print ( '1________')
print ( '2________')
print ( '3________')
print ( '4________')
#or, use a while
number = 1
while number <=4:
  print (number, '_______')
  number +=1
#or, easiest way using range function
#can use one, two or three parameters in range function
#one parameter = how many numbers we want
print (list (range (10)))
#two parameters = specify the start and the end, the end reclusive of the actual value (final value -1)
for number in range (1,5):
  print (number, '_______')
#three parameters = start, end and step size
print (list (range (0, 20, 4)))
print (list (range (10, 0, -1)))

#the 'while' loop, do something for a while
#simple script that asks a user for a year and then prints top 15 results for that year
#if the user replies with a non-olympic year or any other year with no results, we ignore the input and ask again
#loop will run until the input is returned as a blank line
reply = '2000'
while reply:
  reply = int (reply)
  if reply in [2004, 2008, 2012, 2016]:
    for result in results [:15]:
      if result ['year'] == reply:
        print (result)
      reply = input ('Year?')

#just like with for loops, can also use break, continue and else
#continue goes back to the start of the loop, the while condition is checked again. if it is still true, the loop keeps going
#break breaks out of the while loop completely
#the else block is executed only if 'break' was never called
#if break does get called, the 'else' break is skipped
