# Company A Copyright 2023

# This program is a module for the phrase game program
# This program takes user input about total_guesses
# and incorrect_guesses. Each guess gets a box and if
# that guess has been used that box gets an x in it.

# This is the function that draws the scoreboard
def draw_scoreboard(total_guesses, incorrect_guesses):

    # the string we are putting everything in
    string = ""

    # for each guess:
    for i in range(1, total_guesses + 1):

        # create the top of each square
        # and keep it on the same line
        string += "+-----"

    # add this at the end to complete the design and add a new line
    string += "+" + "\n"

    # declare the tuple to store the patterns of each line
    # exclude the seperator at the end because each part
    # will cover the previous end
    tupl = ("|\\\\ //", "| \\V/ ", "| /.\\ ", "|// \\\\")

    # loop through the tuple
    for design in range(len(tupl)):

        # for each guess:
        for i in range(1, total_guesses + 1):

            # if the current i is less than or equal to the incorrect guess count
            if i <= incorrect_guesses:

                # print the design and keep the line going
                string += tupl[design]

                # if it is the end of incorrect guesses
                if i == incorrect_guesses:
                    # close of the line
                    string += "|"

            # in any other case
            else:

                if incorrect_guesses == 0 and i == 1:
                    string += "|"
                string += "     |"

        # concatenate a new line
        string += "\n"

    # exact same thing as we did with the top we do on bottom
    for i in range(total_guesses):
        string += "+-----"
    string += "+"

    # return the value
    return string


# make it accessible to other .py files
if __name__ == '__main__':
    # print the prompt for guesses_allowed
    print("Enter number of guesses allowed between 1 and 11")

    # get the data
    guesses_allowed = int(input())

    # print the prompt for incorrect_guess_count
    print("Enter number of incorrect guesses")

    # get the data
    incorrect_guess_count = int(input())

    # pass the two variables to the function and see the results
    print(draw_scoreboard(guesses_allowed, incorrect_guess_count), end="")
