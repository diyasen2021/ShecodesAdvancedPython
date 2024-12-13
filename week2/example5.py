# Exception handling

try:
  file = open('cities.txt', 'r')

  content = files.read()
except FileNotFoundError:
  print("cannot find the file")

try: 
  12 / 0
except ZeroDivisionError:
  print('cannot divide number by 0')

try: 
  a + b
except Exception:
  print('something went wrong')

print("hello world")