#### Header
# Name: Breck Echelberger
# UIN: 332003322
# Class: ITSV 272
# Section: N/A
# Project: HW 4 Part 1
# Date: 4/9/2024

#### Imports

#### Functions
def MyFactorial():
    y = int(input("Enter a number and I will calculate the factorial: "))

    if y <= 0:
        print("Oops, Try Again!")
    else:
        counter = 1
        for i in range(1, y + 1):
            counter *= i
        return counter

#### Main
print("My DIY facotrial is equal to:", MyFactorial())