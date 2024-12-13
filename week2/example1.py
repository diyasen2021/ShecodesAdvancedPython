# Reading a file

# Open the file
file = open('cities.txt', 'r')
cities = file.readlines()

# or more Pythony approach
with open('cities.txt', 'r') as file:
  lines = file.readlines()

# loop all the cities
for city in cities:
  print(f"I want to visit {city.strip()}")

# Close the file
file.close()