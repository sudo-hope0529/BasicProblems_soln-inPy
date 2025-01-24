#   Program to Count the number of vowels in a string

"""
# function to count vowels of string using basic method
def vowel_count(string):
   vowel_counts = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0,
                    'total_vowel' : 0, 'total_consonant': 0 }

   for letter in string.lower():
      if 'a' in letter:
         vowel_counts['total_vowel'] += 1
         vowel_counts['a'] += 1

      elif 'e' in letter:
         vowel_counts['total_vowel'] += 1
         vowel_counts['e'] += 1

      elif 'i' in letter:
         vowel_counts['total_vowel'] += 1
         vowel_counts['i'] += 1
         
      elif 'o' in letter:
         vowel_counts['total_vowel'] += 1
         vowel_counts['o'] += 1

      elif 'u' in letter:
         vowel_counts['total_vowel'] += 1
         vowel_counts['u'] += 1
      
      elif ' ' in letter:
         pass

      elif letter.isdigit():
         pass

      else:
         vowel_counts['total_consonant'] += 1

   return vowel_counts
"""

def vowels_count(string):
   vowels = 'aeiou'
   vowel_count = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'total_vowel' : 0}

   for letter in string.lower():
      for vowel in vowels:
         if vowel == letter:
            vowel_count[vowel] += 1

   for vowel in vowels:
      vowel_count['total_vowel'] += vowel_count[vowel]
   return vowel_count

while True:
   try:
      sentence = input("Enter Sentece to calculate No. of Vowels: ")
      if sentence.isdigit():
         raise ValueError
      
   except  ValueError as msg:
      print("sentece can't contain Numbers alone...!")

   except:
      print("Enter valid String...!")

   else:
      counts = vowels_count(sentence)

      print(f'''
      Total number of Vowels = {counts['total_vowel']}
      a = {counts['a']}
      e = {counts['e']}
      i = {counts['i']}
      o = {counts['o']}
      u = {counts['u']}
      ''')

      break
