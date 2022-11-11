#Putting the Pieces Together: Building a Program
#problem statement: create a function that will allow for input of different phrases and returns the phrases in a list complete with formatting

#start by making a function that formats sentances
def sentance_maker(phrase):
  capitalized = phrase.capitalize()
#program has to decide if we are asking a question or not
#do this using the startswith method
#create a tuple of interrogatives to check
  interrogatives = ("how", "what", "why", "when", "who", "where")
  if phrase.startswith(interrogatives):
    return "{}?".format(capitalized)
#if it does not start with an interrogative, it is just a normal sentance
  else:
    return "{}.".format(capitalized)

#create empty list to eventually put phrases into
results = []

#create a while loop asking for user information
while True:
  user_input = input("Say something: ")
#ask for more information until someone inserts the \end
  if user_input == "\end":
    break
#so long as the user does not input \end, continue appending the inputs to the results list, using the sentance_maker function
  else:
    results.append(sentance_maker(user_input))

#print everything after formatting it and joining them together
print(" ".join(results))
