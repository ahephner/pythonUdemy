#ordered collection or grouping items
#CAN NOT CHANGE
numbers = (2,3,4)

print(numbers)

#faster than lists 
#code is safer to bugs always treat the same

months = ('Jan', 'Feb', 'Mar', 'April')

print(months[3])

#in dictionary if address would never change 
#Cant use a list as a key in a dictionary

location = {
    (1009, 'South Street'): 'Home Office',
    ('Eller RD'): 'Secondary',
    (123, 'Easy ST'): 'Third'
}

print(location[(1009,'South Street')])

#looping through tuples
#some dictonary methods return tuples
teams = {'chicago': 'bears', 'detroit': 'lions', 'green bay': 'packers', 'minn': 'vikings'}

print(teams.items())


for i in months:
    print(i)
    

    
#can nest

nested = (2,3,4,(5,6), 7)


print(nested)
print(nested[3])
print(nested[:4])
