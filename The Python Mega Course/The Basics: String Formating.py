#The Basics: String Formating
#creating a function to return "hello + a name + !"

user_input = input("What is your name? ")
#use string formatting below to allow for this to work
message = "Hello %s!" % user_input
#alternative way
message1 = "Hello {}!".format(user_input)
print(message)
print(message1)

#String formatting with multiple variables
#what if you want to get both name and surname of a user?

name = input("What is your first name?")
surname = input("What is your last name?")

message = "Hello %s %s!" % (name, surname)
message1 = "Hello {} {}!".format(name,surname)

print(message)
print(message1)