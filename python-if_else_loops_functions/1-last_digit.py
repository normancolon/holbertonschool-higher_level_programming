# This script prints the last digit of a number and its characteristics
import random
num = random.randint(-10000, 10000)
last_digit = num % 10 if num >= 0 else (-num % 10) * -1
print(f"Last digit of {num} is {last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")