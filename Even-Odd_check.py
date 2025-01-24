# Program to identify whether a given number is Even or Odd
def Even0Odd(number):
  if num % 2 == 0:
     return True
  return False

# Main Function
num = int(input("Enter Number:"))

if Even0Odd(num) == True:
   print(f"{num} is an Even Number...!\n")
else:
   print(f"{num} is an Odd Number...!\n")
