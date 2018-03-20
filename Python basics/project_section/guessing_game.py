import random

random_number = random.randint(1, 10)
test = 5

#handle user guess
# if correct tell them they win
#otherwise tell them too high or too low



while True:
    guess = int(input('Guess a number 1-10: '))
    if guess < random_number:
        print('Too Low')
    elif guess > random_number:
        print('Too high')
    else:
        print('Correct')
        play_again = input('Go again y/n? ')
        if play_again == 'y':
            random_number = random.randint(1, 10)
            guess = None
        else:
            print('Later...')
            break 

    

        


#bonus ask to play again 