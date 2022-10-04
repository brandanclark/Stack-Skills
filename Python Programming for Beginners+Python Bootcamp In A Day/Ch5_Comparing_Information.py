#COMPARING INFORMATION
#not all data is clean, often times need to compare data to iteslf or different versions in order to ensure data makes sense
#using < and > to perform logial tests
year = 216
print (year > 2000)
print (year < 2020)
print (2000 < 2020)

#using boolean variables to perform logical tests
year = 216
correct_number = True
print(correct_number)
correct_number = (2000 < year < 2020)
print(correct_number)
#logical tests are run one at a time, if any of them fail then false is printed
correct_number = (2000 < 2012 < 2020)
print(correct_number)

#can also check if a variable has an exact value
#== compares two values
year = 2016
print (year == 2016)
print (year == 2012)

#when comparing text, it will be done alpabetically
print ('C' > 'B')
print ('Hello' < 'OMG')

#variables are boxes, one variable can have multiple names
#id function gives the id/phone number/memory address of a variable/box
value_a = 12345
value_b = 12345
nickname_a = value_a
print (value_a == value_b)
print (nickname_a == value_a)
print (nickname_a == value_b)