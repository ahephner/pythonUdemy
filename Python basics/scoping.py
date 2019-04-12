#calling global will update the global value from inside a fungtion
#function reference local then global
# 
#  num = 5

# def func1():
#     num = 3
#     print(num)

# def func2():
#     global num
#     double_num = num * 2
#     num = 6
#     print(double_num)

    # func1() => 3
    # func2() => 10 but value of global num is 6
    # Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team
    

    # Change the value of team in global: team
    team = 'justice league'
#call function without calling team still equals team titans
change_team()
# Print team
print(team) #-> justice league


# Nested functions

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings have to pass it to the inner function!!
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


#closure notice how inner function has the ability to go to the outter function and get a value in this case n 
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
