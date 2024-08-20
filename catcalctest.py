i = 0
while i < 10:
    i += 1
    age = int(input('how many months old is your cat?:'))
    if age <= 12:
        age = age * 1.25
    elif 13 <= age <= 24:
        age = (age - 12) * .8333 + 15
    elif age >= 25:
        age = (age - 24) * .3333 + 25
    print('Your cat is', age, 'human years old')
    user_input = input('type quit to end program, type anything else to continue:')