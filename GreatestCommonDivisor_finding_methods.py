from math import gcd

# Function to find GCD of two numbers using the Euclidean algorithm
def gcdByEuclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find GCD using normal method
def Finding_common_gcd(num1, num2):
   GCD_num = 1
   if num1 < num2:
      for div in range(1, ( num1 // 2 ), 1):
         if (( num1 % div == 0 ) and ( num2 % div == 0)):
            GCD_num = div
   else:
      for div in range(1, ( num2 // 2), 1):
         if (( num1 % div == 0 ) and ( num2 % div == 0)):
            GCD_num = div

   return GCD_num

# Main Function...
try:
   num1 = int( input( "Enter Number 1: "))
   num2 = int( input( "Enter Number 2: "))

   if num1 <= 0 or num2 <= 0:
      raise ValueError
   
except:
   print("Error, Enter a positive Integer Number...!")

else:
   print(f"Common GCD of {num1} and {num2} By Python Math function : ", gcd(num1, num2))
   print(f"Common GCD of {num1} and {num2} By Euclidean Algorithm : ", gcdByEuclidean(num1, num2))
   print(f"Common GCD of {num1} and {num2} By User Defined function : ", Finding_common_gcd(num1, num2))
