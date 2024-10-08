################################################
## Author: Michael Nickins                    ##
## Last Edited: 08OCT2024                     ##
## Will calculate the area of a circle with a ##
## user-proved value.                         ##
################################################



## Imports math-related functionality. ##
import math

## Asks the user for a value. Can be a decimal. ##
radius = float(input("Give me a value: "))

## Conditional if-else function to check if the given value is greater than 0. ##
## Rejects values is they are less or equal to 0.                              ##
## Calculates accepted values and prints the result.                           ##
if radius <= 0:
    print("Please provide a value greater than zero.")
else:
    area = math.pi * radius ** 2
    print(f"Here is the area of a circle with the provided radius {radius}: {area:.4f}")