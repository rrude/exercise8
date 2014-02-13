#!/usr/bin/env python

import sys
from random import randint


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #process raw text into list of words with punctuation?
    word_list = corpus.split()
    #now generate dict of key pairs with value empty list [] no repeats
    bi_grams = {}
    #go through word_list and add key pairs to dict  using range to run the length of word_list and track index
    # goes to len - 1 so that the last tuple has a value
    for i in range(1, len(word_list[:-1])):
        #creates a tuple of each word pair
        key = word_list[i-1], word_list[i]
        #check if it already exists as key tuple 
        if bi_grams.get(key):
            # append the adjacent word to the key into the value list
            bi_grams[key].append(word_list[i+1])
            pass
        #if tuple key doesn't already exist it adds to dictionary bi_grams
        else:
            # create a key pair and value at the same time (with the adjacent word to the key as its value)
            bi_grams[key]=[word_list[i+1]] 
    #print bi_grams          
    return bi_grams

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # Taking the dictionary created in make_chains. We need to start somewhere (?) random and select a key
    # Now that we have a key, we'll select a random value 
    # Using a while loop to control the length of our output string
    target_string_length = 140
    """ to randomly select a starting point, we'll create a list of keys from the dictionary
    Then we'll select a random index number from 0 to len(the key list)-1. Then we'll assign the tuple
    from the list to a start variable. Then we'll get the values from the dictionary using that start variable
    """
    #for now a tuple key place to start in dict
    key_list = chains.keys()
    random_index = randint(0, len(key_list)-1)
    #this gives us a tuple value from our dict to use to start the 
    start = key_list[random_index]
    #checking dict to see if our start tuple exists returns list of values from that key if it does exist
    #need an if statement if tuple doesn't exist in dict
    values = chains.get(start)
    #creating a random index to use to pick a random word from the specified tuples list of values 
    # used -1 in the randint argument because randint is inclusive so len(values) would be out range
    random_index = randint(0 , len(values)-1)
    #use this index to choose word from list
    next_word = chains[start][random_index]
    #now we put the next_word together with the tupal we started with in a list format so we can still add to it
    output_list = [start[0], start[1], next_word] 
    counter = len(" ".join(output_list))
    # We'll use a while loop set to end when the counter reaches target_string_length.
    # Utilizing the last two elements of output_list as our "start", we'll grab a random 
    # value from start's values. 
    # append the random word from start's values to output_list. 
    new_start = (output_list[-2], output_list[-1])
    while counter < target_string_length and chains.get(new_start):
        new_values = chains.get(new_start)
        new_random_index = randint(0, len(new_values)-1)
        new_next_word = chains[new_start][new_random_index]
        output_list.append(new_next_word)
        #print output_list
        counter = len(" ".join(output_list))
        new_start = (output_list[-2], output_list[-1])
 
        # 
    #print counter
    #eventually we're going to create a while loop to control length of output characters but first we need string

    #print random_index

    #print values
    #print next_word
    #print output_list
    #print counter
    return output_list

def remove_parens(working_list):
    for i in range(0, len(working_list)):
        if "(" in working_list[i] or ")" in working_list[i]:
            working_list[i] = working_list[i].strip(")(") 
    return working_list
def trim_end(working_list):
    if "." in "".join(working_list):    
        for each in working_list[::-1]:
            #if statement will check list item for character
            if not "." in each:
                working_list.pop()
            else:
                break
    else:
        working_list[-1] = working_list[-1]+"."
    return working_list  
def deal_with_upper(working_list):
    #first remove all capitals with exception for I
    for i in range(0,len(working_list)):
        if not working_list[i] in ["I","I'll","I've","I'm"]:
            working_list[i] = working_list[i].lower()
    working_list[0] = working_list[0].title()
    for i in range(0,len(working_list)-1):
        if "." in working_list[i]:
            working_list[i+1] = working_list[i+1].title()


    return working_list

# The scrubber function will take the output of make_text (string? list?)
# and truncate at the last . or ! or ?
# It will return the string that will be printed out in the main function
def scrubber(make_text_output):
    #take the list and clean it up, cut fragment sentence up to last punctuation
    #going backwards through each item in make_text_output list
    removed = remove_parens(make_text_output)
    trimmed = trim_end(removed)
    case_fixed = deal_with_upper(trimmed)

    string_text = " ".join(case_fixed)
    return string_text

def main():
    args = sys.argv
    # args produces a list containing the script
    # and the filenames that we pass through on the command line
    # args = [script.py, file.txt]
    # assigning the file to a variable for added clarity
    textfile = args[1]
    # opening and setting text file to read mode using flag "r" a function of open 
    f = open(textfile, "r")
    #now we read the file
    input_text = f.read()
    #time to close the file below
    f.close()
    #below will call the function make_chains()
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    finished_text = scrubber(random_text)
    print finished_text

if __name__ == "__main__":
    main()
