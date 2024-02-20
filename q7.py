# 7) Write a Python program to implement a binary search on a sorted list.
lst = [2, 3, 4, 78, 90, 1, 100, 98]
lst = sorted(lst)

try:
    el = int(input("Enter a number: "))  

    is_present = False
    lower, upper = 0, len(lst) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid] == el:
            is_present = True
            break
        elif lst[mid] < el:
            lower = mid + 1
        else:
            upper = mid - 1

    if is_present:
        print(el, " is present")
    else:
        print(el, " is not present")
except ValueError:
    print("Please enter a valid integer number.")
       



