#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #process raw text into list of words with punctuation?
    word_list = corpus.split()
    #now generate dict of key pairs with value empty list [] no repeats
    bi_grams = {}
    #go through word_list and add key pairs to dict  using range to run the length of word_list and track index
    for i in range(1, len(word_list)):
        #creates a tuple of each word pair
        key = word_list[i-1], word_list[i]
        #check if it already exists as key tuple 
        if bi_grams.get(key):
            pass
        #if tuple key doesn't already exist it adds to dictionary bi_grams
        else:
            bi_grams[key]=[] 
    print bi_grams          
    #print word_list
    return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

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
