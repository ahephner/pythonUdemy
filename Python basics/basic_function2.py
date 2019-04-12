# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 +'!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)

#new tuple
nums = (3, 4,6)

# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums


# Construct even_nums
even_nums = ( 2,  num2, num3)
print(even_nums)

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1 = shout_all('congratulations','you')[0]
yell2 = shout_all('congratulations', 'you')[1]
# Print yell1 and yell2
print(yell1)
print(yell2)


#Import the pandas package with the alias pd.
#Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting DataFrame to df.
#Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
#Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, 
#add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.

# Import pandas
import pandas as pd 

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
       langs_count[entry] = 1 

# Print the populated dictionary
print(langs_count)
