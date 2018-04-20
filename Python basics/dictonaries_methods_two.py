playlist = {
    'Title': 'Songs', 
    'author': 'AJ',
    'songs': [{'Title': 'Song One', 'Artist': ['Singer1'], 'duration': 2.41},
    {'Title': 'Song Two', 'Artist': ['Singer2'], 'duration': 5.11},
    {'Title': 'Song Three', 'Artist': ['Singer3'], 'duration': 3.00}
    ]
}

time_length = 0 

for i in playlist['songs']:
    time_length += i['duration']

print(time_length)

#syntax {_:_ for_ in_}

numbers = dict(first = 1, second = 2, third = 3)

#because we are using .items() we need two values to loop through to look at the key and value 
squared_numbs = {key: value **2 for key,value in numbers.items()}

print(squared_numbs)


#interweave two vars

str1 = 'ABC'
str2 = '123'

#creating a new dictonary with str1 as key and str2 as value
#loop through the first var
#need range so we can get index telling loop where to start
#len(str1) to tell loop how far to go 

combo = {str1[i]:str2[i] for i in range(0, len(str1))}
print(combo)

#conditional logic with dictionaries
#not limited to only using values can put on keys as well 
list_nums = [1,2,3,4,5,6]

check = {k:('even' if k % 2 == 0 else 'odd') for k in list_nums}

print(check)
