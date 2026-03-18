def check_odd_even(data):
    if((data // 2) * 2 == data):
        return True
    else:
        return False

user_input = int(input('Enter the number to check : '))

result = check_odd_even(user_input)
print(result)

