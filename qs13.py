# 13) Write a Python program to check if a string contains only digits.("12345" -->True) 
str = input("Enter the string: ")


if str.isdigit():
    print(f"{str} --> True (it contains only digits)")
else:
    print(f"{str} --> False (not all elements are digits it contain space or alphabets)")

