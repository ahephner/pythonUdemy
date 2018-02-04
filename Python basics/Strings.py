#print("Hello!")
#print("AJ Hephner")

#numbers in python

#integer 3 whole numbers float 6.1 it's decimals 

# ** is exponent 2 ** 3 = 8

# % modulo like js 10 % 3 = 1 
test = 3 

print(test)
#// integer division 10//3 returns an int not a float

 # variables in python 

 #x = 100 or all, at , once = 2, 3,4 assign multiple vars at once
 #must start with letter or underscore
 #should be snake case this_is_snake_case
 #should be lowercase
 # if there are two underscores that means dont touch the variable



#Data Types boo, int, string, 
#list like an array is an ordered sequence of values of other data types, e.g. [1,2,3] 

#Dynamic Typing means Python allows us to reset var data type

#None is pythons version of null 

str1 = "hello"
str2 = "world"

str3 = str1 + " " + str2

print(str3)

#Plus Equals

name= 'AJ'
name += 'Hephenr'

print(name)

people = 100
people -= 34
print(people)

#F-String
#Ints don't blend with strings so we have to do the following
#f' {var goes in here} '

r = 38
print(f"your guess of {r} is wrong!")
#could do things you do outside of strings
print(f"nice try {name} but your guess of {r} is off by at least {r+50}+")

#Older ways to do this
formatted = "I am {} and  {} old".format(r, name)

#INDEX OF STRING

cat = "archie"
cat[0] #returns a
cat[3] #returns h 
cat[-1] #returns e
cat[-3] #returns h

#change data type

dec = 23.4585

intg = int(dec) #float to int 

my_list = [2,3,4]
my_list_to_string = str(my_list)