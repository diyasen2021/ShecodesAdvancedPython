# File Handling in Python

## **1. Reading a File**
To read the contents of a file, you can use the `open()` function.

```python
# Open the file
file = open('cities.txt', 'r')
cities = file.readlines()

# More Pythonic approach using 'with'
with open('cities.txt', 'r') as file:
    lines = file.readlines()

# Loop through and process each line
for city in cities:
    print(f"I want to visit {city.strip()}")

# Always close the file when using 'open'
file.close()
```

---

## **2. Methods to Read File Contents**
Python offers different methods for reading files:

- **Using `read()`**: Returns the entire file contents as a single string.
```python
with open('TODO.txt', 'r') as file:
    contents = file.read()
print(type(contents))  # Output: <class 'str'>
```

- **Using `readlines()`**: Returns a list of all lines in the file.
```python
with open('TODO.txt', 'r') as file:
    contents = file.readlines()
print(type(contents))  # Output: <class 'list'>
```

- **Using `strip()`**: Removes trailing newline or whitespace characters.
```python
for line in contents:
    print(line.strip())
```

---

## **3. Reading CSV Files**
To work with CSV files, Python provides the `csv` module.

```python
import csv

# Reading a CSV file using csv library
with open('Giants.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
```

---

## **4. Writing and Appending to Files**
Python supports different modes for file operations:
- `'r'`: Read (default).  
- `'w'`: Write (overwrites the file).  
- `'a'`: Append (adds to the file).  

### **Writing to a File with `'w'` Mode**
The `'w'` mode is used to write to a file. It **overwrites** the file if it already exists or creates a new file if it does not exist.

**Example 1: Writing a Simple String**  
```python
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new file created using Python.\n")
```

**Example 2: Writing Multiple Lines**  
You can write multiple lines by using `write()`. Ensure each line ends with a newline character (`\n`).

```python
lines = ["Line 1: Python is fun.\n", "Line 2: File handling is useful.\n", "Line 3: Practice makes perfect.\n"]
with open('example.txt', 'w') as file:
    file.write(lines)
```

**Example 3: Overwriting File Contents**  
Using `'w'`, any existing content in the file will be replaced.

```python
# Before: example.txt contains previous text
with open('example.txt', 'w') as file:
    file.write("The previous content is now replaced with this line.\n")
```

### **Appending to a File with `'a'` Mode**
The `'a'` mode is used to add content to an existing file without overwriting it.

**Example:**
```python
with open('example.txt', 'a') as file:
    file.write("This line is appended to the file.\n")
```

---

## **5. Exception Handling in File Operations**
Always handle exceptions to avoid runtime errors.

**Examples:**
- Handling a missing file:
```python
try:
    file = open('cities.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("Cannot find the file")
```

- Handling a division error:
```python
try:
    12 / 0
except ZeroDivisionError:
    print("Cannot divide number by 0")
```

- Handling general exceptions:
```python
try:
    a + b
except Exception as e:
    print(f"Something went wrong: {e}")

print("hello world")
