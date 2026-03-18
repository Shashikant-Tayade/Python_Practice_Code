# Reverse data using slicing.(String and Numbers allowed)

# Taking input from user.
userinput =  input("Enter the data to reverse : ")

# Reversing input
rev = userinput[::-1]

# check if userinput and rev are same and print result 
if(userinput == rev):
    print(f"{userinput} is palindrome")
else:
    print(f"{userinput} is not palindrome")
    