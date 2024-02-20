# 19) Write a Python program to count the number of vowels in a string. 
vowels = {"a", "e", "i", "o", "u"}
str1 = input("Enter the string: ")
vowel_count = 0

for vowel in str1:
    if vowel.lower() in vowels:
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)
