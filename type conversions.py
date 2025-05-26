#type conversion
#they are 2 types of type conversion
# implicit type conversion
# explicit type conversion
# implicit type conversion
# This code demonstrates implicit and explicit type conversion in Python.
a= 10        # Integer
b = 3.14     # Float
c = "20"     # String
# Implicit type conversion
result1 = a + b  # Integer to Float conversion
result2 = a + int(c)  # String to Integer conversion
print("Implicit type conversion results:")
print("a + b =", result1)  # Output: 13.14
print("a + int(c) =", result2)  # Output: 30
# Explicit type conversion
result3 = float(a) + b  # Integer to Float conversion
result4 = str(a) + c  # Integer to String conversion
print("Explicit type conversion results:")
print("float(a) + b =", result3)  # Output: 13.14
print("str(a) + c =", result4)  # Output: "1020"
# This code demonstrates type conversions in Python.
# It shows how to convert between different data types using both implicit and explicit methods.
# Implicit type conversion
# is done automatically by Python, while explicit type conversion requires the use of functions like int(), float(), and str().
# This code demonstrates type conversions in Python.
# It shows how to convert between different data types using both implicit and explicit methods.