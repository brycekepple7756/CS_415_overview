#Bryce Kepple
#9/9/24
#Strings lab
#defining the function with one parameter
def rephrase_sentence(sentence):
    # using index method to find the first space in the sentence and sets first word to be everything til that space
    space= sentence.index(" ")
    first_word=sentence[0:space]

    #does the same thing as above except uses the rindex to find the last space
    last_word_index=sentence.rindex(" ")+1
    last_word=sentence[last_word_index:]

    #sets mid sentence to be everything except the first and last word
    mid_sentence=sentence[space+1:last_word_index]

    #switches the first and last word of the sentence
    print("i have rephrased that line to read:")
    print(last_word,mid_sentence+first_word)

#gets sentence from user by input, then runs program
sentence=input("enter a line of text. no punctuation needed. \n ")
rephrase_sentence(sentence)




















