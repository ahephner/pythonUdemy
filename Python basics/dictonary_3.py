#Dictionaries are useful whenever you have to items that you wish to link together,
#and for example storing results for quick lookup.
#Create an empty dictionary
months = {}
#Create a dictionary with some pairs

# Note: Each key must be unique
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" } 
#months[1-12] are keys and "January-December" are the values
#Print all keys
print "The dictionary contains the following keys: ", months.keys()
#Output:

#The dictionary contains the following keys:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#11, 12]
#Accessing

#To get a value out of a dictionary, you must supply its key, you cannot provide
#the value and get the key
whichMonth = months[1]
print whichMonth
#Output: January
#To delete an element from a dictionary, use del
del(months[5])
print months.keys()
#Output:
#[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
#To add a new element to a dictionary, assign a value to a new key

months[5] = "May"
print months.keys()
#Output:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#To update an element of a dictionary, assign a new value to its key
months[1] = "Jan"
print months
#Output:
#{1: 'Jan', 2: 'February', 3: 'March', 4: 'April', 5... }

#Sorting
sortedkeys = months.keys()
print sortedkeys
#Output:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#Dictionaries and Loops
#Iterating over keys
for key in months:
    print key, months[key]
#Output:
#1 January
#2 February
#3 March
#4 April
#5 May
#6 June
#7 July
#8 August
#9 September
#10 October
#11 November
##12 December
#Iterating over (key, value) pairs
for key, value in months.iteritems():
    print key, value

#print "The entries in the dictionary are:"
for item in months.keys():
    print "months[ ", item, " ] = ", months[ item ]

#Combining List and Dictionary
#Example of a list of dictionaries
customers = [{"uid":1,"name":"John"},
    {"uid":2,"name":"Smith"},
           {"uid":3,"name":"Andersson"},
            ]
print customers
#Output:
#[{'uid': 1, 'name': 'John'}, {'uid': 2, 'name': 'Smith'}, {'uid': 3, 'name':
#'Andersson'}]
#Print the uid and name of each customer

for x in customer:
    print x["uid"], x["name"]
#Output:
#1 John
#2 Smith
#3 Andersson

#Modify an entry
#This will change the name of customer 2 from Smith to Charlie

customers[2]["name"]="charlie"
print customers
Output:
[{'uid': 1, 'name': 'John'}, {'uid': 2, 'name': 'Smith'}, {'uid': 3, 'name':
'charlie'}]

#Add a new field to each entry
#for x in customers:
 #   x["password"]="123456" # any initial value

print customers
#Output:
#[{'password': '123456', 'uid': 1, 'name': 'John'}, {'password': '123456', 'uid':
#2, 'name': 'Smith'}, {'password': '123456', 'uid': 3, 'name': 'Andersson'}]

#Delete a field
del customers[1]
print customers
#Output:
#[{'uid': 1, 'name': 'John'}, {'uid': 3, 'name': 'Andersson'}]
#Delete all fields
# This will delete id field of each entry.
for x in customers:
    del x["id"]
#Output:
#[{'name': 'John'}, {'name': 'Smith'}, {'name': 'Andersson'}]
