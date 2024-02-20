# 18) Write a Python program to find the second largest number in a list.

given_list = input("Enter a list of elements separated by commas: ")
elements = given_list.split(",")
integer_element_list = []
for element in elements:
    try:
        float_value = float(element.strip())
        integer_element_list.append(float_value)
    except ValueError:
        print("Skipping invalid element:", element)

if not integer_element_list:
    print("There are no numeric values in the given list. Cannot find the second largest number.")
else:
    unique_sorted_integer_element_list = sorted(set(integer_element_list), reverse=True)
    
    if len(unique_sorted_integer_element_list) >= 2:
        second_largest_element = unique_sorted_integer_element_list[1]
        print(f"The second largest number from the given input list [{given_list}] is:", second_largest_element)
    else:
        print("The given list has fewer than two distinct valid numbers. There is no second largest number.")
