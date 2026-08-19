# Question 8:
# Write a program to check whether two lists share no common elements.
# Example:
#   list1 = [1, 2, 3, 4], list2 = [5, 6, 7, 8] → No common elements
#   list1 = [1, 2, 3], list2 = [3, 4] → Share common elements

list1 = list(map(int,input("Enter the integer elements of list-1: ").split()))

list2 = list(map(int,input("Enter the integer elements of list-2:").split()))

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)
if common :
    print(f"Yes there is common element in both the list:{common}")
else:
    print("No common element exist between two list.")

