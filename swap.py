#swap usin g a temporary variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = b
b = a
a = temp
print(f"After swapping: a = {a}, b = {b}")


#swap without using a temporary variable
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))
b = b+a
a = b-a
b = b-a
print(f"value of a after swapping: {a}")
print(f"value of b after swapping: {b}")