#== equal too
1 == 1 #true
a == A #false capitilize

# != not equal too

1 != 1 #false
a != A #true

#> or < greater than less than
1 > 1 #false
2> 1 #true

#>= greater than or equal too <= less than or equal too 
age = 18 

if age >= 18: 
    print('adult')
else: 
    print('your not an adult')

#Logical Operators

#and both have to be true
dad = 60 
mom = 55

if mom >50 and dad > 50: 
    print('time to retire')

#or 1 has to be true

city = input('where do you live')

if city is 'indianapolis' or city is 'fort wayne':
    print('Indiana')
else: 
    print('somewhere else')

#not 

#2-8 2 dollar ticket
#65 + 5 dollar ticket
#everyone else 10 dollar
#gives you the opposite
age = 21

if (age>= 2 and age<= 8 or age>=65):
    print("10 dollars")
else: 
    print('discount')

a = 1
a == 1 #true
a is 1 #true

a = [1, 2]
b = [1, 2]

a== b  #true

a is b #false is checks to see if their saved in the same 
#place in the data and this a good way to find this out
#[] are seperate objects in memory
#== checks for values

c = b
b is c #true becuase they both point toward same data in memory
