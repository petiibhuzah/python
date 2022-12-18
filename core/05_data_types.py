"""
Built-in Data Types


01.Text Type:	     str
02.Numeric Types:	 int, float, complex
03.Sequence Types:	 list, tuple, range
04.Mapping Type:	 dict
05.Set Types:	     set, frozenset
06.Boolean Type:	 bool
07.Binary Types:	 bytes, bytearray, memoryview
08.None Type:	     NoneType
"""

x1 = "Hello World"  # str
x2 = 20  # int
x3 = 20.5  # float
x4 = 1j  # complex
x5 = ["apple", "banana", "cherry"]  # list
x6 = ("apple", "banana", "cherry")  # tuple
x7 = range(6)  # range
x8 = {"name": "John", "age": 36}  # dict
x9 = {"apple", "banana", "cherry", "cherry"}  # set - Has No Duplicates -
# used to convert any of the iterable to sequence of iterable elements with distinct elements
x10 = frozenset({"apple", "banana",
                 "cherry"})  # frozenset - You cant assign once the values declared/Immutable set object from iteration
x11 = True  # bool
x12 = b"Hello"  # bytes
x13 = bytearray(5)  # bytearray - Array of specified bytes
x14 = memoryview(bytes(5))  # memoryview - Best way to expose buffer protocol (pointer to memory address) / Pointer,
x15 = None  # NoneType

# print(f' X1 : {x1}, X2 : {x2}, X3 : {x3}, X4 : {x4}, X5 : {x5}, X6 : {x6}, X7 : {x7}, X8 : {x8}, '
#       f' X9 : {x9}, X10 : {x10}, X11 : {x11}, X12 : {x12}, X13 : {x13}, X14 : {x14}, X15 : {x15}')

print(
    f' X1 : {type(x1)}, X2 : {type(x2)}, X3 : {type(x3)}, X4 : {type(x4)}, X5 : {type(x5)}, X6 : {type(x6)}, '
    f'  X7 : {type(x7)}, X8 : {type(x8)}, '
    f' X9 : {type(x9)}, X10 : {type(x10)}, X11 : {type(x11)}, X12 : {type(x12)}, X13 : {type(x13)}, X14 : {type(x14)}'
    f', X15 : {type(x15)}')
"""
Setting the Specific Data Type
"""
y1 = str("Hello World")  # str
y2 = int(20)  # int
y3 = float(20.5)  # float
y4 = complex(1j)  # complex
y5 = list(("apple", "banana", "cherry"))  # list
y6 = tuple(("apple", "banana", "cherry"))  # tuple
y7 = range(6)  # range
y8 = dict(name="John", age=36)  # dict
y9 = set(("apple", "banana", "cherry"))  # set
y10 = frozenset(("apple", "banana", "cherry"))  # frozenset
y11 = bool(5)  # bool
y12 = bytes(5)  # bytes
y13 = bytearray(5)  # bytearray
y14 = memoryview(bytes(5))  # memoryview

# print(f' y1 : {y1}, y2 : {y2}, y3 : {y3}, y4 : {y4}, y5 : {y5}, y6 : {y6}, y7 : {y7}, y8 : {y8}, '
#       f' y9 : {y9}, y10 : {y10}, y11 : {y11}, y12 : {y12}, y13 : {y13}, y14 : {y14}')
