
# Palindrome Check for both Numbers and Word
print('''
      Check Palindrome for:
         1. For Number
         2. For Word
         3. Exit 
      ''')


def PrintPalindrome0not( result, num0word ):

   if result == 1:
      print(f" {num0word} is a Palindrome..!")
   else:
      print(f" {num0word} is not a Palindrome..!")


def isNumPalindrome( num ):

   temp = num
   reverse_num = 0

   while temp >= 1 :
      reverse_num = reverse_num * 10 + temp % 10
      temp = temp // 10

   if num == reverse_num:
      PrintPalindrome0not( 1, num )
   else:
      PrintPalindrome0not( 0, num )


def isWordPalindrome( word ):
      reverse_word = word[-1::-1]

      if ( word.lower() == reverse_word.lower() ):
         PrintPalindrome0not( 1, word )
      else:
         PrintPalindrome0not( 0, word )


# Main logic of program
while True:
   try:
      choice = int( input("\n Enter your Choice [1/2/3] : ") )

   except ValueError:
      print(" Error... Enter a valid integer Choice..!")

   else:
      # Checking Number for Palindrome
      if choice == 1:

         while True:
            try:
               num = int( input("\n Enter the Number : ") )

               if num <= 0:
                  raise ValueError
               
            except:
               print('''
                     Error... Negative numbers can't be a plaindrome..!
                     Enter a Non-negative integer number..! 
                     ''')

            else:
               isNumPalindrome( num )
               break

      # Checking word for Palindrome
      elif choice == 2:
         word = input("\n Enter the Word : ")
         isWordPalindrome( word )

      elif choice == 3:
         print(' Exiting Program...!')
         break

      else:
         print(' Error.. Enter a valid choice..!')
