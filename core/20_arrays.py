"""
Arrays

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
"""
cars = ["Ford", "Volvo", "BMW"]
print(cars)
# Access the Elements
x = cars[0]
print(x)
# Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)
# The Length of an Array
x = len(cars)
print(x)

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
for x in cars:
    print(x)

# Adding Array Elements
# You can use the append() method
cars.append("Honda")
print(cars)

# Removing Array Elements
# You can use the pop() method
cars.pop(1)
print(cars)

# use the remove() method to remove an element from the array.
cars.remove("Volvo")
print(cars)

"""
Array Methods

append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""