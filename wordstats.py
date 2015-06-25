# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:
#
# Author:
# Date:
# -----------------------------------------------------------------------------
"""
Docstring: Enter your one-line summary here

and your detailed description
"""
import string
# The following imports are needed for the draw cloud function.
import tkinter
import tkinter.font
import random
import string
import operator
# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length = 0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
            word: input_count[word] for word in input_count
            if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame=tkinter.Frame(root)
    frame.grid()
    my_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256,4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word]* ratio))
        label = tkinter.Label(frame, text = word, font = word_font, fg = color)
        label.grid(row = my_row % 5, column = my_row // 5 )
        my_row +=  1
    root.mainloop()

# Enter your own helper function definitions here

def count_words (filename):
    # build and return the dictionary for the given filename
    words = {}
    with open(filename, 'r', encoding='utf-8') as raw_file:

        for line in raw_file:
            for word in line.split():
                word = word.lower()
                word = ''.join(c for c in word if c.isalpha())
                if not word:
                    break
                words[word] = words.get(word, 0) + 1
    return words

def get_input():
    """
    # Obtain the input from the user
    # prompt the user for input until they enter a non-empty string
    # return the string entered by the user
     #
    """
    filename = str(input('Please enter the name of your file:'))
    while filename == "":
      filename = str(input('Please enter the name of your file:'))
    return filename

def report(word_dict):
    # report on various statistics based on the given word count dictionary
    longest_word = sorted (word_dict, key=len, reverse=True)
    longest_word = longest_word[:1]
    print("\nA longest word is '" + longest_word[0] + "'")

    print("\nThe top five most frequent words are:")
    top_five = sorted(word_dict, key=word_dict.get, reverse=True)
    top_five = top_five[:5]
    for word in top_five:
        print(word + ':', word_dict[word])

    alphabetized = sorted(word_dict)
    list2 = ''
    for word in alphabetized:
        combo_word = word + ": ", str(word_dict[word])
        list = ''.join(combo_word)
        list2 += "\n " + list
    print(list2)
    print(type(list2))
    with open('out.txt', 'w', encoding='utf-8') as my_file:
           my_file.write(list2)
        # alphabetized.write(combo_word)

def main():
    # get the input filename and save it in a variable
    # call count_words to build the dictionary for the given file
    # save the dictionary in the variable word_count
    # call report to report on the contents of the dictionary

    # If you want to generate a word cloud, uncomment the line below.
    # draw_cloud(word_count)
    filename = get_input()
    word_dict = count_words(filename)
    report(word_dict)

if __name__ == '__main__':
    main()
   # count_words(filename)
