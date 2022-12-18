"""
Set - A set is a collection which is unordered, unchangeable*, and unindexed.
"""
mySet = {"apple", "banana", "cherry"}
print(mySet)

# Duplicates Not Allowed
thisSet = {"apple", "banana", "cherry", "apple"}

print(thisSet)

# Get the Length of a Set
print(len(thisSet))

# Set Items - Data Types
# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1)
print(set2)
print(set3)
print(set4)

# The set() Constructor
thisSet = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisSet)

"""
Access Set Items
"""

# using a for loop,
for x in thisSet:
    print(x)

# using the in keyword.
print("banana" in thisSet)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

"""
Add Items - Once a set is created, you cannot change its items, but you can add new items.
"""

# use the add() method.

thisSet = {"apple", "banana", "cherry"}

thisSet.add("orange")

print(thisSet)

# Add Sets

thisSet = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisSet.update(tropical)

print(thisSet)

# Add Any Iterable
# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).

thisSet = {"apple", "banana", "cherry"}
myList = ["kiwi", "orange"]

thisSet.update(myList)

print(thisSet)

"""
Remove Set Items
"""

# use the remove() method
# Note: If the item to remove does not exist, remove() will raise an error.
thisSet = {"apple", "banana", "cherry"}

thisSet.remove("banana")

print(thisSet)

# using the discard() method:
# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisSet = {"apple", "banana", "cherry"}

thisSet.discard("banana")

print(thisSet)

# You can also use the pop() method to remove an item,
# but this method will remove the last item.
# Remember that sets are unordered,
# so you will not know what item that gets removed.

# Remove the last item by using the pop() method:

thisSet = {"apple", "banana", "cherry"}

x = thisSet.pop()

print(x)

print(thisSet)

# The clear() method empties the set:
thisSet = {"apple", "banana", "cherry"}

thisSet.clear()

print(thisSet)

# The del keyword will delete the set completely:
thisSet = {"apple", "banana", "cherry"}

del thisSet

# print(thisSet) # This will raise an error

"""
Loop Sets
"""

# using a for loop:
thisSet = {"apple", "banana", "cherry"}
for x in thisSet:
    print(x)

"""
Join Sets
"""

# Join Two Sets
# You can use the union() method
# The union() method returns a new set with all items from both sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# The intersection() method will return a new set,
# that only contains the items that are present in both sets.


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# The symmetric_difference() method will return a new set,
# that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

"""
Set Methods

add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
"""