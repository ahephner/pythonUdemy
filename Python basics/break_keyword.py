# break is an early controlled exit 

while True:
    command = input("Type 'exit' to quit program: ")
    if (command == 'exit'):
        break 
    
for i in range(101):
    print(i)
    if(i == 3):
        break 
    
times = int(input('how many times do i have to tell you clean your room!'))
#takes in number entered then runs through it starts on 0 so thats why it prints 5 times

for time in range(times):
    print('clean your room!')
    if time >= 4:
        print('do you listen')    
        break 

#the break function will stop the loop where it is
#here will take in the above code but kill the loop at the first step

times = int(input('how many times do i have to tell you clean your room!'))

for time in range(times):
    break 
    print('clean your room!')
    if time >= 4:
        print('do you listen')  