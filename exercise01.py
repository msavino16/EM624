# Author:  Michael Savino

# Exercise 01
# Sample program

# This program will convert a temperature in Fahrenheit
# into a temperature in Celsius

# The program is written as a loop (using while True).
#     User must enter the word 'done' (without quotes) to end the loop

print ("\n run by Michael Savino")
print ()

while True:  
    Temp_F  = input("What is the temperature in Fahrenheit you want to convert? , or 'done' (no quote) to stop: ")
    if Temp_F  == 'done':
        break
    else:
        Temp_C = (float(Temp_F) - 32)/1.8
        #print()
        print(f"\nThe equivalent of {Temp_F} degree Fahrenheit is {Temp_C:.2f} Celsius")
        print()

print('\nThanks for using this tool!\n')
