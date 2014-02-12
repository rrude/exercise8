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
    """ 
    # Use a while loop to control the length
    While len(output) < 10: 
    # We want a list of keys so that we can choose one at random
    key_list = #get list of keys
    print key_list
    # we are creating a random index number to grab a tuple from key_list
    start = key_list[randint(0, len(key_list))]
    print start
    """
    #for now a tuple key place to start in dict
    start = ('Hey', 'Jude')
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
    print counter
    #eventually we're going to create a while loop to control length of output characters but first we need string

    print random_index

    print values
    print next_word
    print output_list
    return "This is a random text"
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
    print random_text

if __name__ == "__main__":
    main()
