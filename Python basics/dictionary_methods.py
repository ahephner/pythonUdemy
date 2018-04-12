#clear - empty a dictionary

d = dict(a=1, b=2, c=3)

d.clear

#copy make a copy/ not true copy saved in different places in memory

b = dict(a=1, b=2, c=3)
c = b.copy()

print(c == b) #true
print( c is b) #false
#fromkeys creates key-value pairs good way to assign inital values

z = {}.fromkeys('a', 'b')
y = {}.fromkeys('a', [2,3,4])

print(z)
print(y)

#get 

sample = dict(name= 'aj', email= 'test.com')

print(sample.get('name'))

#if there is no value it returns none instead of an error
#good for if there is none then do this

print(sample.get('phone'))