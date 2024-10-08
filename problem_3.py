################################################################
## Author: Michael Nickins                                    ##
## Last Edited: 08OCT2024                                     ##
## Modifies the previous program to only accept certain names ##
################################################################



## The two accepted names. ##
user_1 = str("Austin")
user_2 = str("Linh")

## Asks the user to input their name under the 'name' variable. ##
name = input("What is your name? ")

if name == user_1 or name == user_2:
    print("Hello,", name,"!")
else:
    print("I don't know you.")