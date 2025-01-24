# Lagest num among 3 Numers
print('''
      Note: 
       Enter Numbers to find largest among them
       Enter 0 or -ve Number to end the program
      ''')

largest_num = 0
i = 1
while True:
   try:
      num = int(input(f"Enter Number {i} : "))

      if i == 1 and num <= 0:
         raise ValueError
      
      if num > largest_num:
         largest_num = num
      elif num <= 0:
         break

      i += 1
      
   except:
      largest_num = None
      print("Error.. 1st Value cannot be Zero..!")
      break


if largest_num is not None:
   print(f"Largest Number Among {i} Numbers is {largest_num}")
