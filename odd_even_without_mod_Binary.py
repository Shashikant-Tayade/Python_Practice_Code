# If the last binary digit is 0, it's even.
def check_odd_even(data):
    return (data & 1) == 0

number = int(input('Enter the number to check for Even : '))
result = check_odd_even(number)
print(result)


