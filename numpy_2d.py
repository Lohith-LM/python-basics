import numpy as np

# Create a 2D array (matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix:")
print(matrix)

# Accessing elements
print("Element at row 0, column 1:", matrix[0][1])

# Shape of matrix
print("Shape of matrix:", matrix.shape)

# Basic operations
print("Add 10 to each element:")
print(matrix + 10)
