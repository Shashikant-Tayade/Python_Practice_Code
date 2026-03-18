# Reverse number or string making function

def universal_reverse(user_input):
   s = str(user_input)

   if(s.startswith('-')):
      only_digits = s[1:]
      reversed_nums = only_digits[::-1]
      final_ans = '-'+reversed_nums
      return final_ans
   else:
      return s[::-1]
   

# --- Main Program ---
print("--- Universal Reverser (Type 'exit' to quit) ---")

while True:
   user_input = input('Enter the data to reverse : ')
   if(user_input.lower() == 'exit'):
      print('GoodBye!')
      break
   result = universal_reverse(user_input)

   print(f"Original : {user_input}")
   print(f"Reverse : {result}")

