#----1----
# --Original code
while True:
    #prompts and receives user input
    char = input('Please enter an alphabetical character:')
    if not len(char) == 1 or char.isdigit(): #checks if input is more than one character
        print ('Invalid input')
    else:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y': #checks if input is a vowel
            print ('False')
        else:
            print ('True')

'''
Errors and Fixes:
    Parts of code were not indented properly (line 7 and lines 10-12)
    Added check for the vowel 'o' on line 9 as it did not check for that vowel
    Had to fix logic on line 9, as it was only checking if char == 'a' and not e,i,o,u,and y
    Fixed logic on line 6 to ensure that the input is one character only, as before it would allow an input of zero characters
    Added an additional check on line 6 for is the charater is a digit, and to print invalid input if it is
'''

#----2----
# --Original code
numbers = [10, 23, 45, 66, 78, 99, 120, 133, 142] # this is the input
categories = {'even': [], 'odd': [], 'multiple of 5': []} # defining the categories

for num in numbers: # looping into the input numbers
    if num % 2 == 0:
        categories['even'].append(num)
    else:
        categories['odd'].append(num)

    if num % 5 == 0:  # Incorrect condition
        categories['multiple of 5'].append(num)

# printing the results
for key, value in categories.items():
    print(key, ' - ', value)

'''
Errors and Fixes
Added a colon to the end of the if statement at line 30, since it was missing
Switched the logic on like 35 to properly check for divisble by 5, as it used // before which is not the correct check
Added a comma in like 39 for "key, value" part of logic instead of it being "key value"
Fixed append method on line 36 to be parenthesis instead of brackets 
'''