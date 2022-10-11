#CH 9: Robust Programs - Handling Errors
#what happens when data is completely wrong?
#imagine writing a program for someone else
#how can we write a program to handle errors correctly and not show cryptic errors

line = '2016, Swimming, gold, 3'
parts = line.split (',')
print (len(parts))

#country is missing, only four parts of the line
"""
single_result = {
  'year': int (parts [0]),
  'discipline': parts [1].strip(),
  'country': parts [2].strip(),
  'medal_type': parts [3].strip(),
  'number_of_medals': int (parts [4])
}
"""

#two different ways to make code more robust
#the first is to look before you leap, check everything is safe before doing something

#first check the number of parts
#if there are not enough parts, show an error
#if there are the correct number of parts, show the number of medals
line = '2016, Swimming, gold, 3'
parts = line.split (',')
if len(parts) < 5:
  print ('Invalid line. Some information is missing')
  print ('in line', line)
else: number_of_medals = int (parts [4])

#most python programers use the try and except block
#aka EAFP, easier to ask for permission
line = '2016, Swimming, gold, 3'
parts = line.split(',')
#run the dangerous code within the try block so that if there is an index error, the except block will run and we will see our error message
try:
  number_of_medals = int (parts [4])
except IndexError:
  print ('Invalid data, IndexError. Some information is missing')
  print ('in line:', line)
#can handle each type of error (IndexError, ValueError, NameError) seperately
except ValueError:
  print ('Invalid data, ValueError. Some information is missing')
  print ('in line:', line)
except NameError:
  print ('Invalid data, NameError. Some information is missing')
  print ('in line:', line)

#the catch all block
#code that can handle any type of error
#must be the final of the various except blocks
#use with care, can make it a lot more diffcult to fix code
  
#example below
line = '2016, Swimming, gold, 3'
parts = line.split(',')

try:
  number_of_medals = int (parts [4])
except IndexError:
  print ('Invalid data, IndexError. Some information is missing')
  print ('in line:', line)
except ValueError:
  print ('Invalid data, ValueError. Some information is missing')
  print ('in line:', line)
except:
  print ('Invalid data, NameError. Some information is missing')
  print ('in line:', line)

#the finally block, one more thing to know about erroring
#when python hits an error it stops, when we add error handling it is up to us to tell python what to do
#if processing a whole data file and there is one bad line, we can continue
#some things that you must finish if you start, such as opening a file and closing them
#what happens when there is an error while a file is open?
  """
file = open('raw_data/results.txt')
print ('File opened')
first_line = file.readline ()
print (1/0)
file.close()
print ('File closed')
print (first_line)
"""

#use finally to make sure file closes no matter what happens
#even with the divide by zero, we still close the file via the finally block
file = open('raw_data/results.txt')
print ('File opened')

try:
  first_line = file.readline ()
  print (1/1)
finally:
  file.close()
  print ('File closed')

print (first_line)