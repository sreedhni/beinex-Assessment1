# 9) Write a Python program to count the occurrences of an element in a list. 
elements = input("Enter elements of the list separated by spaces: ")
lst = elements.split()
element = input("Enter the element: ")
x = [i for i in lst if i == element] 
if x:
    print("The element", element, "occurs", len(x), "times")
else:
    print("The element", element, "is absent in the list")

# OR
    
# elements = input("Enter elements of the list separated by spaces: ")
# lst = elements.split()
# element = input("Enter the element: ")
# count = lst.count(element)
# print(f"The element {element} occurs {count} times in the list.")
