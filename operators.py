#arthimatic opeators
a = 10
b = 20
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction     
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division 
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus  
print("a ** b =", a ** b)  # Exponentiation
# Comparison operators      
# These operators compare the values of two operands and return a boolean result.
print("a == b:", a == b)  # Equal to    
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to
# Logical operators
# These operators are used to combine conditional statements.
print("a > 5 and b < 30:", a > 5 and b < 30)  # Logical AND
print("a < 5 or b < 30:", a < 5 or b < 30)    # Logical OR
print("not (a > 5):", not (a > 5))              # Logical NOT
# Assignment operators  
# These operators are used to assign values to variables.
a = 10
b = 20
a += b  # a = a + b
print("a after a += b:", a)  # a = 30
b -= a  # b = b - a
print("b after b -= a:", b)  # b = -10
a *= b  # a = a * b
print("a after a *= b:", a)  # a = -300
b /= 10  # b = b / 10
print("b after b /= 10:", b)  # b = -1.0
a //= 2  # a = a // 2
print("a after a //= 2:", a)  # a = -150
b %= 3  # b = b % 3
print("b after b %= 3:", b)  # b = 1.0
a **= 2  # a = a ** 2
print("a after a **= 2:", a)  # a = 22500
# Identity operators
# These operators are used to check if two variables point to the same object in memory.        
print("a is b:", a is b)  # Identity check
print("a is not b:", a is not b)  # Identity check