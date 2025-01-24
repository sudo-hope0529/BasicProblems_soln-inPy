from math import lcm

def Find_lcm(n1, n2):
   Lcm = 1
   if (n1 > n2): upto = n1
   else: upto = n2

   for i in range(2, upto+1):
      while True:
         if ((n1 % i == 0) and (n2 % i == 0)):
            n1, n2 = n1 / i, n2 / i
            Lcm *= i
         elif (n1 % i == 0):
            n1 /= i
            Lcm *= i
         elif (n2 % i == 0):
            n2 /= i
            Lcm *= i
         elif ((n1 % i != 0) and (n2 % i != 0)):
            break

   return Lcm


num1 = int( input("Enter Num 1: ") )
num2 = int( input("Enter Num 2: ") )
num3 = int( input( "Enter Num 3: "))

print(f"LCM of {num1} & {num2} & {num3} by Py Math.lcm Fn: ", lcm( lcm(num1, num2), num3) )
print(f"LCM of {num1} & {num2} & {num3} by User Def Fn: ", Find_lcm( Find_lcm(num1, num2), num3) )
