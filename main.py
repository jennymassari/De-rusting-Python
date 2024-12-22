'''
Here's a study guide to practice core Python syntax.

For each task, beneath the comment write the code and print out the result to check it works
'''

'''LISTS'''

# Create a list and assign it to a variable
words = ['hello', 'world', 'python']

# Find the length of the list
print(len(words))

# Append an item to the list
words.append('programming')

# Find the value of an item in the list a specific index
print(words[3])

# Set the value of an item at a specific index
words[0] = 'hi'

# Check whether an item is in the list
print('python' in words)

# Sort the list
words.sort() # sorts the list in place
print(words)
sorted_list = sorted(words) # returns a new sorted list
print(sorted_list)

# Iterate over the list using range, printing out each element and the index
for i in range(len(words)):
    print(i, words[i]) # prints the index and the element

# Iterate over the list without using range, printing out each element
for word in words:
    print(word)

'''TUPLES'''

# Create a tuple and assign it to a variable
chores = ('wash dishes', 'clean bathroom', 'vacuum')
# Find the length of the tuple
print(len(chores))
# Find the value of an item in the tuple a specific index
print(chores[1])
# Check whether an item is in the tuple
print('vacuum' in chores)
# Iterate over the tuple using range, printing out each element and the index
for i in range(len(chores)):
    print(i, chores[i])
# Iterate over the tuple without using range, printing out each element
for chore in chores:
    print(chore)

'''STRINGS'''

# Create a string and assign it to a variable
greeting = 'hello'

# Find the length of the string
print(len(greeting))
# Find the value of a character in the string a specific index
print(greeting[1])
# Check whether an item is in the string
print('h' in greeting)
# Concatenate (add) two strings together
name = 'world'
concatenated = greeting + name
print(concatenated)
# Create an f-string
print(f"{greeting} {name}!")

# Split a string using .split
# The .split() method in Python is used to split a string into a list of substrings based on a specified delimiter. 
# By default, it splits by any whitespace.
# the .split() method is specifically a string method and can only be used on string objects. 
# It cannot be used on other iterables like lists, tuples, or sets.

text = "hello world python programming"
split_text = text.split()  # Splits by whitespace
print(split_text)  # Output: ['hello', 'world', 'python', 'programming']
print(len(split_text))  # Output: 4

# Split by a specific delimiter
# split_text_by_o = text.split('o')
# print(split_text_by_o)  # Output: ['hell', ' w', 'rld pyth', 'n pr', 'gramming']
# ...existing code...

# Split a string by a comma
csv_text = "apple,banana,cherry,dates"
split_csv = csv_text.split(',')  # Splits by comma
print(split_csv)  # Output: ['apple', 'banana', 'cherry', 'dates']

# Join a list of strings using .join
# The .join() method in Python is used to concatenate a list of strings into a single string, 
# with a specified separator between each element.
# The .join() method is typically used on lists of strings, 
# but it can be used on any iterable of strings (e.g., tuples, sets).

print(type(split_text)) # Output: <class 'list'>
print(type(' '.join(split_text)))
joined_text = ' '.join(split_text)  # Joins by whitespace
print(joined_text)  # Output: hello world python programming
print(type(joined_text)) # Output: <class 'str'>

# Iterate over the string using range, printing out each character and the index
for i in range(len(csv_text)):
    print(i, csv_text[i])
# Iterate over the string without using range, printing out each character
for char in csv_text:
    print(char)

'''DICTIONARIES'''

# Create a dictionary and assign it to a variable

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Find the length of the dictionary
# The len() of a dictionary returns the number of key-value pairs in the dictionary.
print(len(my_dict)) # Output: 3

# Add a new key/value pair
my_dict['country'] = 'USA'

# Replace value for a given key
my_dict['city'] = 'Los Angeles'

# Check whether a key is in the dictionary

print('name' in my_dict) # Output: True

# Iterate over keys, printing each key
# Iterating over a dictionary in Python will iterate over its keys by default.
for key in my_dict:
    print(key)
# Iterate over values, printing each value
for value in my_dict.values():
    print(value)

# Iterate over over key/value pairs using .items(), printing each key and value
for key, value in my_dict.items():
    print(key, value)

'''SETS'''

# Create a set and assign it to a variable
topping_set = {'cheese', 'pepperoni', 'mushrooms'}

# Find the length of the set
print(len(topping_set))

# Add a new element
topping_set.add('sausage')

# Remove an element
topping_set.remove('mushrooms')

# Check whether a element is in the set
print('cheese' in topping_set)

# Iterate over elements, printing each one out
for topping in topping_set:
    print(topping)

'''NUMBERS'''

# Add / subtract / multiply 2 numbers
addition = 2 + 3
subtraction = 5 - 2
multiplication = 2 * 3

# Divide two numbers using normal (float) division
division = 5 / 2
print(division)

# Divide two numbers using integer division
integer_division = 5 // 2
print(integer_division)

# Find the modulo (remainder) of two numbers
modulo = 5 % 2
print(modulo)

# Check whether a number is even/odd
print(5 % 2 == 0) # Odd
print(6 % 2 == 0) # Even
# Round a float down to an int
rounded_down = int(5.9)
print(rounded_down)

# Round a float up to an int
print(round(5.9))

'''FUNCTIONS'''

# Write a function that takes no arguments and call it
def say_hello():
    print('Hello!')

say_hello()

# Write a function that takes one or more arguments and call it
def greet(name):
    print(f'Hello, {name}!')
greet('Alice')

# Write a function that returns a value. Call the function and store the return value in a variable
def add(a, b):
    return a + b
result = add(2, 3)
print(result)
'''LOOPS'''

# Write a while loop
while True:
    print('Hello!')
    break

# Write a for loop that loops a set number of times (e.g. 10 times)
for i in range(10):
    print(i)    

'''CONDITIONALS'''

# Write an if/elif/else statement
age = 30
if age < 18:
    print('You are a minor')
elif age < 65:
    print('You are an adult')
else:
    print('You are a senior citizen')

# Write conditionals for the following operators:
# ==
if 2 == 2:
    print('2 is equal to 2')
# !=
if 2 != 3:
    print('2 is not equal to 3')
# <
if 2 < 3:
    print('2 is less than 3')
# >
if 3 > 2:
    print('3 is greater than 2')
# <=
if 2 <= 2:
    print('2 is less than or equal to 2')
# >=
if 3 >= 2:
    print('3 is greater than or equal to 2')

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second
print(nested_list[1][2])
# Iterate through the nested data structure using range
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        # retrieve the element at the current row and column
        print(nested_list[i][j])
        # retrieve the row and column indices
        print(i, j)

# Iterate through the nested data structure without using range 
for row in nested_list:
    for element in row:
        print(element)

'''REMINDER'''

# You're doing great and you got this!
