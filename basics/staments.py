# Staments
#if
x = 0
y = 5

if x < y:
  print('yes')
#yes

if y < x:
  print('yes')
#yes

#if and or
if x or y:
  print('yes')
#yes

#if and and
if x and y:
  print('yes')
#yes

#if and in
if 'aul' in 'grault':
  print('yes')
#yes

if 'quux' in ['foo', 'bar', 'baz']:
  print('yes')
#yes

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('')
    print('Done.')
print('After conditional')
#After conditional

# if with guard clause
if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')

    if 10 > 20:
      print('Inner condition 1')
      print('Between inner conditions')

    if 10 < 20:
      print('Inner condition 2')
      print('End of outer condition')
print('After outer condition')
# Outer condition is true
# Inner condition 2
# End of outer condition
# After outer condition

#if and else
x = 20
if x < 50:
  print('(first suite)')
  print('x is small')
else :
  print('(second suite)')
  print('x is large')
#(first suite)
#x is small


x = 120
if x < 50:
  print('(first suite)')
  print('x is small')
else:
  print('(second suite)')
  print('x is large')

# (second suite)
# x is large

# if and elif and else
name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
  print('Hello Xander')
elif name == 'Joe':
  print('Hello Joe')
elif name == 'Arnold':
  print('Hello Arnold')
else:
  print("I don't know who you are!")
# Hello Joe

# if with multiple executions
if 'f' in 'foo': print('1'); print('2'); print('3')
# 1
# 2
# 3

if 'z' in 'foo': print('1'); print('2'); print('3')
#

x = 2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else : print('corge'); print('grault')

# qux
# quux

x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

# corge
# grault

raining = False
print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the beach

raining = True
print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the library

age = 12
s = 'minor' if age < 21 else 'adult'
print(s)
# 'minor'

print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')
# 'no'

# pass stament
if True:
    pass

print('foo')
# foo

# Loops
# For
a = 5
b = 1
while b <= 5:
	print('%d * %d = %d' %(a, b, a*b))
	b += 1

# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25

# while with break
a = 1
while a <= 3:
	b = 2
	if b == 0:
		print ("exiting loop with break command, 'else' is not executed")
		break
	a+=1
else:
	print ('loop exited without executing break command')

# loop exited without executing break command
a = 1
while a <= 3:
	b = 0
	if b == 0:
		print ("exiting loop with break command, 'else' is not executed")
		break
	a+=1
else:
	print ('loop exited without executing break command')
# exiting loop with break command, 'else' is not executed

#for loop
for a in range(10):
	print (a, end=" ")

# 0 1 2 3 4 5 6 7 8 9 

a = 5
for b in range(1, 5):
	print ("%d * %d = %d" %(a, b, a*b))

# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20

a = [10,20,30,40,50]
for b in a:
	print (b+5, end=" ")

# 15 25 35 45 55 
