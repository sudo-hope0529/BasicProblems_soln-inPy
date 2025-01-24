# function for reversing Words in Sentence or string...
def reverseWordsOfStr(str):
   word, reverse_sent ='', ''
   for letter in str:
      if letter.isdigit() or letter.isalpha() or letter.isalnum():
         word += letter
      else:
         reverse_sent += word[-1::-1] + letter
         word=''
   
   return reverse_sent

# Main function
try: 
   sentence = input("Enter Sentence to reverse words: ")

except Exception as msg:
   print("Error: {msg}")

else:
   reverse_sent = reverseWordsOfStr(sentence)

   print(f"\nGiven Sentence: {sentence}")
   print(f"Reversed Words Sentence: {reverse_sent}")
