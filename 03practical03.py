# Python List Operations

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Adding an element
numbers.append(60)
print("After append():", numbers)

# Inserting an element
numbers.insert(2, 25)
print("After insert():", numbers)

# Removing an element
numbers.remove(25)
print("After remove():", numbers)

# Removing the last element
numbers.pop()
print("After pop():", numbers)

# Sorting the list
numbers.sort()
print("After sort():", numbers)

# Reversing the list
numbers.reverse()
print("After reverse():", numbers)

# Finding length
print("Length of list:", len(numbers))

# Finding maximum and minimum
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# Finding sum
print("Sum of elements:", sum(numbers))

# Counting an element
print("Count of 30:", numbers.count(30))

# Finding index
print("Index of 30:", numbers.index(30))