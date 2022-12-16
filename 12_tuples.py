"""
Tuples - store multiple items in a single variable.
       - one of 4 built-in data types in Python used to store collections of data.
       - The other 3 are List, Set, and Dictionary

A tuple is a collection which is ordered and unchangeable.

There are four collection data types in the Python programming language:

List        is a collection which is ordered and changeable. Allows duplicate members.
Tuple       is a collection which is ordered and unchangeable. Allows duplicate members.
Set         is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary  is a collection which is ordered** and changeable. No duplicate members.
"""

# Create a Tuple:
thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Tuples allow duplicate values:
thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thisTuple)

# Tuple Length
print(len(thisTuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.

thisTuple = ("apple",)
print(type(thisTuple))

# NOT a tuple
thisTuple = ("apple")
print(type(thisTuple))

# Tuple Items - Data Types

# Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

thisTuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisTuple)

"""
Access Tuple Items
"""
thisTuple = ("apple", "banana", "cherry")
print(thisTuple[1])

# Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.

print(thisTuple[-1])

# Range of Indexes
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[2:5])

# From beginning To 'n'
print(thisTuple[:4])

# From 'n' To End:
print(thisTuple[2:])

# Range of Negative Indexes
print(thisTuple[-4:-1])

# Check if Item Exists
thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
    print("Yes, 'apple' is in the fruits tuple")

"""
Update Tuples
 - Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
"""

# Change Tuple Values
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items
thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.append("orange")
thisTuple = tuple(y)
print(thisTuple)
# Remove Items
y = list(thisTuple)
y.remove("apple")
thisTuple = tuple(y)
print(thisTuple)
# The 'del' keyword can delete the tuple completely:
# del thisTuple
# print(thisTuple) #this will raise an error because the tuple no longer exists

"""
Unpack Tuples - When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
              - To extract the values back into variables, is called "unpacking"
"""

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)  # This will be a List

# If the asterisk is added to another variable name than the last,
# will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

"""
Loop Tuples
"""
# using a for loop.
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)

# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.

for i in range(len(thisTuple)):
    print(thisTuple[i])

# Using a While Loop
# Use the len() function to determine the length of the tuple

i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i = i + 1

"""
Join Tuples
"""
# Join Two Tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
myTuple = fruits * 2

print(myTuple)

"""
Tuple Methods

count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
"""