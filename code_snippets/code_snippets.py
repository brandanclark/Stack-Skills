# Figure 6.3 and 6.4
year = 216
if year < 2000:
    print('Incorrect year', year)
print('Done')

# Figure 6.5
if 5:
    print("Executing the first 'if' block")

if 0:
    print("Executing the second 'if' block")

print('Done')

# Figure 6.7
name = 'Fred'
if name:
    print('Hello', name)

name = ''
if not name:
    print('Hello stranger')

# Figure 6.10 - 6.13
name = 'Fred'
if name == 'Fred':
    print('Hi Fred, good to see you again')
else:
    if name:
        print('Hi', name, 'welcome')
    else:
        print('Hello stranger')

# Figure 6.14, 6.15
name = ''
if name == 'Fred':
    print('Hi Fred, good to see you again')
elif name == 'Sue':
    print('Hello Sue, how have you been?')
elif name:
    print('Hi', name, 'welcome')
else:
    print('Hello stranger')

# Figure 7.9
names = []
print('Starting list', names)

names.append('Fred')
names.append('Sue')
print('First two names added', names)

names.append('Sam')
names.append('Alex')
print('Two more names added', names)

# Figure 7.10
numbers = [0, 1, 2, 3, 4]
print('Starting list', numbers)

numbers.insert(0, 25)
print('Inserted 25 at start', numbers)

numbers.insert(3, 40)
print('Inserted 40 at index 3', numbers)

# Figure 7.12
numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[2:])
print(numbers[:3])
print(numbers[::-2])

# Figure 7.24
numbers = [0, 1, 2, 3, 4, 5]
numbers[2] = 22
print(numbers)

# Figure 7.25
numbers = (0, 1, 2, 3, 4, 5)
numbers[2] = 22
print(numbers)

# Figure 7.29 - 7.34
discipline_definitions = {}
discipline_definitions['Athletics'] = 'A collection of sporting events ' + \
                                       'that involve competitive running,' + \
                                       ' jumping, throwing, and walking'
print(discipline_definitions)

discipline_definitions['Football / Soccer'] = 'A family of team sports that involve, to varying degrees, kicking a ball to score a goal'
discipline_definitions['Volleyball'] = "A team sport in which two teams of six players are separated by a net. Each team tries to score points by grounding a ball on the other team's court under organized rules"
print(discipline_definitions)

print(len(discipline_definitions))

print(discipline_definitions['Volleyball'])

discipline_definitions['Volleyball'] = "A sport in which two teams of six players are separated by a net. Each team tries to score points by grounding a ball on the other team's court under organized rules"
print(discipline_definitions)

# Figure 7.35
shapes = {
    'ball': 'round',
    'box': 'square',
    'bottle': 'cylinder',
    'paper': 'flat',
    'string': 'line',
    'pyramid': 'triangle',
    'apple': 'round'
}
print(shapes)
print()

del shapes['paper']
print('Just deleted paper')
print(shapes)

# Figure 7.36 - 7.38
shapes = {
    'ball': 'round',
    'box': 'square',
    'bottle': 'cylinder',
    'paper': 'flat',
    'string': 'line',
    'pyramid': 'triangle',
    'apple': 'round'
}
for key in shapes.keys():
    print(key)

print('------------------------')

for value in shapes.values():
    print(value)

print('------------------------')

for key, value in shapes.items():
    print('a', key, 'has a', value, 'shape')

# Figure 7.39
result = {
    'year': 2012,
    'discipline': 'Gymnastics',
    'country': 'United States',
    'medal_type': 'gold',
    'number_of_medals': 2
}

print('In ', result['year'], result['country'], 'won',
      result['number_of_medals'], result['medal_type'],
      'medal(s) in', result['discipline'])

