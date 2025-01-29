# Function to find Missing Numbers in an input list by simple method
def MissingNums_SimpleMethod(num_list, max_value = 0):

   if max_value == 0: max_value = max(num_list)  # if max is not specified by user then calculate it 
   missing_values = []

   for i in range(1, max_value):
      if i not in num_list:
         missing_values.append(i)
   
   return missing_values

# Function to find a Missing Number in an input list by sum method
def MissingNum_SumMethod(num_list):

   n = len(num_list) + 1      # N = No. of numbers in list
   total_sum = (n * (n + 1)) // 2
   actual_sum = sum(num_list)
   missing_value = total_sum - actual_sum
   return missing_value

# Function to find Missing Numbers in an input list by set method
def MissingNums_SetMethod(num_list):

   max_value = max(num_list)
   full_set = set(range(1, max_value + 1))   # ideal set upto max number
   missing_values = list(full_set - set(num_list)) # actual set from list 
   return missing_values

# Main Function or Example Usages
num_list = list( map( int, input("\nEnter the Numbers: ").split() ))
print("Choose: \nA. If 1 missing Value to find \nB. More that 1 missing value to find")
choice = input("Enter Your Choice [A | B]: ")

missingValues_BySimpleMethod = MissingNums_SimpleMethod(num_list)
missingValues_BySetMethod = MissingNums_SetMethod(num_list)

if choice.lower() == 'a':
   missingValues_BySumMethod = MissingNum_SumMethod(num_list)
   print(f"Missing Value by Sum method: {missingValues_BySumMethod}")

print(f"Missing Values by Simple method: {missingValues_BySimpleMethod}")
print(f"Missing Values by Set method: {missingValues_BySetMethod}\n")