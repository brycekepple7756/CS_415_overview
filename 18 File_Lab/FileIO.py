#
# Bryce Kepple
# File IO Lab
#


def get_tokens_from_file(file_name):

    #opens the file
    with open(file_name, 'r') as f:
        text= f.read()

        #splits the text after a spcae and places it in a list
        tokens=text.split()

        #prints out the list and returns the list then closes file
        for token in tokens:
            print(token)
        f.close()
        return tokens




get_tokens_from_file("test.txt")

#opens the file and gets the text
def get_characters_from_file(file_name):
    with open(file_name, 'r') as f:
        text= f.read()

        #loops through every character and prints it out along with ACII number then closes file
        for character in text:
            print(f'{ord(character):>3d} {character}')
    f.close()

get_characters_from_file("test.txt")


def get_ints_from_file_and_sum(file_name):
    total=0
    #uses first function to separate the numbers then adds them all up
    with open(file_name, 'r') as f:
        for token in get_tokens_from_file(file_name):
            total+=int(token)
        print(total)

    #closes file
    f.close()

get_ints_from_file_and_sum("integers.txt")
