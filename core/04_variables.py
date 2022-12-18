# Declaration of Variable
x = 4
x = "Ibhuzah"
print(f' The Value of X is {x}')

# Variable Casting
x = str(5)
y = int('5')
z = float(7)

print(f' X : {x}, Y : {y}, Z : {z}')

# Get The Type of The Variable
# Types in Python are classes
print(f' X : {type(x)}, Y : {type(y)}, Z : {type(z)}')

"""
VARIABLE NAMES
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

username = "Peter Daniel"
userName = "Peter Daniel"  # ✅ Camel Case - My Favourite
user_name = "Peter Daniel"  # Snake Case
_userName = "Peter Daniel"
_user_name = "Peter Daniel"
USERNAME = "Peter Daniel"
userName1 = "Peter Daniel"
UserName = "Peter Daniel"  # Pascal Case

"""
Assign Multiple Values
"""

# Many Values to Multiple Variables
x, y, z = "One", "Two", "Three"

# One Value to Multiple Variables
x1 = y1 = z1 = "One Value"

# Unpack a Collection
values = [1, 2, 3]
x2, y2, z2 = values

# Output Variables
print(x)
print(x, y, z)
print(x1 + y1 + z1)

"""
Python - Global Variables
"""
gx = "Global Value"


def my_function():
    global anotherGX
    anotherGX = "Using global keyword"
    print(f'This is {gx}')
    print(f'Another Global variable {anotherGX}')


my_function()
