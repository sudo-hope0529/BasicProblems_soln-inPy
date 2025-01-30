# Function for finding Number pairs of given target sum from given number list using Nested Loop
def finding_num_pairs_of_given_sum_by_nested_loop(num_list, target_sum, len_list):
   pair_list = []

   for i in range(len_list):
      for j in range(i+1, len_list):
         if num_list[i] + num_list[j] == target_sum:
            if [j, i] not in pair_list:
               pair_list.append([num_list[i], num_list[j]])

   return pair_list

# Function for finding Number pairs of given target sum from given number list without using Nested Loop
def finding_num_pairs_of_given_sum_without_nested_loop(num_list, target_sum):
   pair_list = []
   seen = set()  # Initialize a set to keep track of numbers we have seen

   for num in num_list:
      complement = target_sum - num
      
      if complement in seen:
         pair_list.append((complement, num))
      seen.add(num)

   return pair_list

# Function for finding number triplets of given target sum from given Number using 3 Loop
def finding_triplets_of_given_sum1(num_list, target_sum, len_list):  # less efficient method
   triplets_list = []

   for i in range(len_list):
      for j in range(i+1, len_list):
         for k in range(j+1, len_list):

            if num_list[i] + num_list[j] + num_list[k] == target_sum:
               if [k, j, i] and [j, k, i] and [i, j, k] in triplets_list:
                  triplets_list.append([num_list[i], num_list[j], num_list[k]])

   return triplets_list

# Function for finding number triplets of given target sum from given Number using 2 loops
def finding_triplets_of_given_sum2(num_list, target_sum, len_list):
      triplets_list = []
      num_list.sort()

      for i in range(len_list - 2):
         left = i + 1
         right = len_list - 1

         while left < right:
            current_sum = num_list[i] + num_list[left] + num_list[right]

            if current_sum == target_sum:
               triplets_list.append((num_list[i], num_list[left], num_list[right]))
               left += 1
               right -= 1
            elif current_sum < target_sum:
               left += 1
            else:
               right -= 1
               
      return triplets_list

def print_pair_list(pair_list):
   if pair_list:
      print(f"\nThe Pairs of Target Sum {target_sum}: {pair_list}")
   else:
      print(f"\nThere are no Pairs of Target Sum {target_sum} \n")

# Main Function or Example Usage
num_list = list( map(int, input("\nEnter the Numbers: ").split() ))
target_sum = int(input("Enter the target Sum: "))
choice = input("Wanna Use Nested Loop Method[A] or Not[b] for pair: ")
len_list = len(num_list)

if len_list >= 2 and target_sum:
   # Finding Pairs
   if choice.lower() == 'a':
      pair_list = finding_num_pairs_of_given_sum_by_nested_loop(num_list, target_sum, len_list)
      print("Method: Nested Loop")
      print_pair_list(pair_list)

   else:
      pair_list = finding_num_pairs_of_given_sum_without_nested_loop(num_list, target_sum)
      print("Method: Single Loop")
      print_pair_list(pair_list)

   # Finding triplets
   triplets_list = finding_triplets_of_given_sum2(num_list, target_sum, len_list)

   if triplets_list :
      print(f"\nThe Triplets of Target Sum {target_sum}: {triplets_list}")
   else:
      print(f"\nThere are no Triplets of Target Sum {target_sum} \n")

else:
   print("Error... Enter a Valid Length Number List (i.e. > 2 nnumbers) ")
