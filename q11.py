# 11) Write a Python program to find the intersection of two lists.


lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
intersection_of_two_list = []
lst1, lst2 = sorted(set(lst1)), sorted(set(lst2))  
p1, p2 = 0, 0
while p1 < len(lst1) and p2 < len(lst2):
    if lst1[p1] == lst2[p2]:
        intersection_of_two_list.append(lst1[p1])
        p1 += 1
        p2 += 1
    elif lst1[p1] < lst2[p2]:
        p1 += 1
    else:
        p2 += 1

print("Intersection of the two given lists are:", intersection_of_two_list)

#   OR

def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3

lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69,"HU"]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26,"HU"]
print("Intersection of the list is",intersection(lst1, lst2))


