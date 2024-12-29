#
# Bryce Kepple
# FBI keywords
#



def load_corpus(file):

    #opens the file and splits every line up
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        data=[]

        #goes through each line and adds every word to the data
        for line in lines:
            words = line.split(" ")

            #makes sure only letters of the word are taken (no periods or anything)
            for word in words:
                for thing in word:
                    if thing.isalpha():
                        continue
                    else:
                        word=word.replace(thing, "")

                # appends the word to the data as lowercase and gets rid of any possible newline characters
                data.append(word.lower().strip())
                
        #returns the data
        return data


def load_keywords(file):

    #opens the keywords text and splits it up by line
    with open(file, 'r') as f:
        lines = f.read().splitlines()

        # sets the threshold and removes it from the lines
        thresh=lines.pop(0)
        words=[]

        #goes through each word and makes them lowercase before adding the words to the list of keywords
        for line in lines:
            line=line.lower()
            words.append(line)

        #sets the thresh to a float, makes a tuple with the thresh and word list and them returns the tuple
        thresh=float(thresh)
        keywords=(thresh,words)
        return keywords

def find_keywords(corpus, keywords):
    word_count=0
    sus_word=0

    # goes through every word and increments the word count by one
    for word in corpus:
        word_count+=1

        #if the word is in the keywords the sus word count also increments by one
        if word in keywords[1]:
            sus_word+=1

    #returns the percent of sus words in the document
    return sus_word/word_count





def main():

    #gets files from user
    text_file=input("Enter the text to scan: ")
    keyword_file=input("Enter the keyword file: ")

    #runs functions
    words=load_corpus(text_file)
    keywords=load_keywords(keyword_file)

    #takes the thresh percent and turns it into a percent and prints it
    thresh_percent=keywords[0]*100
    print(f"The provided threshold is {thresh_percent:.2f}%")

    #finds the amount of sus words in the doc then prints it as a percent
    doc_percent=find_keywords(words, keywords)
    doc_percent=doc_percent*100
    print(f"Keywords make up {doc_percent:.2f}% of the file")

    #if the doc percent is higher than the thresh percent it prints a message saying the file is suspicious
    if doc_percent > thresh_percent:
        print("The document \'"+text_file+"\' is suspicious!")


if __name__ == '__main__':
    main()