#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
    last_digit = -(number % 10)
    number = -number
else:
    last_digit = number % 10
buffer = f"Last digit of {number} is {last_digit}"
if last_digit > 5:
    print(f"{buffer} and is greater than 5")
elif last_digit == 0:
    print(f"{buffer} and is 0")
elif last_digit < 6 and not 0:
    print(f"{buffer} and is less than 6 and not 0")
