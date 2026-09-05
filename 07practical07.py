# Array Searching in Python

# Create an array
arr = [10, 20, 30, 40, 50, 60, 70]

print("Array:", arr)

# -------- Linear Search --------
key = int(input("\nEnter element to search using Linear Search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")


# -------- Binary Search --------
key = int(input("\nEnter element to search using Binary Search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index:", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")