# 10) Write a Python program to remove duplicates from a list. 
elements = input("Enter elements of the list separated by spaces: ")
lst= elements.split()
duplicates=set([i for i in lst if lst.count(i)>1])

if duplicates:
    for dupli in duplicates:
        lst.remove(dupli)
    print("duplicates removed list=,",lst)
else:
    print("no duplicates")

# OR

# elements = input("Enter elements of the list separated by spaces: ")
# lst = elements.split()
# unique_list = list(set(lst))

# print("List with duplicates removed:", unique_list)

