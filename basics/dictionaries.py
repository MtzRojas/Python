
#Dictionaries

#create
a = {'joe' : 85 , 'peter' : 88 , 'jack' : 90}
b = dict(joe = 90 , peter = 85 , jack = 88)
c = dict( [('joe' , 90), ('peter' , 85), ('jack' , 95)])

print(a)
# {'joe': 85, 'peter': 88, 'jack': 90}
print(b)
# {'joe': 90, 'peter': 85, 'jack': 88}
print(c)
# {'joe': 90, 'peter': 85, 'jack': 95}

#Adds list in Dictionary
a = {'joe' : 85 , 'peter' : 88 , 'jack' : 90, 'anothers' : ['philp', 'jhon', 'Anne']}
print(a)
# {'joe': 85, 'peter': 88, 'jack': 90, 'anothers': ['philp', 'jhon', 'Anne']}
a = {'joe' : 85 , 'peter' : 88 , 'jack' : 90, 'anothers' : ['philp', 'jhon', 'Anne'], 'others_one' : {'inside' : 'key'}}
print(a)
# {'joe': 85, 'peter': 88, 'jack': 90, 'anothers': ['philp', 'jhon', 'Anne'], 'others_one': {'inside': 'key'}}

#Acces to key
a = {'joe' : 85 , 'peter' : 88 , 'jack' : 90, 'anothers' : ['philp', 'jhon', 'Anne']}
print(a['anothers'])
# ['philp', 'jhon', 'Anne']

# remove key and value
del a['jack']
print(a)
# {'joe': 85, 'peter': 88, 'anothers': ['philp', 'jhon', 'Anne']}

#convert dictionario into a string
a = str(a)
print(a)
# '{'joe': 85, 'peter': 88, 'jack': 90}'

print(a[0:5])
# {'joe

# check for key
print('peter' in a)
# True

print('michel' not in a)
# True

print('kriss' in a)
# False

#use method get
a = {'joe' : 85 , 'peter' : 88 , 'jack' : 90}
b = a.get('peter',0)
print (b)
# 88

#get() method will return the value of the given key if that key is present, else it will return the second argument. 
c = a.get('kris',0)
print (c)
# 0 

#Extract Keys
b = a.keys()
print(b)
# dict_keys(['joe', 'peter', 'jack'])

#Extract Vlues
b = a.values()
print(b)
# dict_values([85, 88, 90])

#conver dictionary into a list
print (list(b))
# [85, 88, 90]

# Dictionary with lists
marks = {'peter': [80,85,90], 'jose' : [85,90,95]}

print(marks['jose'])
# [85, 90, 95]

print(marks['jose'][0])
# 85

marks['jose'][0] = 86
print(marks)
# {'jose': [86, 90, 95], 'peter': [80, 85, 90]}

marks2= {'jose' : {'maths': 85 , 'english': 90, 'science' : 95} , 'peter' : {'marks': 80 , 'english':85 , 'science': 90}}
print(marks2['jose']['science'])
# 95

marks2['jose']['science'] = 96
print(marks2)
# {'jose': {'science': 96, 'maths': 85, 'english': 90}, 'peter': {'science': 90, 'marks': 80, 'english': 85}}

# create a empty dic
from collections import defaultdict
marks3 = defaultdict(dict)

# adds keys with list
marks3['jose']['maths'] = 85
marks3['jose']['science'] = 95
marks3['peter']['maths'] = 80
marks3['peter']['english'] = 85
print(marks3)
# defaultdict(<class 'dict'>, {'jose': {'science': 95, 'maths': 85}, 'peter': {'maths': 80, 'english': 85}})

print(marks3['jose']['science'])
# 95