# Figure 8.40, 'lines' variable also used in later figures
# Only part of the full data is included here
# For the full data, see the other .py files
lines = """2012,Rowing,Hungary,gold,1
2012,Gymnastics,United States,gold,2
2008,Gymnastics,Australia,silver,4
2012,Swimming,Belgium,silver,4
2016,Football / Soccer,Sweden,silver,2
2016,Synchronized Swimming,Finland,gold,2
2004,Gymnastics,Australia,gold,2
2016,Football / Soccer,Italy,bronze,0
2012,Modern Pentathlon,Cuba,bronze,6
2004,Swimming,Soviet Union,silver,5
2016,Modern Pentathlon,Canada,bronze,4
2008,Football / Soccer,Finland,silver,4
2016,Swimming,Austria,silver,1
2012,Cycling,Austria,silver,5
2016,Swimming,East Germany,silver,3
2008,Athletics,Austria,bronze,6
2004,Rowing,Bulgaria,s,0
2008,Volleyball,Turkey,bronze,2
2004,Athletics,Norway,silver,2
2008,Football / Soccer,Great Britain,bronze,2
2008,Rowing,Cuba,bronze,2
2012,Cycling,Austria,bronze,5
8,Athletics,South Korea,gold,1
2016,Cycling,Canada,silver,6
2004,Rowing,West Germany,gold,6
2016,Football / Soccer,Italy,silver,3
2004,Rowing,Bulgaria,gold,5
2004,Football / Soccer,Germany,bronze,4
2008,Gymnastics,Italy,g,1
2004,Cycling,Australia,silver,6
2004,Gymnastics,Commonwealth of Independent States,bronze,4
2004,Swimming,Belgium,silver,6
2008,Cycling,United States,gold,2
2004,Football / Soccer,Bulgaria,silver,1
2008,Tennis,Denemark,gold,2
2016,Athletics,Finland,gold,0
2008,Rowing,Bulgaria,s,2
4,Football / Soccer,Bulgaria,gold,2
2016,Athletics,Netherlands,silver,6
2004,Swimming,Finland,bronze,4
2004,Athletics,Czechoslovakia,bronze,1
2004,Cycling,Netherlands,gold,1
2012,Swimming,West Germany,gold,5
16,Synchronized Swimming,Netherlands,gold,4
2016,Cycling,Sweden,s,5
2008,Gymnastics,Bulgaria,bronze,4
2016,Gymnastics,Hungary,gold,0
2004,Swimming,Belgium,gold,6
2016,Cycling,Australia,gold,2
2004,Volleyball,Commonwealth of Independent States,silver,4
2008,Volleyball,Netherlands,bronze,0
2016,Athletics,Norway,bronze,4
2008,Cycling,Turkey,bronze,0
2008,Synchronized Swimming,Australia,bronze,4
2004,Cycling,Hungary,silver,0
2004,Synchronized Swimming,Commonwealth of Independent States,bronze,2
2008,Swimming,West Germany,gold,1
2012,Football / Soccer,East Germany,silver,1
2004,Tennis,Commonwealth of Independent States,bronze,2
2016,Synchronized Swimming,Romania,silver,0
2012,Football / Soccer,Norway,bronze,6
2016,Swimming,Turkey,gold,3
2012,Athletics,Japan,silver,0
2012,Gymnastics,Netherlands,bronze,5
2004,Swimming,West Germany,bronze,5
2008,Swimming,Russia,gold,1
2004,Football / Soccer,Soviet Union,gold,5
2004,Swimming,Australia,bronze,1
2008,Modern Pentathlon,East Germany,bronze,4
2004,Cycling,China,silver,5
2016,Gymnastics,Austria,silver,3
2008,Swimming,East Germany,bronze,6
2008,Gymnastics,Canada,bronze,0
2012,Synchronized Swimming,Czechoslovakia,silver,5
2016,Athletics,South Korea,bronze,2
2008,Cycling,Finland,gold,0
2016,Synchronized Swimming,Great Britain,gold,5
2012,Football / Soccer,Hungary,bronze,2
12,Swimming,Switzerland,bronze,1
2012,Synchronized Swimming,Japan,gold,0
2008,Rowing,Netherlands,gold,2
2012,Cycling,France,silver,6
2004,Athletics,Bulgaria,gold,4
2012,Athletics,Finland,gold,5
2004,Gymnastics,Germany,bronze,2
2016,Swimming,Canada,silver,4
2012,Cycling,West Germany,gold,5
2012,Volleyball,Bulgaria,silver,5
2008,Rowing,Norway,gold,1
2004,Gymnastics,United States,bronze,0
2008,Volleyball,Sweden,silver,5
2004,Volleyball,Hungary,silver,3
2008,Football / Soccer,Switzerland,silver,0
2016,Synchronized Swimming,East Germany,bronze,1
2008,Modern Pentathlon,Switzerland,silver,2
2008,Cycling,Australia,bronze,2
2016,Synchronized Swimming,Soviet Union,bronze,3
2016,Synchronized Swimming,Russia,bronze,4
2008,Athletics,Soviet Union,silver,5
2016,Tennis,China,gold,0
2012,Cycling,United States,bronze,2
2012,Tennis,Austria,silver,6
2008,Synchronized Swimming,Russia,gold,5
2004,Football / Soccer,Denemark,gold,4
2012,Tennis,Norway,bronze,4
2008,Cycling,South Korea,gold,4
2004,Synchronized Swimming,Finland,gold,0
2004,Cycling,Sweden,bronze,2
2004,Modern Pentathlon,Bulgaria,silver,5
2008,Gymnastics,Japan,bronze,1
2004,Volleyball,Soviet Union,silver,0
2008,Rowing,Norway,silver,6
2004,Tennis,Austria,silver,5
2004,Synchronized Swimming,Japan,silver,1
2012,Modern Pentathlon,Commonwealth of Independent States,silver,2
2008,Swimming,Commonwealth of Independent States,silver,4
2008,Football / Soccer,Switzerland,bronze,5
2016,Football / Soccer,Czechoslovakia,gold,0
2008,Cycling,Commonwealth of Independent States,bronze,3
2004,Tennis,Soviet Union,silver,4
2012,Tennis,Sweden,silver,5
2012,Cycling,Finland,bronze,2
2012,Rowing,Sweden,bronze,1
2012,Modern Pentathlon,Switzerland,gold,6
2016,Tennis,Austria,gold,3
2016,Volleyball,Czechoslovakia,bronze,4
2008,Athletics,Australia,gold,2
2004,Athletics,Denemark,gold,1
2004,Football / Soccer,Norway,silver,1
2008,Swimming,Hungary,gold,2
2016,Gymnastics,Czechoslovakia,gold,3
2008,Cycling,Sweden,silver,1
2008,Swimming,Canada,bronze,5
2016,Gymnastics,Great Britain,silver,5
2016,Tennis,Great Britain,bronze,5
2004,Tennis,Cuba,silver,5
2004,Rowing,Hungary,gold,6
2008,Synchronized Swimming,Netherlands,bronze,5
2004,Volleyball,Australia,gold,1
2008,Modern Pentathlon,Denemark,silver,1
2004,Synchronized Swimming,Czechoslovakia,gold,1
2012,Football / Soccer,Switzerland,gold,2
2012,Athletics,Turkey,bronze,0
2008,Volleyball,Switzerland,bronze,6
2012,Cycling,Switzerland,bronze,6
2016,Synchronized Swimming,Russia,gold,1
2016,Volleyball,Finland,bronze,3
2004,Gymnastics,Netherlands,gold,2
2008,Cycling,Italy,silver,0
2016,Football / Soccer,Austria,gold,0
2016,Gymnastics,Norway,bronze,0
2016,Rowing,East Germany,bronze,5
2012,Rowing,Canada,silver,5
2016,Swimming,Soviet Union,silver,4
2008,Athletics,Denemark,gold,6"""
lines = lines.split('\n')

