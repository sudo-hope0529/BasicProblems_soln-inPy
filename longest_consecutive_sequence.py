# solution for finding longest consecutive sequence using 2 loops from mine
def longest_consecutive_sequence_in_unsorted_list(num_list):
   if len(num_list) <= 2:
      return None
   
   num_set = set(num_list)

   # separating consecutive numbers in separate sub-lists
   consecutive_seq_list, index = [], 0
   for num in range(min(num_set), max(num_set)+1):
      if num in num_set:
         if index >= len(consecutive_seq_list):
            consecutive_seq_list.append([num])
         else:
            consecutive_seq_list[index].append(num)
   
      else:
         index += 1
   
   # Finding max consecutive sequence length and sub-list
   max_consecutive_seq_len = len(consecutive_seq_list[0])
   max_consecutive_seq_index = 0

   for i in range(1, len(consecutive_seq_list)):
      current_consecutive_seq_len = len(consecutive_seq_list[i])
      
      if current_consecutive_seq_len > max_consecutive_seq_len:
         max_consecutive_seq_len = current_consecutive_seq_len
         max_consecutive_seq_index = i
   
   return max_consecutive_seq_len, consecutive_seq_list[max_consecutive_seq_index]

# more efficient solution learned from chatgpt
def longest_consecutive_sequence(num_list):
    if not num_list:
        return None
   
    num_set = set(num_list)
    longest_length = 0
    best_sequence = []

    for num in num_set:
        if num - 1 not in num_set:  # Start a sequence only if it's the first number in a consecutive sequence
            current_num = num
            current_sequence = []

            while current_num in num_set:
                current_sequence.append(current_num)
                current_num += 1

            # Update longest sequence if found
            current_sequence_len = len(current_sequence)
            if current_sequence_len > longest_length:
                longest_length = current_sequence_len
                best_sequence = current_sequence

    return longest_length, best_sequence


# Example usages
num_list = list( map(int, input("Enter the Numbers: ").split() ))
# result = longest_consecutive_sequence_in_unsorted_list(num_list)
result = longest_consecutive_sequence(num_list)

if result:
   print(f"Longest Consecuteive Length: {result[0]}")
   print(f"Max consecutive Sequence: {result[1]}")

else:
   print("No Consecutive Sequence found on given list...")