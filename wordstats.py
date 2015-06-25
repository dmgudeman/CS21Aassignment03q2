# -----------------------------------------------------------------------------
# Name:         wordstats
# Purpose:      Counts and categorizes words in a text file
#
# Author:       David Gudeman
# Date:         June 23, 2015
# -----------------------------------------------------------------------------
"""
Receives text file from the user then counts the words, alphabetizes them
to a new file and returns a longest word and the top 5 most frequent words

Input: filename of a text file. Takes it from the keyboard
Output: to display: a longest word and the top 5 most frequently used words
        to a new file: an alphabetized lists of the words in the file and
        how often they are used

"""

def count_words (filename):
    """
    function accepts a filename as parameter, opens the file, reads
    the file by line, coverts all characters to lowercase and returns only
    alpha characters. It counts how many times a word is used in the text and
    does not keep duplicates

    parameter: filename
    returns: dictionary with words as key and their frequency of use as value
    """
    word_dict = {}                 # initialize an empty dictionary
    with open(filename, 'r', encoding='utf-8') as raw_file: # open input file

        for line in raw_file:               # read the file by line
            for word in line.split():       # parse line into words
                word = word.lower()         # convert to lower case
                word = ''.join(c for c in word if c.isalpha())  # alpha filter
                if not word:
                    break                   # break loop if char is not alpha
                word_dict[word] = word_dict.get(word, 0) + 1 # tally frequency
    return word_dict                        # return the dictionay

def get_input():
    """
    Obtain the input from the user
    prompt the user for input until they enter a non-empty string
    return the string entered by the user

    """
    filename = str(input('Please enter the name of your file:'))
    while filename == "":
      filename = str(input('Please enter the name of your file:'))
    return filename

def report(word_dict):
    """
    takes in a dictionary of lowercase words and calculates the longest word,
    the top five most frequently used words.  This data are returned to the
    display. It alphabetizes the entire dictionary and writes this to the
    file "out.txt".

    parameter:  dictionary
    returns:    longest word - to display
                top five frequenlty used words - to display
                an alphabetized list with frequency - to the file out.txt

    """
    longest_word = sorted (word_dict, key=len, reverse=True) # sort large -> s
    longest_word = longest_word[:1]             # slice off a largest
    print("\nA longest word is '" + longest_word[0] + "'") # to display

    print("\nThe top five most frequent words are:") # context for data
    top_five = sorted(word_dict, key=word_dict.get, reverse=True) # freq sort
    top_five = top_five[:5]                     # slice off top five
    for word in top_five:                       # iterate them to display
        print(word + ':', word_dict[word])

    alphabetized = sorted(word_dict)            # alphabetize the dictionary
    list2 = ''                                  # intialize and empty list
    for word in alphabetized:                   # iterate through list output
        combo_word = word + ": ", str(word_dict[word])
        list = ''.join(combo_word)
        list2 += "\n " + list      # prepare string of data formatted as column
    with open('out.txt', 'w', encoding='utf-8') as my_file: # open output file
        my_file.write(list2)        # write the string output file

def main():
    # get the input filename and save it in a variable
    # call count_words to build the dictionary for the given file
    # save the dictionary in the variable word_count
    # call report to report on the contents of the dictionary

    filename = get_input()
    word_dict = count_words(filename)
    report(word_dict)

if __name__ == '__main__':
    main()
