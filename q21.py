# 21) Write a Python program to remove all whitespace characters from a string. 
def remove_space(string):
    white_space_removed_charactor=""
    for i in string:
        if(not i.isspace()):
            white_space_removed_charactor+=i
    return white_space_removed_charactor   
str1 = input("enter the string :")
print("whitespace removed charactors=",remove_space(str1))
