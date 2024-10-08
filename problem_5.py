######################################################
## Author: Michael Nickins                          ##
## Last Edited: 08OCT2024                           ##
## The program asks the user for miles driven and   ##
## gallons used, calculates the MPH, and prints it. ##
######################################################



# Asks the user for input. ##
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))

# Calculates the miles per gallon. ##
mpg = miles_driven / gallons_used

## Prints the result. ##
print(f"The MPG for your car is: {mpg:.2f}")