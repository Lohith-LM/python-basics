import numpy as np

# Create a 2D array
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

print("Full Data:")
print(data)

# Select first two rows
print("\nFirst two rows:")
print(data[0:2])

# Select last column
print("\nLast column:")
print(data[:, 2])

# Select a sub-matrix (rows 1 to 2, columns 0 to 1)
print("\nSub-matrix:")
print(data[1:3, 0:2])
