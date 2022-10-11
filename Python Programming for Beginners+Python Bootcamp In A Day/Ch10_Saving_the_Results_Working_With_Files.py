#Ch 10: Saving the Results - Working With Files
#added bad data to the last few rows of the raw_data/results.txt file in order to create an error
#to open a file
"""
#files open in read mode by default
file = open ('raw_data/results.txt')

#open a file in write mode
#when doing this, python will create a new, empty file
output_file = open ('clean_data/results.txt', 'w')
"""

#read the raw_data and check each line, if we can break it up and process it we will store it into clean_data/results while all errors will go to clean_data/errors

#open the file and read it
input_file = open ('raw_data/results.txt')
#readlines method reads all the lines as a list of lines
lines = input_file.readlines ()
input_file.close()

#open the clean and error files
output_file = open ('clean_data/results.txt', 'w')
error_file = open ('clean_data/errors.txt', 'w')

#loop over all the lines in the liest
for line in lines:
#try to split the line and process each individual element
  try:
    parts = line.split (',')
    single_result = {
      'year': int (parts [0]),
      'discipline': parts [1].strip(),
      'country': parts [2].strip(),
      'medal_type': parts [3].strip(),
      'number_of_medals': int (parts [4])
    }
#if above lines are successful, will continue to  below
    output_file.write (line)
#if there is a problem in the above code, go straight to the except code below
  except:
    error_file.write (line)

#close the files below
output_file.close ()
error_file.close ()

#files are by default opened in text mode
#when interacting with a file in text mode, some characters can be treated oddly
#can also open a file in binary mode, used for non-text files like images, videos, etc
#example of opening a file in binary mode
#file = open('woods.pnd', 'rb')
#when opening a file in binary mode, must specify the read, write or append mode
#rb = read
#wb = write
#ab = append

#text file modes
#when opening a file in append mode, anything you write will be added to the end of the file
#the 'w' at the end of the open logic shows the mode
#when opening a file in write mode, you overwrite the existing data
#open a file and write one thing
file = open ('sample_log.txt', 'w')
file.write('First line\n')
file.close()
#then open a file and write something else
file = open ('sample_log.txt', 'w')
file.write ('Second line\n')
file.close()
#when reading the file, only 'Second line' appears
file = open ('sample_log.txt')
text = file.read ()
file.close()
print (text)

#write to  a file in append mode instead:
#open it first in write mode
file = open ('sample_log.txt', 'w')
file.write('First line\n')
file.close()
#then open in append mode and write something else
file = open ('sample_log.txt', 'a')
file.write ('Second line\n')
file.close()
#when reading the file now, both lines appear
file = open ('sample_log.txt')
text = file.read ()
file.close()
print (text)

#extra notes about text file modes
"""
file.read() reads eveything into one single string line for a text file or a sequnce of bytes for a binary file
file.readlines() reads all the lines into a list of strings
file.readline() reads the next line and returns an empty string when all lines have been read

to write information to a file, use the following:
file.write(string or bytes) writes the string or bytes to a file
file.writelines(list of strings) writes the strings in the list of a file, one after another
"""

#the with statement
#when using the with block, python will still close the file no matter what
#try to always use the with block when opening files
with open ('raw_data/results.txt') as file:
  lines = file.readlines()

print (len (lines), 'lines found')