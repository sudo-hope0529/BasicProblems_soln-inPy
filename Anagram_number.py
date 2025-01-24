def Check_Anagram(str1, str2):
   str1 = str1.lower()
   str2 = str2.lower()
   Anagram = True
   
   if len(str1) != len(str2):
       return False
   
   for letter1 in str1:
         for letter2 in str2:
            if letter1 not in str2 or letter2 not in str1:
               Anagram = False
 
         return Anagram

#main function for checking anagrams
string1 = input("Enter String 1: ")
string2 = input("Enter String 2: ")

result = Check_Anagram(string1, string2)
if result == True:
   print(f"'{string1}' & '{string2}' are Anagrams..!")
else:
   print(f"'{string1}' & '{string2}' are not Anagrams..!")
