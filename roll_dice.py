def dice_game():
    import random
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    while dice1==6:
        if dice2==6:
            print('Success!')
    while dice2==6:
        if dice1==6:
            print('Success!!')
    else:
        print('Sorry no success')
def play_again():
    user_choice1=input('Do you want to play again? ')
    if 'y' in user_choice1:
        dice_game()
    else:
        print('No problem. Bye.')
        exit()

user_choice=input('Do you want to roll dice? ')

if 'y' in user_choice:
    user_times=int(input('How many times? '))
    for i in range(user_times+1):
        dice_game()
        play_again()
else:
    print('No problem!!')
