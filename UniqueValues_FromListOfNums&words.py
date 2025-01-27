# Printing Unique Values
def PrintUniqueValues(unique_values):
   if unique_values:
      print("\nUnique Values are: \n")
      for i in range( len(unique_values) ):
         print(unique_values[i])

   else:
      print("\nNo unique Values found...")

# find Unique Values for both numbers and words
# Remember This code is case-sensitive ( e.g. H & h are different)
def UniqueValues(value):

   if len(value) < 1:   # If length is less that 1 then return that no unique Values
      return None
   
   elif len(value) == 1:  # if length is 1 then return that value as Unique
      return value

   elif len(value) == 2:  # For length of 2 if 2 Values are diff then return both as Unique values
      if value[0] != value[1]:
         return value
      return None
   
   else:                 # For length greater than 2 
      unique_values = []  # list for unique values
      for i in range(len(value)):

         popped = False
         unique_values.append(value[i])

         for j in range(len(value)):
            if j != i:
               if value[i] == value[j]:
                  if popped != True:
                     popped = True
                     unique_values.pop(-1)
         
      return unique_values


# Main Function
print("\nNote - This solution is Case-sensitive (e.g. R & r are different)...")
value_list = list(input("Enter values to find Unique values among them: ").split() )
unique_values = UniqueValues(value_list)
PrintUniqueValues(unique_values)
