"""
Python Collections (Arrays)

1. List        is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple       is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set         is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary  is a collection which is ordered** and changeable. No duplicate members.
"""
thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)

# List Length
print(len(thisList))

# List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)

# The list() Constructor
list5 = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(list5)

"""
Access List Items
"""

# 01. Access Items
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[1])

# 02. Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.

print(thisList[-3])

# 03. Range of Indexes
# When specifying a range, the return value will be a new list with the specified items.
print(thisList[2:5])

# CASE I: FROM THE BEGINNING
print(thisList[:4])

# CASE I: TO THE END
print(thisList[4:])

# 04. Range of Negative Indexes
print(thisList[-4:-1])  # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

# 05. Check if Item Exists
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")

"""
Change List Items
"""

# Change Item Value
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

# Change a Range of Item Values
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList[1:2] = ["blackcurrant", "watermelon"]
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList[1:3] = ["watermelon"]
print(thisList)

# Insert Items - The insert() method - Does not replace
thisList = ["apple", "banana", "cherry"]
thisList.insert(2, "watermelon")
print(thisList)

"""
Add List Items
"""

# Append Items - To add an item to the end of the list, use the append() method:
thisList.append("orange")
print(thisList)

# Insert Items - seen

# Extend List - To append elements from another list to the current list, use the extend() method.
thisList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

# Add Any Iterable - The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).

thisList = ["apple", "banana", "cherry"]
thisTuple = ("kiwi", "orange")
thisList.extend(thisTuple)
print(thisList)

# Remove List Items - The remove() method removes the specified item.

thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

# Remove Specified Index - The pop() method removes the specified index.

thisList = ["apple", "banana", "cherry"]
thisList.pop(1)
print(thisList)

# If you do not specify the index, the pop() method removes the last item.
thisList = ["apple", "banana", "cherry"]
thisList.pop()
print(thisList)

# The del keyword also removes the specified index:
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

# Delete the entire list:
del thisList

# Clear the List - The clear() method empties the list.
# The list still remains, but it has no content.

thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)

"""
Loop Lists
"""

# for loop:
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x + "\n")

# Loop Through the Index Numbers - Use the range() and len() functions
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print(thisList[i])

# Using a While Loop - Use the len() function to determine the length of the list
thisList = ["apple", "banana", "cherry"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1

# Looping Using List Comprehension
thisList = ["apple", "banana", "cherry"]
[print(x) for x in thisList]

"""
List Comprehension - offers a shorter syntax when you want to create a new list based on the values of an existing list.

Syntax

newList = [expression for item in iterable if condition == True]
"""

# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# With List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if "a" in x]
print(newList)

# Condition - Filter that only accepts the items that valuate to True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if x != "apple"]
print(newList)

# With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits]
print(newList)

# Iterable - The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:
newList = [x for x in range(10)]
print(newList)

# Accept only numbers lower than 5:
newList = [x for x in range(10) if x < 5]
print(newList)

# Expression - is the current item in the iteration
#            - but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x.upper() for x in fruits]
print(newList)

# Set all values in the new list to 'hello':
newList = ['hello' for x in fruits]
print(newList)

# Return "orange" instead of "banana":
newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)

"""
Sort Lists
"""

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

newList = ["orange", "mango", "kiwi", "pineapple", "banana"]
newList.sort()
print(newList)

# Sort the list numerically:

newList = [100, 50, 65, 82, 23]
newList.sort()
print(newList)

# Sort Descending - To sort descending, use the keyword argument reverse = True:
newList = ["orange", "mango", "kiwi", "pineapple", "banana"]
newList.sort(reverse=True)
print(newList)
newList = [100, 50, 65, 82, 23]
newList.sort(reverse=True)
print(newList)


# Customize Sort Function - by using the keyword argument key = function.

# Example: Sort the list based on how close the number is to 50:

def lowestCloseNumberSort(n):
    return abs(n - 50)


newList = [100, 50, 65, 82, 23]
newList.sort(key=lowestCloseNumberSort)
print(newList)

# Case Insensitive Sort
# By default the sort() method is case sensitive,
# resulting in all capital letters being sorted before lower case letters:

newList = ["banana", "Orange", "Kiwi", "cherry"]
newList.sort()
print(newList)

# Perform a case-insensitive sort of the list:
newList = ["banana", "Orange", "Kiwi", "cherry"]
newList.sort(key=str.lower)
print(newList)

# Reverse Order - The reverse() method reverses the current sorting order of the elements.

newList = ["banana", "Orange", "Kiwi", "cherry"]
newList.reverse()
print(newList)

"""
Copy Lists

You cannot copy a list simply by typing list2 = list1, 

because: list2 will only be a reference to list1,

and changes made in list1 will automatically also be made in list2.

"""
print("---------Copy List---------")
# There are ways to make a copy, one way is to use the built-in List method copy().
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)

# Another way to make a copy is to use the built-in method list().

thisList = ["apple", "banana", "cherry"]
myList = list(thisList)
print(myList)

"""
Join Lists

There are several ways to join, or concatenate, two or more lists.
"""
print("---------Join Two Lists---------")
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by
# appending all the items from list2 into list1, one by one:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""
List Methods 

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""