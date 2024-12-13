# Writing to a file

# Appending
with open('cities.csv', 'a') as file:
  file.write("\n")
  file.write("London,20,cloudy\n")
  file.write("Calcutta, 40, rainy")