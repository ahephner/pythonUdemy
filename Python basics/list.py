#list is similar to array

task =['my', 'first', 'list', 'hey', 'hey']

print(task)

#dont have to all be the same
not_all_same =[12, 'numbers', True]


#len = lenght
len(not_all_same)

r = range(1,5)

print(r) #outcome range(1,5)

print(list(r)) #outcome [1,2,3,4]

#accessing data in lists 

print(task[1])

fun = not_all_same[2]
print(fun)

print(task[-1])

#check value in list use terminal 

12 in not_all_same

people = ['aj', 'jack', 'Geoff', 'Kelly']

#capitalize aj
people[0] = 'AJ'

#change jack to Jackie
people[1] = 'Jackie'

#Geof to Jeff

people[-2] = 'Jeff'

print(people)

#loop through list

loop = [1,2,4,5,6]

for x in loop:
    print(x)
    if x == 4:
        print('I am 4')


#need to set the var going through first
#can't get print out with a for loop only a while loop
color = ['red', 'white', 'blue']
g=0 
while g < len(color):
    print(f'{g}:{color[g]}')
    g += 1 
    
sounds= ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ''

for t in sounds:
    result += t.upper()

print(result)