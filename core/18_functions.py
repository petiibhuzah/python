"""
Functions

1. A function is a block of code which only runs when it is called.
2. You can pass data, known as parameters, into a function.
3. A function can return data as a result.
"""


# Creating a Function
# def keyword:
def my_function():
    print("Hello from a function")


# Calling a Function
my_function()


# Arguments
# Information can be passed into functions as arguments.
def my_function(fname):
    print(fname + " Kilimba")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments
def my_function(first_name, last_name):
    print(first_name + " " + last_name)


my_function("Peter", "Daniel")


# Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
    print("The Email is " + kid["email"])


my_function(fname="Tobias", lname="Refsnes", email="petiibhuzah@gmail.com")


# Default Parameter Value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# The pass Statement
# function definitions cannot be empty,
# but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def my_function():
    pass


# Recursion
#  It means that a function calls itself.
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
