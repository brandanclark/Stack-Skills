#The Basics: Processing User Input
#define weather function

def weather_condition(temperature):
  if temperature > 70:
    return "Warm"
  else: 
    return "Cold"

print(weather_condition(80))

#but this is not very useful if we do not allow for input
user_input = input("What is the temperature?")

#when you use the input function, it will freeze the output at the input command

print(user_input)

#print out the weather with the user input
#errors because the user_input is currently a string
#change user_input to be a float
user_input = float(input("What is the temperature?"))

#now it all works
print(weather_condition(user_input))

