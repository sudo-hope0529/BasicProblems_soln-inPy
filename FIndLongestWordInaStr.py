# Finding longest word in a sentence or string...
def longest_word(str):

   letters = []
   longestWordIndex = 0
   current_word = ""

   for letter in str:
      if letter.isalpha():
         current_word += letter
      else:
         if current_word:
            letters.append(current_word)
            current_word = ""
   if current_word:
      letters.append(current_word)

   longestLength = len(letters[0])

   for i in range(len(letters)):
      lett_len = len(letters[i])

      if ( lett_len > longestLength ): 
         longestLength = lett_len
         longestWordIndex = i

   return longestLength, letters[longestWordIndex]


# Main function
sentence = input( "Enter Sentence: ")

longestLen, long_word = longest_word(sentence)

print(f"The longest word in Given sentence is {long_word} with length {longestLen}")
