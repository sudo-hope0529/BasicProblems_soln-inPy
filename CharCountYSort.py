from collections import Counter

# For counting characters in a sentence and sorting them based on their counts
def SortBasedOnValueYKey(char_counts):

   sorted_char_counts = sorted(char_counts.items(), key=lambda item: (-item[1], item[0]))
   return sorted_char_counts


# Main
sentence = input("Enter Sentence: ")
sorted_char_counts = SortBasedOnValueYKey(Counter(sentence.lower()))

if sorted_char_counts:
   for letter, count in sorted_char_counts:
      if letter != ' ':
         print(f"{letter}: {count}")
else:
   print("No chars to print...")
