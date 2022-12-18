"""
Dictionaries - store data values in key:value pairs.
             - A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisDict)

# Dictionary Items
print(thisDict["brand"])

# Dictionaries cannot have two items with the same key:
# Dictionaries are changeable, meaning that we can change,
# add or remove items after the dictionary has been created.

# Dictionary Length
print(len(thisDict))

# Data Types
thisDict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisDict)
print(type(thisDict))

# The dict() Constructor
thisDict = dict(name="John", age=36, country="Norway")
print(thisDict)

"""
Accessing Items
"""
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisDict["model"]
y = thisDict.get("model")  # Same as above
print(x)
print(y)

# Get Keys
# Get a list of the keys:
x = thisDict.keys()
print(x)

# Add a new item to the original dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

# Get Values - return list of values
x = thisDict.values()
print("------")
print(x)

# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

# items() - return each item in a dictionary, as tuples in a list.
x = thisDict.items()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change

# Check if Key Exists
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""
Change Dictionary Items
"""

print("-----")
# Change Values
thisDict["year"] = 2018
print(thisDict)
# Update Dictionary
thisDict.update({"year": 2020})
print(thisDict)
print(type(thisDict))

"""
Add Dictionary Items
"""

# Adding Items
thisDict["color"] = "red"
print(thisDict)

# The update() method
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisDict.update({"color": "red"})

"""
Remove Dictionary Items
"""
# The pop() method removes the item with the specified key name:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisDict.pop("model")
print(thisDict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisDict.popitem()  # "year" will be removed
print(thisDict)

# The del keyword removes the item with the specified key name:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisDict["model"]
print(thisDict)

del thisDict
# print(thisDict)  # this will cause an error because "thisdict" no longer exists.

# The clear() method empties the dictionary:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisDict.clear()
print(thisDict)

"""
Loop Dictionaries
"""

# using a for loop.
print("-----Loop------")
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# Print all key names in the dictionary
for x in thisDict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisDict:
    print(thisDict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisDict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary:
for x in thisDict.keys():
    print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisDict.items():
    print(x, y)

"""
Copy Dictionaries

 You cannot copy a dictionary simply by typing dict2 = dict1,
 because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
"""

# Make a copy of a dictionary with the copy() method:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
myDict = thisDict.copy()
print(myDict)

# Another way to make a copy is to use the built-in function dict().
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
myDict = dict(thisDict)
print(myDict)

"""
Nested Dictionaries
"""

# Nested Dictionaries - A dictionary can contain dictionaries
print("-----Nested Dictionaries------")
myFamily = {
    "child1": {
        "name": "Emil Daniel",
        "year": 2004
    },
    "child2": {
        "name": "Tobias Daniel",
        "year": 2007
    },
    "child3": {
        "name": "Linus Daniel",
        "year": 2011
    }
}
print(myFamily)

# or
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myFamily)

"""
Dictionary Methods

clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""