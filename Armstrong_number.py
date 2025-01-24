# For finding Armstrong Numbers in a given range of numbers 
def Print_Armstrong_nums( num_range ):

   for num in range(1, num_range):

      num_len = len(str(num))
      sum_of_digits = 0

      for dig in str(num):
         sum_of_digits += ( int(dig) ** num_len )
      
      if sum_of_digits == num:
         print(num)

# For Checking if a num is an Armstrong
def Check_4_Armstrong( number ):

   num_digits = len(str(number))
   # digits = [int(dig) for dig in str(number)]  adding all digits of number to list 'digits' by converting number into string 
   sum_of_digits = 0

   for dig in str(number):
      sum_of_digits += ( int(dig) ** num_digits )

   if sum_of_digits == number:
      return True
   return False


# Main function
print("""\n
Armstrong Program:
1. Choose to Check Any Number for Armstrong
2. Choose to Find Armstrong Numbers in a range of numbers
""")

choice = int( input("\nEnter Ur Choice: "))
if choice == 1:
   number = int(input("\nEnter Number to Check Armstrong: "))

   Armstrong = Check_4_Armstrong(number)

   if Armstrong == True:
      print(f"Number {number} is an Armstrong\n")
   else:
      print(f"Number {number} is not an Armstrong\n")

elif choice == 2:
   num_range = int(input("\nEnter range from 0 to _ to check for Armstrong Numbers: "))
   print(f"Armstrong numbers Between 1 & {num_range}:")
   Print_Armstrong_nums(num_range)
   
else:
   print("Error.. Choose Appropriate option...!")
