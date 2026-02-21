 # swap variable values using a temporary variable
a = input("Enter the value of a: ")

b = input("Enter the value of b: ") 

temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")  