# 25) Write a Python program to count the number of occurrences of each element in a tuple.
while True:
    try:
        elements= input("Enter elements separated by spaces: ")
        tp = tuple(elements.split())
        
        break  
    except ValueError:
        print("Invalid input format. Please separate elements with spaces.")
element_occurance={}
for el in tp:
    if el in element_occurance:
        element_occurance[el]+=1

    else:
        element_occurance[el]=1

for key, value in element_occurance.items():
    print(f"occurance of {key}={value}")