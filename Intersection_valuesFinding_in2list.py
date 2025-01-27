""" Function to find intersecting & Non-Intersecting values in 2 list
    containing either integers or words or both """

def Intersection(list1, list2):

   intersectionValues, NonIntersectingValuesOfList1, NonIntersectingValuesOfList2 = [], [], []

   for i in list1:                       # For finding Intersecting & non-intersecting values
      if i in list2:
         if i not in intersectionValues:
            intersectionValues.append(i) # store intersecting values in list1 and list2
      else:
         NonIntersectingValuesOfList1.append(i) # store non-intersecting values of list1

   for j in list2:                        # For finding Non-intersecting values of list 2
      if j not in list1:
         if j not in NonIntersectingValuesOfList2:
            NonIntersectingValuesOfList2.append(j)  # store non-intersecting values of list1

   return intersectionValues, NonIntersectingValuesOfList1, NonIntersectingValuesOfList2


#Main Function of Program
list1 = list(input("\nEnter Element of list or set 1: ").split() )
list2 = list(input("Enter Element of list or set 2: ").split() )

if list1 and list2:
   result = Intersection(list1, list2)

   if result:
      print("\nThe Intersecting Values are: ")
      print(result[0], "\n")

      print("\n Non-Intersecting Values of List 1: ")
      print(result[1], "\n")

      print("\n Non-Intersecting Values of List 2: ")
      print(result[2], "\n")
