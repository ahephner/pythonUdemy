#continue to execute while truthy

user_response = None

while user_response != 'Please':
    user_response = input("You didn't use the magic word: ")

msg = input('whats the password ')
while msg != 'blue':
    print('wrong')
    msg = input('whats the password ')
print('yes!')

#infinte loop did not give it a way to step through
# num = 1
# while num<11:
#     print(num)

# here num += 1 step up by one

num = 0
while num<10:
    print(num)
    num += 1