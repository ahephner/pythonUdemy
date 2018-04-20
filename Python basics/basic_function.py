#syntax
#def name_function():
    #do something
from random import random  


def say_hi():
    print('hi')
    
say_hi()

#return
def seven_sq():
    return 7**2
    print('hey hey player') #-> wont run the return takes you out of the function
print(seven_sq())

def coin_flip():
    #generate random num 0-1 
    #between 0-.5 heads
    if random() > 0.5:
        return 'tails'
    else:
        return 'heads'
        
print(coin_flip())

#generate evens to 50

def gen_evens():
    return {i for i in range(0,50) if i %2 ==0}
       

print(gen_evens())
#using inputs
def square(i):
    return i*i
    
print(square(2))

#using mult input

def times(x,y):
    return x*y

print(times(4,9))


#parameters are passed here when creating function
def hey_there(fname, lname):
    print(f'Hey there {fname} {lname}')
    
#here 'big', 'guy' is an argument. You pass arguments to functions
#create functions with parameters
hey_there('big', 'guy')
