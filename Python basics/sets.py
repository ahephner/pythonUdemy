#sets 

#formal mathematical sets 
#collection of data WITHOUT duplicates and no order
s = set({1, 2,3,4,})

# or 
t = {3,4,5,6,6}
#print(t)-> 3,4,5,6

scores = [10,10,4,12,7,2,4,4]
#get unique scores
print(set(scores))

#set methods 

#add

s.add(2)
#wont throw error here just wont add duplicate to set 
s.add(2)

#remove
#will throw error if value is not in set
s.remove(7)

#discard if value is not there you will not get an error
s.discard(12)

#copy

s2 = s.copy()

s2 is s #-> false 

#UNION character = |
#combine two sets with

#if i had two lists of employees and need to combine

stl = {'James', 'Rick', 'Dave'}
ia = {'Dave', 'Glenn', 'Dick', 'Lauren'}

everyone = stl | ia

#intersect character = & tells you who is in both lists

stl & ia # -> 'Dave'

#set comprehension

{x**2 for x in range(10)}

string = 'hello'

{x for x in string if x in 'aeiou'}
