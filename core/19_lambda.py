"""
Lambda

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax

lambda arguments : expression
"""
# Example
y = lambda x: x + 10
print(y(90))

# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b
print(x(5, 6))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:

# Example
def my_function(n):
    return lambda a: a * n


myDoubler = my_function(2)

print(myDoubler(11))


# Example
def my_function(n):
    return lambda a: a * n


myTripler = my_function(3)

print(myTripler(11))


# use the same function definition to make both functions, in the same program:

# Example
def my_function(n):
    return lambda a: a * n


myDoubler = my_function(2)
myTripler = my_function(3)

print(myDoubler(11))
print(myTripler(11))
