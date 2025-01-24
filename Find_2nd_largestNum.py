from math import inf

def Check_Uniqueness(list):
   num = list[0]
   for n in list:
      if (num != n): return True
   return False

def Second_largest(list, large = -inf, second_large = -inf):
   for num in list:
      if num > large: second_large, large = large, num
      elif num > second_large: second_large = num
   return large, second_large 

# Main Function for Finding 2nd Largest Number
try:
   num_list = list( map( int, input("Enter the List of Numbers to Find 2nd largest Num: ").split() ) )

   if len(num_list) < 2:
      raise ValueError('Atleast 2 values needs to be present')
   
   if not Check_Uniqueness(num_list):
      raise ValueError('Atleast 2 Unique values needs to be present...!')

except Exception as msg:
   print(f"Err0r: {msg}")

else: 
   result = Second_largest(num_list) # Pass large & then 2nd Large if have reference e.g.

   if result == (-inf):
      print("No Second Largest Number in Given List...!")
   elif result:
      print(f"Largest Number: {result[0]}")
      print(f"Second Largest Number: {result[1]}")
