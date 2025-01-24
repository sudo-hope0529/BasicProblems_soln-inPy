# function to check if number id divisible by 3
def isDivisibleBy3(number):
   if number % 3 == 0:
      return True
   else:
      return False

# function to check if number id divisible by 5
def isDivisibleBy5(number):
   if number % 5 == 0:
      return True
   else:
      return False

# Main Function for FIZZ & Buzz Problem
while True:

   try:
      number = int( input("\nEnter the Number [0. to Exit]: ") )
      if number < 0:
         raise ValueError
      if number == 0:
         break
      
   except:
      print("Error.. Enter Valid Input...!")

   else:
      if isDivisibleBy3(number) and isDivisibleBy5(number) :
         print("Fizz-Buzz")
      elif isDivisibleBy3(number):
         print("Fizz")
      elif isDivisibleBy5(number):
         print("Buzz")
      else:
         print(number)
