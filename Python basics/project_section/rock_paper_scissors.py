print('...rock...')
print('...paper...')
print('...scissors...')

player1 = input('Player 1:')

# if player1 != "": 
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
print('NO CHEATING!!!!!!!!!')
player2 = input('Player 2: ')
if player1 == 'rock' and player2 == 'paper':
    print('player 2 wins')
elif player1 == 'paper' and player2 == 'scissors':
    print('player2 wins')
elif player1 == 'scissors' and player2 == 'rock':
    print('player2 wins')
elif player1 == 'rock' and player2 == 'scissors':
    print('player1 wins')
elif player1 == 'scissors' and player2 == 'paper':
    print('player1 wins')
elif player1 == 'paper' and player2 == 'rock':
    print('player1 wins')
elif player1 == player2:
    print('Tie game')
else: 
    print('flush')
# else:
#     print('Player 1 does not seem to want to play!')

