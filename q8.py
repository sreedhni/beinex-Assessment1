# 8) Write a Python program to reverse a list.
elements = input("Enter elements of the list separated by spaces: ")
lst = elements.split()
lst.reverse()
print("Reversed list is ",lst)

#   OR

elements = input("Enter elements of the list separated by spaces: ")
lst = elements.split()
reversed_lst = lst[::-1]  
print("Reversed list is:", reversed_lst)
