# Function to check if strSub is a substring of strMain and return starting Index (position) of Substring in strMain

def Substring_check(strMain, strSub):
   position = strMain.find(strSub)
   if position != -1:
      return True, position
   return False, -1


# Main Function
strMain = input('\nEnter the main String: ')
strSub = input('Enter the Sub-String to check: ')

string_substring, strStIndex = Substring_check(strMain.lower(), strSub.lower())

# If strSub is a substring of StrMain then show with Starting-Index
if string_substring is True: 
   print(f''''{strSub}' is a Sub-String of String:'{strMain}'
   Starting Index of Sub-String: {strStIndex+1}\n''')

else:
   print(f"'{strSub}' is not a Sub-String of '{strMain}'\n")