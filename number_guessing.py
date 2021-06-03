#number guessing game
import random
n=random.randint(1,100)
play=input('Do you want to guess a number (Yes/No) ? ')
if play=='Yes':
    print('I have a secret number ')
elif play=='No':
    print('No problem')
    exit()
counter=0
if play=='Yes':

    guess=int(input('Here is your chance to make a guess '))
if guess==n:
    print('Wow.You got it right in first go!')
elif guess!=n:
    counter=1
    print('Try guessing again!')
    print("Heres the next hint: ")
    counter=2
    if n>guess:
        print('The secret number is greater than your guess ')
    elif n<guess:
        print('The secret number is smaller than your guess ')
    guess=int(input('Try guessing again '))
if guess==n:
    print('Great job!!')
else:
    counter=3
    print('Here is the third hint ')
    if n%2==0:
        print('The secret number is even ')
    elif n%2!=0:
        print('the secret number is odd')
    guess=int(input('take a guess again '))
    if guess==n:
        print('Bingo!!')
    else:
        print('Tha secret number was ',n,'.Better luck next time!')
