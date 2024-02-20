# 2)Write a program to check the validity of a password. Primary conditions for password validation: 
# - minimum 8 charecters 
# - The alphabet must be between [a-z] 
# - At least one alphabet should be of Upper Case [A-Z]
#  - At least 1 number or digit between [0-9].
# - At least 1 character from [ _ or @ or $ ]. 

from re import search

password = input("Enter the password: ")

if len(password) < 8:
    print("Invalid password")
    print("Explanation: Minimum length of the password is 8")
elif not search("[a-z]", password):
    print("Invalid password")
    print("Explanation: The alphabet must be between [a-z] ")
elif not search("[A-Z]", password):
    print("Invalid password")
    print("Explanation: Must contain at least one uppercase letter")
elif not search("[0-9]", password):
    print("Invalid password")
    print("Explanation: Must contain at least one digit")
elif not search("[_@$]", password):
    print("Invalid password")
    print("Explanation: Must contain at least one special character (_ or @ or $)")
else:
    print("Valid password")




#     FUNCTION BASED                OR           


# from re import search

# def valid_password(password):
#     if len(password) < 8:
#         return False, "Minimum length of the password is 8"
#     elif not search("[a-z]", password):
#         return False, "The alphabet must be between [a-z]"
#     elif not search("[A-Z]", password):
#         return False, "Must contain at least one uppercase letter"
#     elif not search("[0-9]", password):
#         return False, "Must contain at least one digit"
#     elif not search("[_@$]", password):
#         return False, "Must contain at least one special character (_ or @ or $)"
#     else:
#         return True, "Valid password"

# password = input("Enter the password: ")
# validity, message = valid_password(password)

# if validity:
#     print(message)
# else:
#     print("Invalid password")
#     print("Explanation:", message)

