# basic syntax

# for item in iterable_obj;
    #do something with item
    
#iterable_obj is what you want iterate over
#item new var reps where you are in the loop currently

for item in 'hi':
    print(item)
    
for i in range(1, 10):
    print(i)
    
    #range does not give last number 
    # range(7) gives 0-6
    # range(1,5) gives 1-4
    #range(1,10,2) third int tells you how many to skip so 1, 3, 5, 7, 9
    #range(7,0, -1) get 7, 6,5,4,3,2,1 
    
    #to print range example
    
nums = range(10)
print(list(nums))


for k in range(10):
    print(k)

#nested for statements
#dont use the x in first for loop it just says to run what is inside it three times

for x in range(3):
   for num in range(1, 11):
    print("*" * num) 