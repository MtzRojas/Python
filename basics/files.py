#text Files
# open file
myfile = open('example_file.txt')

#read file
file_string = myfile.read()
print(file_string)
# Hello
# one line
# another line

#use read again
print(myfile.read())
# ''

# reposition to the beggin of the document
print(myfile.seek(0))
# 0
print(myfile.read())
# Hello
# one line
# another line

#red document line by line
print(myfile.seek(0))
print(myfile.readlines())
# ['Hello\n', 'one line\n', 'another line ']

# close file and out from memory
myfile.close()

#another way to open
with open('example_file.txt') as my_new_file:
  contents = my_new_file.read()
  
print(contents)
# Hello
# one line
# another line

with open('example_file.txt', mode = 'a') as f:
  f.write('\nanother other line')
  
with open('example_file.txt') as f:
  print(f.read())
# Hello
# one line
# another line
# another other line
