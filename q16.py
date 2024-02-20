# 16) Write a Python program to merge two sorted lists into a single sorted list. 
elements1 = input("Enter elements of the first list separated by spaces: ")
list1 = sorted([float(x) for x in elements1.split() if x.replace('.', '', 1).isdigit()])

elements2 = input("Enter elements of the second list separated by spaces: ")
list2 = sorted([float(x) for x in elements2.split() if x.replace('.', '', 1).isdigit()])

print("First list:", list1)
print("Second list:", list2)

res = sorted(list1 + list2)
print("The combined sorted list is:", res)

