# Variable Swapping: Write a Python program to swap the values of two variables using a third temporary variable.


num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print(f"Before swapping : a = {num1}, b = {num2}")

num3 = num1
num1 = num2
num2 = num3

print(f"BefAfterore swapping : a = {num1}, b = {num2}")
