import csv

# Read customers.csv and print out in specific format
with open('customers.csv', 'r') as file:
  csv_contents = csv.reader(file)
  for row in csv_contents:
    print(f'Customer #{row[0]}, {row[2]} {row[3]}, {row[9]}')
    