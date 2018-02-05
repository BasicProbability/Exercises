'''
Created on Sep 13, 2015

@author: Philip Schulz
'''

import sys
from string import punctuation
from collections import Counter

# Create the counter that will do most of the work
word_frequencies = Counter()

# Ask user for path to text file
textFile = input('Please enter the path to the text file you want to read: ')

with open(textFile) as text:
    for line in text:
        # Get the String in the right format and add it to the counter
        words = line.lower().split()
        word_frequencies.update(words)

    
# I keep a list of in which all occurrence frequencies are stored in ascending order.
# There are different ways to go about this, but I will use this list to go retrieve the most/least common words further down.
frequencies = sorted(set(word_frequencies.values()))
    
# Define a map from frequencies to sets of words. This is exactly the opposite direction of the word_frequencies counter.
frequency_dictionary = dict()
for word, frequency in word_frequencies.items():
    # If I want to assign a value to a non-existent key, I will get a keyError. That's why I first make sure the key exists.
    if frequency in frequency_dictionary:
        frequency_dictionary[frequency].add(word)
    # If the key does not exist, I add it and set its value to a set containing only one word. IMPORTANT: I have to put this
    # word in a list (by using square brackets). Otherwise, the word will be decomposed into a set of characters.
    else:
        frequency_dictionary[frequency] = set([word])
        
# To make my life easier, I sort the words in each set alphbetically. My word sets are now sorted lists of words.
for frequency, word_set in frequency_dictionary.items():
    frequency_dictionary[frequency] = sorted(word_set)
        
# I set the user_answer to None initially.
user_answer = None
# Infinite loop that can only be broken by user input
while(True):
    user_answer = input('Please choose one of the following options.\n1) Retrieve most frequent words.'
              + '\n2) Retrieve least frequent words.\n3) Retrieve frequency of a specific word.'
              + '\n4) Exit.\n')
    
    if user_answer == '1':
        
        # This is my way of forcing the user to enter a sensible amount of words. I just keep nagging him until he does.
        amount = 0
        while (amount < 1):
            amount = int(input('How many of the most frequent words would you like? Please enter a positive number:'))
        
        # I use the iterator variable i to keep track of how many word-frequency pairs I have printed already
        i = 1
        # This is a convenience variable. I do not strictly need it. My innermost break statement ensures
        # that I will not print more than the required amount of words. However, the outer loops will keep executing,
        # which means that I will waste a lot of time on doing things that have no effect (since the innermost loop
        # will get broken each time we get there). By using the broken variable I can break all three loops simultaneously.
        broken = False
        while (i <= amount):
            # Some interesting piece of syntax that I found online: frequencies[::-1] traverses the list from behind.
            # The syntax is frequencies[start:stop:step_size]. Since I did not specify start or stop, the whole list
            # will be traversed. Since my step_size is -1 it will be traversed in reverse order.
            for freq in frequencies[::-1]:
                words = frequency_dictionary[freq]
                for word in words:
                    # If I already have printed all the words I need, I break. Otherwise, I print the next word.
                    if i > amount:
                        broken = True
                        break
                    else:
                        print(word + '\t' + str(freq))
                        i += 1
                # This is where I use broken to break the outer for-loop
                if broken:
                    break
            # And here I break the while-loop
            if broken:
                break
                    
    elif user_answer == '2':
        
        amount = 0
        while (amount < 1):
            amount = int(input('How many of the most frequent words would you like? Please enter a positive number:'))
        
        i = 1
        broken = False
        while (i <= amount):
            # The only change to the routine above is that I traverse the list in its normal order (lowest to highest).
            for freq in frequencies:
                words = frequency_dictionary[freq]
                for word in words:
                    if i > amount:
                        broken = True
                        break
                    else:
                        print(word + '\t' + str(freq))
                        i += 1
                if broken:
                    break
            if broken:
                break
                    
    # If you understand the counter, then this should be straightforward.
    elif user_answer == '3':
        word = input("Which word's frequency would you like to obtain?\n")
        if word in word_frequencies:
            print(word + '\t' + str(word_frequencies[word]))
        else:
            print('Sorry, this word does not occur in the text.')
        
    # Exit on user input. Notice that I could also just have broken the while loop, but using sys.exit() here seems
    # cleaner to me. After all, I don't need to worry about which loop I am breaking.
    elif user_answer == '4':
        sys.exit(0)
        
    # Standard output if the user entered bogus. The while loop starts from the beginning again.
    else: 
        print('Sorry, I do not understand this. Please choose again.\n')