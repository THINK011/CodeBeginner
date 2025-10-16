# CodeBeginner
BasicCode

#Password Strength Checker

import string

#Ask user input 
password = input("Enter your password:> ")

#Check Conditions
length = len(password) >= 8  # they're output boolen
lower = any(char.islower() for char in password) # any() output boolen but need to True at least one #.islower() decided True or False
upper = any(char.isupper() for char in password) 
digit = any(char.isdigit() for char in password)
special = any(char in string.punctuation for char in password)

#Use Sum
total = sum([length,lower,upper,digit,special])

# Evaluate Strength
if total <= 2:
    print("Weak")
elif total == 3 or total == 4:
    print("Medium")
else:
    print("Strong")

# Check not conditions
print("\nPassword Checker")
if not length:
    print("- Must to be length 8 character")
if not lower:
    print("- Must be lowercase letters")
    print("- Must be uppercase letters")
if not digit:
    print("- Must be include digit")
if not special:
    print("-- Must be include strong special")
