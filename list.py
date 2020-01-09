# Making a list:
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
#Accessing elements:

# Getting the first element
first_col = colors[0]
print(first_col)
# Red
# Getting the second element
second_col = colors[1]
print(second_col)
# Blue
# Getting the last element
newest_col = colors[-1]
print(second_col)
# Blue

# Modifying individual items:
# Changing an element
print(colors)
# ['Red', 'Blue', 'Green', 'Black', 'White']

colors[0] = 'Yellow'
print(colors)
# ['Yellow', 'Blue', 'Green', 'Black', 'White']

colors[-2] = 'Red'
print(colors)
# ['Yellow', 'Blue', 'Green', 'Red', 'White']

# Adding elements:
# Adding an element to the end of the list
print(colors)
# ['Red', 'Blue', 'Green', 'Black', 'White']

colors.append('Orange')
print(colors)
# ['Red', 'Blue', 'Green', 'Black', 'White', 'Orange']

# Starting with an empty list
colors = []
print(colors)
# []

colors.append('Red')
print(colors)
# ['Red']

colors.append('Blue')
print(colors)
# ['Red', 'Blue']

colors.append('Green')
print(colors)
# ['Red', 'Blue', 'Green']

# Inserting elements at a particular position
colors.insert(0, 'Violet')
print(colors)
# ['Violet', 'Red', 'Blue', 'Green']

colors.insert(2, 'Purple')
print(colors)
# ['Violet', 'Red', 'Purple', 'Blue', 'Green']

# Removing elements:
# Deleting an element by its position
print(colors)
# ['Violet', 'Red', 'Purple', 'Blue', 'Green']

del colors[-1]
print(colors)
# ['Violet', 'Red', 'Purple', 'Blue']

# Removing an item by its value
colors.remove('Red')
print(colors)
# ['Violet', 'Purple', 'Blue']

# Popping elements:
# Pop the last item from a list
print(colors)
# ['Violet', 'Purple', 'Blue']

most_recent_col = colors.pop()
print(most_recent_col)
# Blue

# Pop the first item in a list
first_col = colors.pop(0)
print(first_col)
# Violet

# List length:
# Find the length of a list
print(colors)
# ['Purple']

num_colors = len(colors)
print("We have " + str(num_colors) + " colors.")
#We have 1 colors.

# Sorting a list:
# Sorting a list permanently
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
print(colors)
# ['Red', 'Blue', 'Green', 'Black', 'White']

# Sorting a list temporarily
print(sorted(colors))
# ['Black', 'Blue', 'Green', 'Red', 'White']

print(sorted(colors, reverse=True))
# ['White', 'Red', 'Green', 'Blue', 'Black']

# Looping through a list:
# Printing all items in a list
for col in colors:
 print(col)
# Red
# Blue
# Green
# Black
# White

# Printing a message for each item, and a separate message afterwards
for col in colors:
 print("Welcome, " + col + "!")
print("Welcome, we're glad to see you all!")
# Welcome, Red!
# Welcome, Blue!
# Welcome, Green!
# Welcome, Black!
# Welcome, White!
# Welcome, we're glad to see you all!

# The range() function:
# Printing the numbers 0 to 10
for num in range(11):
 print(num)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Printing the numbers 1 to 10
for num in range(1, 11):
 print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Making a list of numbers from 1 to a million
nums = list(range(1, 1000001))
# print(nums)
# [1... 1000001]

# Simple statistics:
# Finding the minimum value in a list
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
num_min = min(nums)
print(num_min)
# 1

# Finding the maximum value
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
num_max = max(nums)
print(num_max)
# 82

# Finding the sum of all numbers
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
total_num = sum(nums)
print(total_num)
# 388

# Slicing a list:
# Getting the first three items
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
first_three = colors [:3]
print(first_three)
# ['Red', 'Blue', 'Green']

# Getting the middle three items
middle_three = colors[1:4]
print(middle_three)
# ['Blue', 'Green', 'Black']

# Getting the last three items
last_three = colors[-3:]
print(last_three)
# ['Green', 'Black', 'White']

# Copying a list:
# Making a copy of a list
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
copy_of_colors = colors[:]
print(colors)
# ['Red', 'Blue', 'Green', 'Black', 'White']
print(copy_of_colors)
# ['Red', 'Blue', 'Green', 'Black', 'White']

# List of Comprehensions:
# Using a loop to generate a list of square numbers
squr = []
for x in range(1, 11):
 sq = x**2
 squr.append(sq)

print(squr)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using a comprehension to generate a list of square numbers
squr = [x**2 for x in range(1, 11)]
print(squr)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using a loop to convert a list of names to upper case
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = []
for cols in colors:
 upper_cols.append(cols.upper())
print(upper_cols)
# ['RED', 'BLUE', 'GREEN', 'BLACK', 'WHITE']

# Using a comprehension to convert a list of names to upper case
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = [cols.upper() for cols in colors]
print(upper_cols)
# ['RED', 'BLUE', 'GREEN', 'BLACK', 'WHITE']