# Reversing a given string while removing spaces @cleaned_string

user_string = input("Enter a string: ")
cleaned_string = ''

for letter in user_string:
   if letter != ' ':
      cleaned_string += letter

reverse_cleaned_str = cleaned_string[-1::-1]

print("Reversed Cleaned string is: ", reverse_cleaned_str)
