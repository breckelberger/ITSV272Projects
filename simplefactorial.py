x = int(input("Enter a number: "))
i = int(input("How many iterations? "))
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

print("Answer is equal to: ", answer)