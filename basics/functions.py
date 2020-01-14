def hello_function(name = 'Name'):
  if name == 'Name':
    return "adds a name compa :v"
  else:
    a = "whats up"
    return a + ' ' + name

print(hello_function('some name'))


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