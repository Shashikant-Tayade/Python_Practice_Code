num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

print(f"Befor Swapping : a = {num1}, num 2 = {num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After Swapping : a = {num1}, num 2 = {num2}")