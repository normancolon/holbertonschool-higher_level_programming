#!/usr/bin/python3
import random
random_value = random.randint(-10000, 10000)
if random_val >= 0:
    final_digit = random_val % 10
elif random_value < 0:
    final_digit = ((random_val * -1) % 10) * -1
if final_digit > 5:
    result_message = 'Last digit of {0} is {1} and is greater than 5'
elif final_digit < 6 and final_digit != 0:
    result_message = 'Last digit of {0} is {1} and is less than 6 and not 0'
elif final_digit == 0:
    result_message = 'Last digit of {0} is {1} and is 0'
print(result_message.format(random_val, final_digit))
