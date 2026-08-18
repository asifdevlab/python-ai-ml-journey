# Question 3:
# Input two lists of integers from the user.
# Merge them into one list and sort the result.
# Example: list1 = [1, 2, 7], list2 = [2, 4, 5]
# Result = [1, 2, 2, 4, 5, 7]

# Step 1: Take input for two lists
list1 = list(map(int, input("Enter numbers for list1 separated by spaces: ").split()))
list2 = list(map(int, input("Enter numbers for list2 separated by spaces: ").split()))

# Step 2: Merge the two lists
merged_list = list1 + list2

# Step 3: Sort the merged list
merged_list.sort()

# Step 4: Print the result
print("Merged and sorted list:", merged_list)
