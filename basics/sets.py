# Sets
myset = set()
myset.add(1)
print(myset)
# {1}
myset.add(2)
print(myset)
# {1, 2}
myset.add(2)
print(myset)
# {1, 2}

#Sets have uniq values
mylist = [1,2,3,5,1,2,3,1,2,3,2,1]
another_set = set(mylist)
print(another_set)
# {1, 2, 3, 5}

#Sets split strings by characters
string = 'Python'
print(set(string))
# {'y', 'P', 'h', 'o', 'n', 't'}