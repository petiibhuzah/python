import random

"""
Python Numbers


There are three numeric types in Python:

1. int
2. float
3. complex

"""

x1 = 45  # int
x2 = 67.90  # float
x3 = 67j  # complex

# print(f'x1 : {x1}, x2 : {x2}, x3 : {x3}')

# Int - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
y1 = 1
y2 = 35656222554887711
y3 = -3255522

# Float Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
y4 = 1.10
y5 = 1.0
y6 = -35.59

"""
📝📝📝
Float can also be scientific numbers with an "e" to indicate the power of 10.
"""
y7 = 35e3
y8 = 12E4
y9 = -87.7e100

# print(f'y1 : {y1}, y2 : {y2}, y3 : {y3}'
#       f' y4 : {y4}, y5 : {y5}, y3 : {y6}'
#       f' y7 : {y7}, y8 : {y8}, y9 : {y9}')

"""
Type Conversion

You can convert from one type to another with the int(), float(), and complex() methods:
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

"""
print(random.randrange(1, 10))
