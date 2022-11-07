#The Basics: Operations with Data Types
#using lists
monday_temperatures = [9.1, 8.8, 7.5]
#.append
monday_temperatures.append(8.1)
print(monday_temperatures)

#.clear
monday_temperatures.clear()
print(monday_temperatures)

#.index
monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures.index(8.8))
print(monday_temperatures.index(8.8,0))

#accessing list items
print(dir(list))

#use __getitem__
print(monday_temperatures.__getitem__(1))
print(monday_temperatures[1])

#accessing list slices
print(len(monday_temperatures))
print(monday_temperatures[2:])

#how do we get the last item of a list
print(monday_temperatures[-1])

#accessing characters and slices in strings
monday_temperatures = ["hello", 1, 2, 3]
#to access the character within a string
print(monday_temperatures[0][2])

#accessing items in dictionaries
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
#using a search item to find a value in a dictionary
print(student_grades["Sim"])
