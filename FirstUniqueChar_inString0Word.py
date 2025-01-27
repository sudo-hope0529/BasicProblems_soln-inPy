from typing import Counter

# Function to find first non-repeating character in a given string or word
def FirstUniqueValue(str):
   str_list = dict(Counter(str.lower()))   # converts str into dict with their occurance counts in given order
   for i in str_list:
      if i.isalpha():              # Ensures that only letters are checked and searched
         if str_list[i] == 1:      # check if occurance count of character is single only
            return i

# Main Function
str = input("\nEnter String to find first Non-repeating Character: ")

firstUniqueValue = FirstUniqueValue(str)

if firstUniqueValue:
   print(f"The First non-repeating Character in Given strings is: {firstUniqueValue}\n")
else:
   print("There is no non-repeating character.\n")
