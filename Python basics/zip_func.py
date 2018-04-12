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


