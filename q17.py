# 17) Write a Python program to find the sum of all even numbers in a list. 
while True:
    given_list = input("Enter a list of elements separated by commas: ")
    if ',' not in given_list:
        print("Invalid input format. Please enter a comma-separated list.")
        continue
    elements = given_list.split(",")
    integer_element_list = []
    for element in elements:
        try:
            float_value = float(element.strip())
            integer_element_list.append(float_value)
        except ValueError:
            print("Skipping invalid element:", element)
    if integer_element_list:
        even_sum = sum(element for element in integer_element_list if element % 2 == 0)
        print(f"Sum of all even numbers in the given list [{given_list}] is:", even_sum)
        break
    else:
        print("The input list does not contain any valid numbers. Please enter again.")
