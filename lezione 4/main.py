# OPERANDS
## Arithmetic Operators
print(2+1) 
print(2*1) 
print(2-1) 
print(2/2) 
print(2%2) # This gives me the remainder of the division
print(2**2) # This is 2 to the power of two 
print(14//3) # Floor division (approximated to the smallest integer) - Returns a int

# all these operators are binary, but + and - can be used as UNARY operators too
a = 5
print(-a)

# +, - and * return an int ONLY if all the terms are ints, otherwise they return float
# / returns ALWAYS a float

# priority: * and / have more priority than + and -

# powers use right-side binding> from right to left so it's 1**3 and then 2**1
print(2**1**3) # = > 2

# We can also write something like this
price = 2
price = price + 2.5
price += 2.5

# + and * can also be used for strings
print("Hello" + " World")

# the asterisk operator used for strings does a replication
print("hello"*3) # hellohellohello

# number = int(input())
# print(number)


a = "ciao"
b = 5
print(a + str(b))

# truthy e falsity
print(bool("")) # => False
print(bool(0)) # => False
print(bool(None)) # => False

print(bool("True")) # => True
print(bool("False")) # => True

# Comparison Operator
# They Always return a boolean
a = 10
print(a>1) # strict
print(a<1) # strict
print(a>=1) # non strict
print(a<=1) # non strict
print(a==1) # equivalence
print(a!=1) # different than
print("Ananas">"kiwi") # This is use whichever unicode character code comes first

# Comparison Operator
# They take boolean or truthy/falsity
print(True and False)
print("" or 1)

# not operator
print(not True) # => False

is_admin = False
is_moderator = True
is_banned = True
is_allowed = is_admin or is_moderator and not is_banned # Not has more priority, and and or have the same

# priority
# 1. **     (arithmetic operator: exponential)
# 2. ~      (bitwise operator: negation)
# 3. other arithmetic operators
# 4. other bitwise operators
# 5. comparison operators
# 6. logical operators 

# Bitwise operators
# They work bit per bit

register_1 = 0b10101011
register_2 = 0b01100110
register_3 = register_1 & register_2 # conjunction operator returns 1 if both bit are 1
print(register_3) #00100010 The print will convert that to decimal anyway
print(bin(register_3)) # This converts that to the binary form
register_3 = register_1 | register_2 # bitwise or
register_3 = register_1 ^ register_2 # bitwise xor
~register_1 # bitwise not
register_2 >> 1 # shift operation, it translates to the right of one position
register_2 << 1 # shift operation, it translates to the left of one position