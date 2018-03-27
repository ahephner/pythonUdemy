#list methods add

#append
#cant add more than item
scores = [3,4,12,4]

scores.append(3)

scores.append('string')

#extend can pass in a list that adds to the end of that list
#if you did .append([]) you would nest a list in a list 
scores.extend([2, 3])
print(scores)

#insert
#first pass where you want the item placed in the index
scores.insert(2, 'HEY')
#based off last count
scores.insert(-2, 'neg')

print(scores)

teachers = []

teachers.extend(['Colt', 'Blue', 'Lisa'])

print(teachers)

#List Methods- Delet

build = [1,3,4,5]
 #delete all
build.clear()

item1 = [1,3,4,5]

#returns last item and removes from list 
question = item1.pop()
print(question)
print(item1)

#removes the index and returns it
#can use to grab specific var or just simple remove it 
sel = item1.pop(1)
print(sel)
print(item1)
#remove
#will remove first item from a list of value you give

pets = ['dog', 'cat', 'fish', 'fish']
pets.remove('fish')
print(pets)