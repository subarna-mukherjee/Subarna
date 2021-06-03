# rock paper scissor game
game = ['rock', 'paper', 'scissor']
import random
comSel = random.randint(0, 2)
computer = game[comSel]
#print(computer)
user = input('Do you want to play the game (Yes/No)? ')
while user == 'Yes':
    userChoice = input('Enter any one (Rock/Paper/Scissor) ')
    if userChoice == computer:
            print('Its a tie')
    elif userChoice == 'Rock':
        if computer == 'Paper':
                print('Computer wins! Paper can cover the scissor')
        elif computer == 'Scissor':
                print('You win! Your rock can squash my scissor')
    elif userChoice == 'Paper':
            if computer == 'Rock':
                print('You win! Paper can cover the rock')
            elif computer == 'scissor':
                print('I win! My scissor can cut your paper')
    if userChoice == 'Scissor':
        if computer == 'Paper':
                print('You win! your scissor can cut my paper')
        elif computer == 'Rock':
                print('I win! My rock can squash your paper')
if user == 'No':
    print('No problem')
