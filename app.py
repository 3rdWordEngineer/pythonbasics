# User input lines 2 - 4 are commented out
#name = input("What is your name? ")
#colour = input("What is your fav colour ? ")
#print(name + " likes " + colour)
# String concatenation
firstName = 'John'
lastName = 'Smith'
message = f'{firstName} [{lastName}] is a coder'
print(message)

# String functions
course = 'Python for Beginners'
print(len(course)) # length of string, general purpose not just strings
print(course.upper()) # all letters to  upper case
print(course.find('t')) # returns index at which the character or sequence of characters start at in this case 2, also works for numerous characters, case sensitive
print(course.replace('Beginners', 'Absolute Beginners')) # Two overloads and case sensitive
print('Python' in course) # boolean result and also case sensitive

# Arithematic operators
# +, -, / (returns double), // (returns int), % (remainder of divison), ** (exponent)
# +=, -=, *=

# Math Functions
x = 2.9
print(round(x)) # Should print 3
print(abs(-2.9)) # always returns positive value

# import math (this will import all the math functions. To use type math.(name of function)

# Conditions
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Logical operators
# AND, OR, NOT (difference is these are in words lower case

has_high_income = True
has_good_credit = True
has_kinda_good_credit = False

if has_high_income and has_good_credit:
    print("This boy is living")

if has_high_income or has_kinda_good_credit:
    print("Step your money game up")

# NOT (not) inverts a current boolean

# Comparators
# (> greater than) (< less than) (>= greater than or equal to) (<= less than or equal to) ( != not equal to)
temperature = 30

if temperature > 30:
    print("It's a hot day")

# test here
# while loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

# for loops
for item in "Python":
    print(item)

# lists are defined using square brackets. Loop through list
for name in ["Brandon", "Nicola", "Ecko"]:
    print(name)

# nested loop
for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')


# lists
names = ["John", "Bob", "Mosh", "Sarah", "Mary"] # -1 returns last item, -2 second last item

# access via indexes like all other lanuages
# returns all items from index 2 till end
print(name[2:])

# returns elements from start index till the end index EXCLUDING that index element
print(names[2:4]) # Mosh, Sarah

# returns elements start from 0 if no starting index is specified

# matrices
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# list methods



