def check_palindrome(data):
    s = str.lower(data)
    original = s
    rev = s[::-1]

    if original == rev:
        return True
    else:
        return False
    
user_input = input("Enter the data to check for palindrome : ")
result = check_palindrome(user_input)
print(f"result : {result}")
