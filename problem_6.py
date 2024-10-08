####################################################################
## Author: Michael Nickins                                        ##
## Last Edited: 08OCT2024                                         ##
## The program concerts the provided temperature from farenheight ##
## into celsius.                                                  ##
####################################################################



## Adds math-related functionality. ##
import math

## Asks the user for input. ##
farenheight = int(input("Give me a temperature in farenheight and I will turn it into celsius: "))

## Calculates celsius with the provided farenheight. ##
celsius = (farenheight-32) * 5 / 9

print(f"Here is your provided temerature of {farenheight} converted into celsius: {round(celsius)}.")