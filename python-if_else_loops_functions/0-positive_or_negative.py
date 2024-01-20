# This script determines if a number is positive, negative, or zero
import random
num = random.randint(-10, 10)
if num > 0:
    print(f"{num} is positive")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is negative")