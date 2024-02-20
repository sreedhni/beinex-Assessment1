# 24) Write a Python program to calculate the sum of all elements in a list recursively. 

def sum_of_all_elements(lst):
    if not lst:
        return 0
    return lst[0] + sum_of_all_elements(lst[1:])

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

result = sum_of_all_elements(lst)
print("Sum of all elements in the list:", result)





 

