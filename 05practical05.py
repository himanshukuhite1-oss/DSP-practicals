# Import user-defined module
import mymodule

# Import built-in modules
import math
import random

print("===== USER-DEFINED MODULE =====")

print("Addition:", mymodule.add(10, 5))
print("Multiplication:", mymodule.multiply(10, 5))
print("Square:", mymodule.square(5))


print("\n===== MATH MODULE =====")

number = 25

print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.6))
print("Floor:", math.floor(4.6))


print("\n===== RANDOM MODULE =====")

print("Random number:", random.randint(1, 100))