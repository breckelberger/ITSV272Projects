#### Header
# Name: Breck Echelberger
# UIN: 332003322
# Class: ITSV 272
# Section: N/A
# Project: HW 5 Part 1
# Date: 4/24/2024

#### Imports
import math

#### Functions
def MyExponent():
    counter = 0
    answer = 0
    factorial = 1

    while counter < i:
        exponent = x ** counter
        for y in range(1, counter+1):
            factorial *= y
        taylor  = exponent/factorial
        answer += taylor
        counter += 1
    return answer

#### Main
x = int(input("Enter a number: "))
i = int(input("How many iterations? "))

print("Answer is equal to: ", MyExponent())
print("The value of Python's built-in function for exponents is:", math.exp(x))