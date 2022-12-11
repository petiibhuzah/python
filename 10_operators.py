"""
Python Operators

01.Arithmetic operators
02. Assignment operators
03. Comparison operators
04. Logical operators
05. Identity operators
06. Membership operators
07. Bitwise operators
"""

"""
01. Python Arithmetic Operators

+	Addition	    x + y	
-	Subtraction	    x - y	
*	Multiplication	x * y	
/	Division	    x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	 (x ** y) #same as 2*2*2*2*2
//	Floor division	x // y (x // y) - rounds the result down to the nearest whole number
"""

# **
print(2 ** 5)  # 32

# //
print(15 // 2)  # 7

"""
Python Assignment Operators

Op      Eg.         Same 
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
//=	    x //= 3	    x = x // 3	
**=	    x **= 3	    x = x ** 3	
&=	    x &= 3	    x = x & 3	BETWISE
|=	    x |= 3	    x = x | 3	BETWISE
^=	    x ^= 3	    x = x ^ 3	
>>=	    x >>= 3	    x = x >> 3	
<<=	    x <<= 3	    x = x << 3

Bitwise Operators

& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
^	XOR	Sets each bit to 1 if only one of two bits is 1
~	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""

"""
a. Binary AND(&) Operator in Python
It performs bit by bit AND operation on the two values. Here, binary for 2 is 10, and that for 3 is 11. &-ing them results in 10, which is binary for 2.

Similarly, &-ing 011(3) and 100(4) results in 000(0).
"""
print(3 & 4)  # 0

"""
b. Binary OR(|) Operator in Python
It performs bit by bit OR on the two values. Here, OR-ing 10(2) and 11(3) results in 11(3).
"""
print(2 | 3)  # 3

"""
c. Binary XOR(^) Operator in Python
It performs bit by bit XOR(exclusive-OR) on the two values. Here, XOR-ing 10(2) and 11(3) results in 01(1).
"""

print(2 ^ 3)  # 1

"""
d. Binary One’s Complement(~) in Python
It returns the one’s complement of a number’s binary. It flips the bits. Binary for 2 is 00000010. Its one’s complement is 11111101.

This is binary for -3. So, this results in -3. Similarly, ~1 results in -2.
"""

print(~1)  # -2

"""
e. Binary Left-Shift(<<) Operator in Python
It shifts the value of the left operand the number of places to the left that the right operand specifies.

Here, binary of 2 is 10. 2<<2 shifts it two places to the left. This results in 1000, which is binary for 8.
2  - 10 shift two places of the left (00) 
8 - 1000

3  - 11
12 - 1100

5   - 101
20  - 10100 
"""

print(5 << 2)  # 20

"""
f. Binary Right-Shift(>>) in Python
It shifts the value of the left operand the number of places to the right that the right operand specifies.

Here, binary of 3 is 11. 3>>2 shifts it two places to the right. This results in 00, which is binary for 0.

Similarly, 3>>1 shifts it one place to the right. This results in 01, which is binary for 1.

5  - 101
4  - 001 
"""

print(5 >> 2)  # 1

"""
Python Comparison Operators

==	Equal	                    x == y	
!=	Not equal	                x != y	
>	Greater than	            x > y	
<	Less than	                x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	    x <= y
"""

"""
Python Logical Operators

and 	Returns True if both statements are true	                x < 5 and  x < 10	
or	    Returns True if one of the statements is true	            x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
"""

"""
Python Identity Operators

is 	Returns True if both variables are the same object	            x is y	
is not	Returns True if both variables are not the same object	    x is not y
"""

print(5 is 5)
print(4 is not 56)

"""
Python Membership Operators

in 	Returns True if a sequence with the specified value is present in the object	            x in y	
not in	Returns True if a sequence with the specified value is not present in the object        x not in y
"""

values = [1, 2, 3, 4, 5]

print(3 in values)
print(45 not in values)
