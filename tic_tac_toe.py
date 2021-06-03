#creating the board
the_board={'T1':' ','T2':' ','T3':' ',
           'M1':' ','M2':' ','M3':' ',
           'D1':' ','D2':' ','D3':' '
       }
board_keys=[]
for key in the_board:
    board_keys.append(key)
print('T1  |  T2  |  T3')
print('____+______+____')
print('M1  |  M2  |  M3')
print('____+______+____')
print('D1  |  D2  |  D3')
def print_board(board):
    print(board['T1'],' | ', board['T2'],' | ', board['T3'])
    print(' __ + __ + __ ')
    print(board['M1'],' | ',board['M2'],' | ', board['M3'])
    print(' __ + __ + __ ')
    print(board['D3'],' | ',board['D2'],' | ', board['D3'])
    print('***************')

def game():
    turn='X'
    count=0
    for i in range(10):
        print_board(the_board)
        move=input('Its your turn,Move to which place? ')
        if the_board[move]==' ':
            the_board[move]=turn
            count+=1
        else:
            print('This place is filled.\n Move to another place? ')
            continue
#now to check who0 won
        if count>=5:
            if the_board['T1']==the_board['T2']==the_board['T3']!=' ':   #top row
                print_board(the_board)
                print('\n GAME OVER!!')
                print(turn,' Won')
                break
            elif the_board['M1']==the_board['M2']==the_board['M3']!=' ':   #middle row
                print_board(the_board)
                print('\nGAME OVER!!')
                print(turn,' Won')
                break
            elif the_board['D1']==the_board['D2']==the_board['D3']!=' ':    #last row
                print_board(board)
                print('\n GAME OVER!!')
                print(turn,' Won')
                break
            elif the_board['T1']==the_board['M2']==the_board['D3']!=' ':    #left diagonal
                print_board(th_board)
                print('\nGAME OVER!!')
                print(turn,' Won')
                break
            elif the_board['T3']==the_board['M2']==the_board['D1']!=' ':     #right diagonal
                print_board(the_board)
                print('\nGAME OVER!!')
                print(turn,' WOn')
                break
            elif the_board['T1']==the_board['M1']==the_board['D1']!=' ':     #first column
                print_board(the_board)
                print('\nGAME OVER!!')
                print(turn, " Won")
                break
            elif the_board['T2']==the_board['M2']==the_board['D2']!=' ':    #second column
                print_board(the_board)
                print('\n GAME OVER!!')
                print(turn,' Won')
                break
            elif the_board['T3']==the_board['M3']==the_board['D3']!=' ':    #third column
                print_board(board)
                print('\n GAME OVER!!')
                print(turn,' WON')
                break
        if count==9:
            print_board(board)
            print('Its a tie')
        if turn=='X':
            turn='0'
        else:
            turn='X'
user_choice=input('DO you want to play?(Y/N)')
if user_choice=='Y':
    game()
else:
    print('Ok')



