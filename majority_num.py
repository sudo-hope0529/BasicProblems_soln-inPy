from typing import Counter

# function to find majority numbers in a list using dict for n // 3 instead of n // 2
def find_majority_nums(num_list):
   majority_list = []
   num_dict = dict(Counter(num_list))

   for num in num_dict:
      if num_dict[num] > len(num_list) // 3:
         majority_list.append([num, num_dict[num]])

   return majority_list

# Booyer Moore Voting Algorithms for finding majority number in a list [ for n // 3 ]
def boyer_moore_voting_algorithm(num_list):
   if not num_list:
      return []
   
   candidate1, candidate2, count1, count2 = None, None, 0, 0

   # Pass 1: Finding the potential candidates( Numbers )
   for num in num_list:
      if candidate1 == num:
         count1 += 1
      elif candidate2 == num:
         count2 +=1
      elif count1 == 0:
         candidate1, count1 = num, 1
      elif count2 == 0:
         candidate2, count2 = num, 1
      else:
         count1 -= 1
         count2 -= 1

   # pass 2: verifying potential condidates(numbers)
   count1, count2 = 0, 0
   for num in num_list:
      if num == candidate1:
         count1 += 1
      elif num == candidate2:
         count2 += 1
   
   # Checking if potential candidates are majority numbers
   threshhold = len(num_list) // 3
   majority_list = []
   if count1 > threshhold:
      majority_list.append([candidate1, count1])
   if count2 > threshhold:
      majority_list.append([candidate2, count2])

   return majority_list


# main Function or Example Usages
num_list = list(map(int, input("\nEnter Numbers to find Majority Number: ").split() ))
majority_num = find_majority_nums(num_list)
majority_nums = boyer_moore_voting_algorithm(num_list)

if majority_num:
   for i in range(3):
      print(f"Majority Num: {majority_num[i][0]}, Frequency: {majority_num[i][1]} times\n")
else:
   print("There is no majority number on given list..\n")
if majority_nums:
      print(f"Majority Num: {majority_nums}\n")