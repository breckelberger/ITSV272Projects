#### Header
# Name: Breck Echelberger
# UIN: 332003322
# Class: ITSV 272
# Section: N/A
# Project: HW 4 Part 2
# Date: 4/9/2024

#### Imports
import math

#### Functions
def MyFactorial(y):
    if y < 0:
        print("Oops, Try Again!")
    else:
        counter = 1
        for i in range(1, y + 1):
            counter *= i
        return counter
    
#### Main
X = int(input("What is the value of X? "))
SP = int(input("How many iterations? "))

if SP <= 0 or X <= 0:
    print("Try again and pick a positive integer greater then zero.")
else:
    Sum = 0
    C = 0
    while C<=SP:
        w = 2*C
        Expression = ((X**(2*C)) / (MyFactorial(w)) * ((-1)**C))
        Sum += Expression
        C += 1
    print("The value of my DIY cosine is:", Sum)


print("The value of Python's built-in function for cosine is:", math.cos(X))