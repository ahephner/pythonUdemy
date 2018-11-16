#make an iterator that aggregates elements left to right
#cool way to loop over two list and combin them together
#runs left to right through list 
x = [1,2,3]
y= [1,2,3]

a = zip(x,y)
print(a)


b = [1,2,3]
c = [1,2,3]
d=[]
d.append(b)
d.append(c)

print(d)

e = [sum(x)for x in zip(*d)]

print(e)
 #carefull on list that are uneven in length
length = [[1,2,3,4,5], [10,12,14]]

uneven= [sum(x)for x in zip(*length)]

print(uneven) #->returns 11, 14, 17  NOT 11, 14,17, 4, 5

#lists for zipping
list_keys = list(['Dog', 'Cat'])
list_values = list(['bark', 'purr'])

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

key=['a', 'b', 'c']
values = [1,2,3]
dictionary = dict(zip(key, values))
print(dictionary)

# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels


# Make a string with the value 'PA': state
state = "PA"

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(dict(data))

# Print the DataFrame
print(df)
