# 4) Write a Python program to perform matrix multiplication using lists of lists. 

def matrix_multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Matrices are not compatible for multiplication.")

    res = [[0 for i in range(len(b[0]))] for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]

    return res

def input_matrix(prompt):
    matrix = []
    print(prompt)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(value)
        matrix.append(row)

    return matrix

try:
    print("Enter matrix A:")
    a = input_matrix("Matrix A:")
    print("\nEnter matrix B:")
    b = input_matrix("Matrix B:")

    result = matrix_multiply(a, b)
    print("\nResultant Matrix:")
    print(result)
except ValueError as e:
    print(f"Error: {e}")
