######################################################################
## Author: Michael Nickins                                          ##
## Last Edited: 08OCT2024                                           ##
## Program asks the user for input and caculates the returning day. ##
######################################################################



## Prompts the user for input. ##
start_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))
length_of_stay = int(input("Enter the length of your stay in nights: "))

## Calculates the return day. ##
return_day = (start_day + length_of_stay) % 7

## Prints the result. ##
print(f"You will return on day number: {return_day}")
