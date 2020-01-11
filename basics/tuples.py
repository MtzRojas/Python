#Tuples
# Creating tuples 
tup = 'python', 'geeks'
print(tup) 
# ('python', 'geeks')
tup = ('python', 'geeks') 
print(tup) 
# ('python', 'geeks')

# Code for concatenating 2 tuples 
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
print(tuple1 + tuple2) 
# ((0, 1, 2, 3), ('python', 'geek'))

# Code for creating nested tuples 
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
tuple3 = (tuple1, tuple2) 
print(tuple3) 
# ((0, 1, 2, 3), ('python', 'geek'))

# Code to create a tuple with repetition 
tuple3 = ('python')*3
print(tuple3) 
# ('python', 'python', 'python')

# code to test slicing 
tuple1 = (0 ,1, 2, 3) 

print(tuple1[1:]) 
# (1, 2, 3)

print(tuple1[::-1])
# (3, 2, 1, 0) 

print(tuple1[2:4]) 
# (2, 3)

# Code for printing the length of a tuple 
tuple2 = ('python', 'geek') 
print(len(tuple2)) 
# 2

# Code for converting a list and a string into a tuple 
list1 = [0, 1, 2] 
print(tuple(list1)) 
# (0, 1, 2)

print(tuple('python')) # string 'python' 
# ('p', 'y', 't', 'h', 'o', 'n')