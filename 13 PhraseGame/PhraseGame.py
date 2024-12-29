#
# Bryce Kepple
# 13 PhraseGame
#

#import the draw scoreboard function
from DrawScoreboard import draw_scoreboard


def display_guessed_letters(guessed_letters):
    #creates an empty string witch will hold the letters that will be displayed
    letters_guessed=""

    #creates a loop that runs through the string of letters that have been guessed
    for letter in guessed_letters:

        #takes each letter and adds them to the string that will be displayed followed by a comma and a space
        letters_guessed+=(letter.lower()+", ")

    #gets rid of the final comma and space from the string and returns it
    letters_guessed=letters_guessed[:-2]
    return letters_guessed


def display_secret_phrase(secret_phrase, guessed_letters):

    #creates a string that will hold the letters that will display the correctly guessed letters and the ones that haven't been guessed
    secret_phrase_check =""

    #loops through each letter in the secrete phrase
    for letter in secret_phrase:

        #if the lowercase version of the letter in the secret phrase is in the lowercase version
        # of the letters guessed then it adds that letter to the empty string above
        if letter.lower() in guessed_letters.lower():
            secret_phrase_check+=letter

        #if it's a space it adds a space
        elif letter==" ":
            secret_phrase_check+=letter

        #if its not in the guessed letters or a space it prints out a dash representing an un guessed letter
        else:
            secret_phrase_check+="-"


    return secret_phrase_check





def play_game(secret_phrase, total_guesses):

    #sets the guessed letters to empty and the incorrect guesses to 0
    incorrect_guesses = 0
    guessed_letters=""

    #loops until broken
    while True:

        #runs the display function above and if there is no dashes then it means the word was fully guessed
        #prints out a win message and breaks the loop
        if "-" not in display_secret_phrase(secret_phrase,guessed_letters):
            print("="*39)
            print("You Won!")
            print("The phrase was:", secret_phrase)
            print("="*39)
            break

        #draws the scoreboard
        print(draw_scoreboard(total_guesses,incorrect_guesses))

        #checks to make sure the user hasnt guessed incorrectly too many times if they have then prints you loose and breaks loop
        if incorrect_guesses>=total_guesses:
            print("="*39)
            print("No more guesses left. Game over!")
            print("The phrase was:", secret_phrase)
            print("="*39)
            break

        #displays how much of the phrase has been guessed and the letters guessed
        print("Secret Phrase:  ",display_secret_phrase(secret_phrase, guessed_letters))
        print("Guessed Letters:",display_guessed_letters(guessed_letters))

        #prompts the user to guess a letter
        guess=input("Enter a letter to guess or \'!\' to end the game\n")

        #if the user types an exclamation point print a goodbye and breaks the loop
        if guess =="!":
            print("="*39)
            print("Game ended early")
            print("="*39)
            break

        #checks to make sure a letter was typed in
        elif guess.isalpha():

            #if the lowercase version of the letter typed is in the lowercase guesses then tells user they already guessed it
            if guess.lower() in guessed_letters.lower():
                print("You already guessed",guess.lower())

            #if the lowercase guess is in the lowercase secret phrase then it adds to the guessed letters
            elif guess.lower() in secret_phrase.lower():
                guessed_letters+=guess

            #if it's not in the phrase then it adds an incorrect guess and adds the letter to the guessed letters
            else:
                incorrect_guesses+=1
                print("No,",guess,"is not in the phrase")
                guessed_letters+=guess

        #if a letter wasn't typed tells user not a valid guess and runs them back through the loop
        else:
            print("Not a valid guess!")


if __name__ == "__main__":
    phrase = input("Enter a secret phrase: ")
    guesses = int(input("Enter a number of allowed guesses: "))
    play_game(phrase, guesses)



