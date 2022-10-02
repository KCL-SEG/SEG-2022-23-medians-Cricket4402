"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
from platform import java_ver
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        str = input().replace(" ", "")
        numbers = [float(value) for value in str.split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
    
# Actual functionality
numbers.sort()
x = math.floor(len(numbers)/2)

print(x)
if(len(numbers) % 2 == 0):
    print((numbers[x-1] + numbers[x])/2)
else:
    print(numbers[x])