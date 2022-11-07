#learning Python is about learning three things
#1. Syntax
#2. Data structures for your scenario
#3. The algorithms you are using

#here is a list
#student_grades = [9.1, 8.8, 7.5]

#here is a dictionary
student_grades = {"Mary": 9.1, "Alex": 8.8, "James": 7.5}

#to get the sum, need to find the .values method of a dictionary
mysum=sum(student_grades.values())
mylen=len(student_grades.values())
student_avg=mysum/mylen
print(student_avg)

#how to show the keys of a dictionary
print(student_grades.keys())

#exercise: create list
temperatures = [70, 56.2, 88.9, "warm"]
print(temperatures)

#exercise: create complex list
rainfall = [55.2, 33, "no data", [22, 23, 24]]
print(rainfall)

#exercise: calculate maximum value of student grades
student_grades = [9.1, 8.8, 7.5]
max_value = max(student_grades)
print(max_value)

#exercise: count values
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
count_grades = student_grades.count(10.0)
print(count_grades)

#exercise: modify string to print lower case
username = "Python3"
print(username.lower())


