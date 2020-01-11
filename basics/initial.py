# Hello World
print("hello world")
# Numbers
# sum
1+2
# 3
print(1+2)
# subtraction
2-1
# 1
print(2-1)
# multiplication
3*2
# 6
print(3*2)
# division
3/2
# 1.5
print(3/2)
7/4
# 1.75
print(7/4)
# Mod Operator
7%4
print(7%4)
# 3
50%5
print(50%5)
# 0


# Variables
operation = 7/4
print(operation)
# 1.75

# self sum
a = 10
a = a + 10
print(a)
# 20

#get variable class
type(a)
print(type(a))
# <class 'int'>

type(operation)
print(type(operation))
# <class 'float'>

# quotes
print('i have something to say')
# i have something to say
print("i've something to say")
# i've something to sa
print("i have something to say")
# i have something to say

# select chars in string
word = 'Hello'
print(word)
# Hello
print('Hello \tWorld')
# Hello
# World
#Indexing
print(word[0])
# H
print(word[4])
# o
print(word[-2])
# l
#Slicing
print(word[:3])
# Hel
print(word[2:])
# llo
print(word[1:4])
# ell
print(word[::4])
# Ho
print('Hello World'[-3])

# concat
print(word + ' World')
# Hello World
word = word + ' World'
print(word)
# Hello World

# strings methods
phrase = 'whats up '
print(phrase * 3)
# whats up whats up whats up
print(phrase.upper())
# WHATS UP
print(phrase.lower())
# whats up
print(phrase.split())
# ['whats', 'up']
print(phrase.split('a'))
# ['wh', 'ts up ']

# Interpolation
print('This is a string {}'.format('INSERTED'))
# This is a string INSERTED
print('The {} is {} and {}'.format('tree', 'green', 'brown'))
# The tree is green and brown
print('The {0} is {0} and {0}'.format('tree', 'green', 'brown'))
# The tree is tree and tree
print('The {0} is {2} and {1}'.format('tree', 'green', 'brown'))
# The tree is brown and green
print('The {t} is {b} and {g}'.format(t='tree', g='green', b='brown'))
# The tree is brown and green
result = 100/777
print(result)
# 0.1287001287001287
print('The result was {}'.format(result))
# The result was 0.1287001287001287
print('The result was {r:1.3f}'.format(r=result))
# The result was 0.129
name = 'Manuel'
print(f'Hello my Name is {name}')
# Hello my Name is Manuel
years = 31
print(f'{name} is {years} years old')
# Manuel is 31 years old

