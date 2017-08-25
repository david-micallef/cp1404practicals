"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the value that is entered is not a number.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when the denominator value entered is a zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    To avoid the possibility of a ZeroDivisionError, you could make a while 
    loop to keep asking for a value until it is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")