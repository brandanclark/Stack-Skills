#The Basics: Functions and Conditionals
#creating a mean function
#creating a function begins with the def term
def mean(mylist):
  the_mean = sum(mylist)/ len(mylist)
  return the_mean

#print the mean
print(mean([1,2,3,4]))

#testing the type function
print(type(mean), type(sum))
#result <class 'function'> <class 'builtin_function_or_method'>

#re-create student_grades dictionary
student_grades = {"Marry": 9.1, "Joe": 2.3, "Simi": 6.9}

#intro to conditionals
#how to update the function to also consider a dictionary
def mean2(value):
  if type(value) == dict:
    the_mean = sum(value.values()) / len(value)
  else:
    the_mean = sum(value) / len(value)
  return the_mean

print(mean2(student_grades))

#can also run conditionals outside of functions
if 3 > 1:
  print("Greater")
else:
  print("Not greater")

#elif conditionals
x = 30
y = 100
if x > y:
  print("x > y")
elif x == y:
  print("x = y")
else:
  print("x < y")
