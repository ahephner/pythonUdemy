#my solution below works but not best practice

x = range(int(input('how many times do I have to tell you to clean your room ')))

for i in x:
    print('Clean your room!')

#their solution

time = input('How many times to clean up room? ')
time = int(time)
#notice how they use range down here to get it to loop through
#big issue for solving repl.it challenges constent error trying to loop through a digit

for i in range(time):
    print(f'{i +1}: clean your room')