# Figure 7.40. 'results' variable also used in later figures
results = []

for line in lines:
    parts = line.split(',')

    year = int(parts[0])
    discipline = parts[1].strip()
    country = parts[2].strip()
    medal_type = parts[3].strip()
    number_of_medals = int(parts[4])

    single_result = {}
    single_result['year'] = year
    single_result['discipline'] = discipline
    single_result['country'] = country
    single_result['medal_type'] = medal_type
    single_result['number_of_medals'] = number_of_medals

    results.append(single_result)

# Figure 7.43, 7.44
print(results[0])
print(results[10])

print(len(results))

# Figure 7.45
numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers.index(50))

# Figure 7.46
numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
del numbers[3]
print(numbers)

# Figure 7.47
medal_types = set()
for result in results:
    medal_types.add(result['medal_type'])

print(medal_types)

# Figure 7.48, 7.49
for result in results:
    if result['medal_type'] == 'b':
        result['medal_type'] = 'bronze'
    elif result['medal_type'] == 's':
        result['medal_type'] = 'silver'
    elif result['medal_type'] == 'g':
        result['medal_type'] = 'gold'

medal_types = set()
for result in results:
    medal_types.add(result['medal_type'])

print(medal_types)


# Figure 7.50
years = set()
for result in results:
    years.add(result['year'])

