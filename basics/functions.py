# hello function
def hello_function(name = 'Name'):
  if name == 'Name':
    return "adds a name compa :v"
  else:
    a = "whats up"
    return a + ' ' + name

print(hello_function('some name'))

#moxitho function
def myfunc(string):
    list = tuple(string)
    output = []
    i = 1
    for index in range(len(list)):
        character = list[index]
        char = character.lower() if index%2 == 0 else character.upper()
        output.append(char)
        index += 1
    return "".join(output)
    
print(myfunc('SuperLOL'))

# This allows you to find the maximum number out of the 3 numbers, it doesn't have to be 3!
def max_of_three(*numbers):
    number_list = list(numbers)
    max_number = max(number_list)
    if max_number == 3: 
      final_number = max(number_list.pop(max_number))
    else:
      final_number = max_number
    return final_number
print(max_of_three(8, 10, -9))

# This sums all the numbers in a list
def sum_numbers(*numbers):
  sum(numbers)
print(sum_numbers(2, 4, 6, 8, 10))

# This multiplies all the numbers in a list
def multiply(*numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply(1, 2, 3, 4, -5))

# This reverses a string
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('Superlol :V'))

# This function to calculates the factorial of a number (a non-negative integer). The function accepts the number as an argument

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

# This function checks whether a number is in a given range
def test_range(n):
    if n in range(3,9):
        print( "{} is in the range".format(n))
    else :
        print("The number is outside the given range.")
test_range(5)

# This prints a string and calculates the amount of upper and lower case letters within that string
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('Rajive is a Clash Royale Legend')

# This function takes a list and returns the new list with unique elements
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

# This checks whether the number is a prime number
def check_prime(n):
  return True if n%2 == 0 else False     
print(check_prime(7))

# This prints out the even numbers from a given list
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# This checks whether a number is perfect or not
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))

# This checks whether a word, phrase, or sequence that reads the same backward as forward
def is_a_palindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(is_a_palindrome('aza')) 

# This prints out the first n rows of Pascal's triangle
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6) 

# This whether words or sentences containing every letter of the alphabet at least once
import string, sys
def is_a_pangram(str, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str.lower())
 
print ( is_a_pangram('The quick brown fox jumps over the lazy dog')) 