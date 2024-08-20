#### Header
# Name: Breck Echelberger
# UIN: 332003322
# Class: ITSV 272
# Section: N/A
# Project: HW 5 Part 2
# Date: 4/24/2024

#### Imports

#### Functions

#### Main
elements = int(input("Enter the number of elements you want in the list: "))
elementlist = []
counterone = 0
countertwo = 0

for i in range(elements):
    element = float(input(f"Input value of element {counterone} in this list: "))
    elementlist.append(element)
    counterone += 1

for i in range(elements):
    print("The position of the element is ",countertwo,"and the value stored in the element is ", elementlist[i])
    countertwo += 1

print(":-)")