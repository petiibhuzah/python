"""
For Loops
"""
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
for x in "banana":
    print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
for x in range(6):  # values 0 to 5.
    print(x)

for x in range(2, 6):  # values 2 to 5
    print(x)

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):  # 3 is increment
    print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
print("----------")
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
# for loops cannot be empty,
# but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass
