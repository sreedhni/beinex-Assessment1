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

a = [[1, 2, 3], 
     [4, 5, 6],
    [7, 8, 9],
      [2, 7, 8]]
b = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

try:
    result = matrix_multiply(a, b)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
