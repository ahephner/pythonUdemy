#Notice the spacing it's very important to follow this when
#making the code spread it all out
#4 spaces is proper indent 


# ask for age
age = input('How old are you?')
#if age is empty don't run 
if age !="":
    #turns age into an int comes as a string on input
    age = int(age)
#18 - 21 wrist bands
    if age >= 18 and age< 21:
        print('You can enter, but need a wristband')
    #21+drink
    elif age >= 21:
            print("You can enter and drink")
    #under too young
    else: 
        print("cant enter")
else: 
    print('Please enter an age')        