"""
Boolean Values

True or False.
"""

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

# Most Values are True
print("--True Values---")
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# Some Values are False
print("--False Values---")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

"""
  value, or object in this case, evaluates to False, 
  and that is if you have an object that is made 
  from a class with a __len__ function that returns 0 or False:
"""


class TestClass:
    def __len__(self):
        return 0


myObject = TestClass()
print("Here " + str(bool(myObject)))


class TestClassWithFunctionReturningBoolean:
    def testFunction(self):
        return True


object2 = TestClassWithFunctionReturningBoolean()
print(object2.testFunction())
