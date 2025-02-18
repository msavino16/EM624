# Author:  Michael Savino

# Exercise 02
# Password program

# This program will intake a password and check to make sure it follows a set of requirements

# The program is written as a loop (using while True).
#     User must enter the word 'done' (without quotes) to end the loop

print ("\n run by Michael Savino")
print ()

while True:  
    password  = input("Please enter a password, or 'done' (no quote) to stop: ")
    if password  == 'done':
        break
    else:
        if len(password) < 6: 
            print("The password is too short!")
            continue
        
        if len(password) > 12: 
            print("The password is too long!")
            continue
        
        hasLetter = False
        hasNumber = False
        hasSpecial = False
        specialChar = "!@#$%&?"
        
        for char in password:
            if char.isalpha():
                hasLetter = True
            if char.isdigit():
                hasNumber = True
            if char in specialChar:
                hasSpecial = True
        
        if not hasLetter or not hasNumber: 
            print("The password must contain both numbers and letters!")
            continue
        
        if not hasSpecial:
            print("The password must contain one of the following special characters: !, @, #, $, %, &, or ?.")
            continue

        if "password" in password.lower(): 
            print("The password must not contain the word password in it!")
            continue
        
        print("Password accepted!")

print('\nThanks for using this tool!\n')
