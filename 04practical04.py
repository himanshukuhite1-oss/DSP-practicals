# Tuple, Set and Dictionary Operations in Python

# ================= TUPLE =================
print("===== TUPLE OPERATIONS =====")

t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)
print("First Element:", t[0])
print("Last Element:", t[-1])
print("Length:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Tuple Slicing:", t[1:4])


# ================= SET =================
print("\n===== SET OPERATIONS =====")

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print("Set 1:", s1)
print("Set 2:", s2)

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))

s1.add(50)
print("After add():", s1)

s1.remove(10)
print("After remove():", s1)


# ================= DICTIONARY =================
print("\n===== DICTIONARY OPERATIONS =====")

student = {
    "name": "Rahul",
    "age": 18,
    "branch": "CSE",
    "marks": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Student Name:", student["name"])
print("Student Marks:", student["marks"])

# Adding a new key-value pair
student["city"] = "Nagpur"
print("After adding city:", student)

# Updating a value
student["marks"] = 90
print("After updating marks:", student)

# Removing a key-value pair
student.pop("age")
print("After removing age:", student)

# Dictionary functions
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Number of items:", len(student))