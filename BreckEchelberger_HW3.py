import random

print("Let's play Rock, Paper, Scissors!")

player_one = input('Player one, pick one: "R" for Rock, "P" for Paper, or "S" for Scissors: ')
computer_one = random.choice(['R', 'P', 'S'])

if player_one == computer_one:
    print("It was a tie! Try Again!")
elif player_one == 'R' and computer_one == 'S':
    print("You picked Rock and the computer picked Scissors so you win!")
elif player_one == 'P' and computer_one == 'R':
    print("You picked Paper and the computer picked Rock so you win!")
elif player_one == 'S' and computer_one == 'P':
    print("You picked Scissors and the computer picked Paper so you win!")
elif player_one == 'R' and computer_one == 'P':
    print("You picked Rock and the computer picked Paper so you lose!")
elif player_one == 'P' and computer_one == 'S':
    print("You picked Paper and the computer picked Scissors so you lose!")
elif player_one == 'S' and computer_one == 'R':
    print("You picked Scissors and the computer picked Rock so you lose!")