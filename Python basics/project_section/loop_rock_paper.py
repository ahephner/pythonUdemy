import random 
chance = ['paper', 'rock', 'scissors']

player_wins = 0
computer_wins = 0 

while player_wins< 2 and computer_wins < 2:
    print('...rock...')
    print('...paper...')
    print('...scissors...')
    print(f'score: player1 has {player_wins} computer has {computer_wins}')
    
    player1 = input('Player 1:').lower()
    computer = random.choice(chance)
    
    print(f'computer says {computer}')
    if player1 == 'rock' and computer == 'paper':
        print('computer wins')
        computer_wins += 1
    elif player1 == 'paper' and computer == 'scissors':
        print('computer wins')
        computer_wins += 1
    elif player1 == 'scissors' and computer == 'rock':
        print('computer wins')
        computer_wins += 1
    else:
        print('player1 wins')
        player_wins += 1
        
print(f'final score: player1 has {player_wins} computer has {computer_wins}')
