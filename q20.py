# 20) Write a Python program to remove all occurrences of a given element from a list. 
lst = []

while True:
    try:
        length = int(input("Enter the length of the list: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value for the length.")

for i in range(length):
    while True:
        try:
            element = int(input(f"Enter the {i+1}th element: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value for the element.")
    lst.append(element)

while True:
    try:
        removing_element = int(input("Enter the element to remove: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value for the element.")
lst = [x for x in lst if x != removing_element]

print("List after removing all occurrences of the element:", lst)
