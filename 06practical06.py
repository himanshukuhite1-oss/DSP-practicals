import numpy as np

# 1. Array Creation
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(arr)

# 2. Indexing
print("\n===== INDEXING =====")
print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])

# 3. Slicing
print("\n===== SLICING =====")
print("First three elements:", arr[:3])
print("Elements from index 2 to 4:", arr[2:5])
print("Every second element:", arr[::2])

# 4. Reshaping
print("\n===== RESHAPING =====")
arr2 = np.array([1, 2, 3, 4, 5, 6])
matrix = arr2.reshape(2, 3)

print("Original Array:", arr2)
print("Reshaped Array:")
print(matrix)

# 5. Mathematical Operations
print("\n===== MATHEMATICAL OPERATIONS =====")

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Square of a:", a ** 2)
print("Square Root of a:", np.sqrt(a))
print("Sum of a:", np.sum(a))
print("Maximum of a:", np.max(a))
print("Minimum of a:", np.min(a))