from math import ceil, sqrt

# function to check if nummber is a Prime 
def isPrime(num):
   
   for i in range( ceil(sqrt(num)), 1, -1 ):
      if num % i == 0:
         return False

   return  True
 
# Main function
while True:
   try:
      number = int( input ("Enter Number to Check Prime: ") )

      if number <= 1:
         raise ValueError

   except ValueError:
      print("Enter a valid positive-Integer Number...!")

   else:
      if isPrime(number):
         print(number, "is a Prime Number." )
      else:
         print(number, "is Not a Prime Number." )

      try:   
         choice = int( input( "\n Wanna Check for Another Number[Enter 1] or Exit[Enter any Number except 1]: " ) )

         if choice != 1:
            break
         
      except ValueError:
         print( "\n Enter Valid Choice to perform oprr.." )
