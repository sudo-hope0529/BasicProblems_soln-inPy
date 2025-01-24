# Calculating factorial using Iteration & Rucursion based on User input

# Self Defined choice error
class ChoiceError( Exception ):
    def __init__(self):
        print( "Enter a valid choice for performing Factorial...!" )
    pass

# Factorial using tail recursion
def FactByTailRecursion(num, accumulator):
   if num == 1:
      return accumulator
   
   return FactByTailRecursion(num - 1,  num * accumulator)

# Factorial using Iterating( i.e. loop )
def FactByIteration(num):
   fact = 1

   while num >= 1:
      fact = fact * num
      num -= 1
   
   return fact


try:
   number = int( input( "Enter the Number: " ) )
   choice = int( input( "Enter Choice[ '1' for Rucursive method | '2' for Iterative method]: ") )

   if choice != 1 and choice != 2:
       raise ChoiceError
   
   if number <1:
       raise ValueError

except ValueError:
    print("Error... Enter a positive Integer number to perform Factorial....!")

except ChoiceError as msg:
    print( msg, end='')

else:
   if choice == 1:
         fact = FactByTailRecursion(number, 1)
         print(f"Factorial of '{number}' using Recursion : {fact}")

   else:
         fact = FactByIteration(number)
         print(f"Factorial of '{number}' using Iteration : {fact}")
