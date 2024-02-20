# 3) print the following patterns: 
# a) 
# 0 
# 0 0 
# 0 0 0 
# 0 0 0 0 
while True:
    try:
        row = int(input("Enter the number of rows: "))
        break  
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(1, row + 1):
    print(i * " 0")

print( )
# b) 
#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
    
while True:
    try:
        row = int(input("Enter the number of rows: "))
        break  
    except ValueError:
        print("Invalid input. Please enter an integer value.")
for i in range(1, row + 1):
    print(" " * (2 * (row - i)) + "* " * (2 * i - 1))

print( )

# c) 
# 0 
# 1 1 
# 2 2 2 
# 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 5 
while True:
    try:
        row = int(input("Enter the number of rows: "))
        break  
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(0,row):
    for j in range(i+1):
        print(i,end=" ")
    print()


print( )

# d) 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
while True:
    try:
        row = int(input("Enter the number of rows: "))
        break  
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print( )

# e) 
# * * * * * * 
# * * * * * 
# * * * * 
# * * *  
# * * 
# *

while True:
    try:
        row = int(input("Enter the number of rows: "))
        break  
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(row, 0, -1):
    print("* " * i)
print( )

# f) 
# @ @ @ @ @ @ @ 
# @ @ @ @ @ @ @ 
# @ @ @ @ @ @ @ 
# @ @ @ @ @ @ @

while True:
    try:
        row = int(input("Enter the number of rows: "))
        column=int(input("Enter the number of coloumns: "))
        break  
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(row):
    for j in range(column):
        print("@", end=" ")
    print()
print( )
