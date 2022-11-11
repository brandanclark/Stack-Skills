#The Basics: Loops
#how to make a program that rounds all of the numbers in a list

monday_temperatures = [9.1, 8.8, 7.6]

#how to access items in a list? 
#could use the logic below, but inefficient
print(round(monday_temperatures[0]))
print(round(monday_temperatures[1]))
print(round(monday_temperatures[2]))

#instead, use a for loop
#loops allow you to create a variable and then go through the loop
for temperature in monday_temperatures:
  print(round(temperature))

#could also use a string
for letter in 'hello':
  print(letter.title())

#looping in a dictionary is a bit more complex
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

#to get the items, as a tuple
for grades in student_grades.items():
  print(grades)

#to get the values
for grades in student_grades.values():
  print(grades)

#to get the keys
for grades in student_grades.keys():
  print(grades)

#can also combine a dictionary for loop with string formatting
phone_numbers = {"John Smith": "+19807797463", "Mary Jones": "+14953033433"}
for key, value in phone_numbers.items():
  print("{} has a phone number {}".format(key, value))

#for loops run as long as runs until a container is exhausted
#while loops run as long as a condition is true, this will run forever
#a = 3
#while a > 0:
#  print(1)
  
#in the real world, while loops have much better functionality
username = ''

#while loops end when the condition is no longer true
#when the while loop ends, due to the condition no longer being in agreement, it moves on to the next line, and therefore prints "successful login"
while username != "pypy":
  username = input("Enter username: ")
print("successful login")

#can also do this using break logic
while True:
  username = input("Enter username: ")
  if username == "pypy":
    break
  else:
    continue