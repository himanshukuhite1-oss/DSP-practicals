# Python Operators Demonstration

a = 10
b = 3

print("===== ARITHMETIC OPERATORS =====")
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponent       :", a ** b)

print("\n===== RELATIONAL OPERATORS =====")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\n===== LOGICAL OPERATORS =====")
x = True
y = False

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

print("\n===== BITWISE OPERATORS =====")
print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a    :", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

print("\n===== ASSIGNMENT OPERATORS =====")
c = 10
print("Initial c :", c)

c += 5
print("c += 5    :", c)

c -= 3
print("c -= 3    :", c)

c *= 2
print("c *= 2    :", c)

c /= 4
print("c /= 4    :", c)