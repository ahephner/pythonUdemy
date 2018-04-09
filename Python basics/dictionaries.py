#consists of key value pairs 

me = {
    'name': 'AJ',
    'age': 31,
    'owns_dog': True,
    12: 'Favorite Number'
}

#another approach to creating a dictionary
#key dont need quotes around. 
take_two = dict(name = 'jackie', age = 31)

#accessing this information
#use dictionary name then [key]

print(me['age'])

#looping over dictionaries 

#loop through values with .values()
for x in me.values():
    print(x)

#loop through keys with .keys()
for k in me.keys():
    print(k)
    
    
#access both with .items
print(me.items())


#because there are two items we need to values to loop through
#also have access to both items 
for i, a in me.items():
    print(f'this is {i} and it is {a}')
    
#test for existence of key or value in a dictionary
# this would be a good way to set up a if conditional 
#if me['name'] is true:


print('name' in me) #true
print('car' in me)#false 
print(31 in me) #this test for keys only not values
#this will look for vaules 
print(31 in me.values())