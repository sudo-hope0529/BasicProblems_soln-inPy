# Program to check if a sentece is a pangram...
def Check_Panidrome(sentence, absent_letter='', present_letter=''):
   alpha ='abcdefghijklmnopqrstuvwxyz'
   pangram = True
   for letter in alpha:
      if letter in sentence.lower():
            present_letter += ' ' + letter
      else:
            absent_letter += ' ' + letter
            pangram = False

   return pangram, present_letter, absent_letter

# main Function for Pangram Checking
string = input("\nEnter sentence to Check Pangram: ")
result, present_letters, absent_letters = Check_Panidrome(string)

if result == True:
    print(f"\n'{string}' is a Pangram...")

else:
    print(f"\n'{string}' is not a Pangram...")
    print(f"Present Letters: '{present_letters}'")
    print(f"Absent Letters: '{absent_letters}'\n")
