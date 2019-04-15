#the *args allows you to pass several values to a function it does not limit them 
#you can call anything after the * args however is standard practice 

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word) #=> luke
print(many_words) #=> lukeleiahanobidarth

def num(*args):
    add = 0

    for i in args:
        add += i 
    return add
test = num(3,4)

print(test)
