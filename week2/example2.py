# Different methods to read file contents

#read method returns all contents in a single string
with open('TODO.txt', 'r') as file:
  contents = file.read()
print(type(contents))

# readlines will return a list of all lines in file
with open('TODO.txt', 'r') as file:
  contents = file.readlines()
print(type(contents.strip())) # strip will remove newlines 
