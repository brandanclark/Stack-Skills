#INDEXING
#creating an object named line to test out text reading
line = '2004, Athletics, Norway, Gold, 3'
#create variable final_position as shorthand to finding medals count
final_position = len(line) - 1
print (line [final_position])
#can also use Python shorthand of [-1] to go backwards from the end, using a negative index
print(line[-1])

#SLICES
#create a slice of the year by combinging the first four characters
year = line[0] + line[1] + line[2] + line[3]
print(year)
#alternative method using colons, leave the space before the first colon blank to start at the beginning of the characters
print(line[:4])
print(line[2:15])
#useing the third number in a slice to pull data of a certain stepsize
print(line[::2])
#step can alos be negative, returning the text backwards, even every other letter backwards
print(line[::-2])

#STRING FUNCTIONS
#using string functions to find specific bits of data
#string of line has a method of find
print(line.find(','))
#use find to search for a given index within a string, starting at position 5
print (line.find(',', 5))
#combine the two searches to find text between commas irregardless of length
first_comma_possition = line.find(',')
second_comma_possition = line.find(',', first_comma_possition + 1)
print(first_comma_possition)
print(second_comma_possition)
#print the values between the first and second comma possitions
print(line [first_comma_possition: second_comma_possition])
#remove the extra comma and space
print(line [first_comma_possition + 2: second_comma_possition])
#simpler way of doing this using SPLIT method
#we select it to split on commas, if we do not select, it will split on spaces
parts = line.split(',')
#returns a python list of the different texts?
print(parts)
#print just the first text value
print(parts[0])
#or the second text value
print(parts[1])
#assign the parts as a variable
country = parts[2]
print(country)
#use .strip method to remove unwanted spaces
print(country.strip())

#THE INPUT FUNCTION
#input function asks the user a question and then stores the answer
age = input('How old are you?')
#asks how old you are and then stores it as a variable
print(age)

#MORE STRING OPERATIONS
greeting = 'How are you?'
name = 'Sam'
print(greeting + name)
#need to add a space manually
print(greeting + ' ' + name)
#can also duplicate string
print (name * 10)
#change to upper or lower case
discipline = 'Athletics'
print('The winner in', discipline.lower(), 'is...' )
print(discipline.upper(), 'was won by....')