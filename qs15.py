# 15) Write a Python program to check if a string is an anagram of another string.("listen", "silent") 
def anagram_check(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    
    if len(str1) != len(str2):
        return False
    count_str1 = {}
    count_str2 = {}
    for char in str1:
        count_str1[char] = count_str1.get(char, 0) + 1
    for char in str2:
        count_str2[char] = count_str2.get(char, 0) + 1
    return count_str1 == count_str2

str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")
if anagram_check(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
