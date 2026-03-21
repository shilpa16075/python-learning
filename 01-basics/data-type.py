# Dta type define the type of data a variable can store in python
# Python Data Types Example Program

# Numeric Types
a = 10          # int (integer value)
b = 3.14        # float (decimal value)
c = 2 + 3j      # complex number

print(a, b, c)

# String Type
name = "Shilpa"   # string (text data)
print(name)

# Boolean Type
x = True          # boolean True
y = False         # boolean False
print(x, y)

# List Type (mutable)
lst = [1, 2, 3, 4]   # list can be changed
print(lst)

# Tuple Type (immutable)
tup = (1, 2, 3)      # tuple cannot be changed
print(tup)

# Set Type (no duplicates)
st = {1, 2, 3, 3}    # duplicate 3 will be removed
print(st)

# Dictionary Type (key-value pairs)
d = {"name": "Shilpa", "age": 20}
print(d)

# Type checking
print(type(a))      # check type of variable a
print(type(name))   # check type of variable name