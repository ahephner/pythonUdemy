# for x in range (0,21,1):
#     if x == 4 or x == 13:
#         print(f'{x}: unlucky')   
#     elif x % 2 == 0:
#         print(f'{x}: even')
#     elif x % 1 == 0: 
#         print(f'{x}: odd')


##little bit cleaner way to right a fizz buzz 
for i in range(0, 21):
    if i == 4 or i == 13:
        y =  'unlucky'
    elif i %2 == 0: 
        y = 'even'
    else:
        y = 'odd'
    print(f'{i} is {y}')

    