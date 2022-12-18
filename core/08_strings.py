"""
Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""

# Assign String to a Variable

a = "String Value"

# Multiline Strings

a1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

a2 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

"""
📝📝📝
Strings are Arrays
"""

a3 = "Hello, World!"
print(a3[1])

# Looping Through a String

for x in "banana":
    print("\n", x)

# String Length
a4 = "Hello, World!"
print(len(a4))

# Check String keyword `in`.
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
# Use if statement
if "free" in txt:
    print("Yes, 'free' is present.")
# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
# Both 'if' and 'not'
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

"""
Slicing Strings
"""

# From Index To Index
b = "Hello, World!"
print("1. " + b[2:5])

# Slice From the Start
b = "Hello, World!"
print("2. " + b[:5])

# Slice To the End
b = "Hello, World!"
print("3. " + b[2:])

# Negative Indexing - to start the slice from the end of the string:
b = "Hello, World!"
print("4. " + b[-5:-1])

"""
Modify Strings
"""

a = " Hello, World! "
# Upper Case
print(a.upper())
# Lower Case
print(a.lower())
# Remove Whitespace
print(a.strip())
# Replace String
print(a.replace("H", "J"))
# Split String
value = a.split(",")
print(value[0])

"""
String Concatenation
"""
a = "Hello"
b = "World"
c = a + b
print(c)

"""
String Format
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

"""
Escape Character

\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\\ooo	Octal value	
\\xhh	Hex value
"""