print(years)

# Figure 7.51, 7.53
for result in results:
    year = result['year']
    if year < 100:
        year += 2000
        result['year'] = year

years = set()
for result in results:
    years.add(result['year'])

print(years)

# Figure 8.3, 8.4, 8.5
alert_count = 0
for result in results:
    number_of_medals = result['number_of_medals']

    if 0 <= number_of_medals <= 5:
        continue

    alert_count += 1

    if alert_count > 5:
        continue

    print(result)

# Figure 8.6, 8.7. Numbers made smaller to speed this up a little
import random
numbers = [random.randint(0, 50_000_000) for _ in range(10_000_000)]
print(numbers[:10])

for number in numbers:
    if number == 3098213:
        print('Found')
        break
else:
    print('Not found')

# Figure 8.11
for number in range(1, 5):
    print(number, '_____________')

# Figure 8.12
print(list(range(5)))
print(list(range(3)))

# Figure 8.13
print(list(range(1, 3)))
print(list(range(-3, 5)))

# Figure 8.14
print(list(range(0, 20, 2)))
print(list(range(10, 0, -1)))

# Figure 8.15
reply = '2000'
while reply:
    reply = int(reply)
    if reply in [2008, 2016, 2004, 2012]:
        for result in results[:15]:
            if result['year'] == reply:
                print(result)
    reply = input('Year? ')

# Figure 9.5
line = '2016,Swimming,gold,3'
parts = line.split(',')
try:
    number_of_medals = int(parts[4])
except IndexError:
    print('Invalid line. Some information is missing')
    print('In line:', line)

# Figure 9.6 - 9.9
line = '2016,Swimming,Norway,gold,'
try:
    number_of_medals = int(parts[4])
except IndexError:
    print('Invalid line. Some information is missing')
    print('In line:', line)
except ValueError:
    print('Invalid line. The year and number of medals must be shown as numbers')
    print('In line:', line)
except:
    print('Failed to get the number of medals')
    print('In line:', line)

# Figure 11.1
def say_hello():
    print('Hello')

say_hello()
say_hello()

# Figure 11.2
def print_unique_values(results, fieldname):
    unique_values = set()
    for result in results:
        value = result[fieldname]
        unique_values.add(value)
    print(fieldname, unique_values)


print_unique_values(results, 'year')
print_unique_values(results, 'discipline')
print_unique_values(results, 'number_of_medals')

# Figure 11.3 - 11.7
def print_twice(some_text):
    print(some_text)
    print(some_text)

print_twice('Hello')

print_twice('Good morning')

greeting = 'How are you?'
print_twice(greeting)

# Figure 11.8
def print_twice(some_text):
    print(some_text)
    print(some_text)

some_text = 'This is not printed'
print_twice('Printed this will be')

# Figure 11.9
def print_twice(some_text):
    print(introduction_text)
    print(some_text)
    print(some_text)

introduction_text = 'Good morning'
print_twice('How are you?')

# Figure 11.10
def count_to_five():
    number = 0
    while number <= 5:
        print(number)
        number = number + 1

    print('At the end of count_to_five, number is', number)

number = 1234
count_to_five()
print('Back in the main code, number is', number)

# Figure 11.11, 11.12
def say_something_friendly(name, time_of_day):
    print('Good', time_of_day, ',', name)

say_something_friendly('Sue', 'morning')
say_something_friendly('John', 'evening')

# Figure 11.14
def say_something_friendly(name, time_of_day):
    print('Good', time_of_day, ',', name)

say_something_friendly(time_of_day='morning', name='Sue')
say_something_friendly(time_of_day='evening', name='John')

# Figure 12.5
data = [ (1, 5), (1, 3), (1, 4), (2, 10), (2, 0)]
data.sort()
print(data)

# Figure 12.28
name = 'Fred'
greeting = f'Hello {name}, how are you?'
print(greeting)

# Figure 12.29
some_calculation = f'5 times 3 = {5 * 3}'
print(some_calculation)

# Figure 13.31
one_third = 1/3
print(one_third)
print(f'{one_third:5.2}')

# Figure 13.1
pi = 10
print(pi)
from math import pi
print(pi)

# Figure 13.2
pi = 10
print(pi)
from math import *
print(pi)
