#
# Bryce Kepple
# Escape Room
#

#first choice made by the user with three outcomes
choice1=input("You are in a room with a door and stairs. Which way will you go? :")

#the first outcome based off the first choice, this leads to us down the door path which leads to another choice
if choice1=='door':

    #this is the next choice down the door path, the user chooses which button to choose
    doorchoice1=input("There are 2 buttons on the door. Which do press? (1 or 2) :")

   #choosing one causes the user to lose
    if doorchoice1=='1':
        print("A trap door opens underneath your feet and you fall. GAME OVER")

    #choosing 2 allows them to win
    elif doorchoice1=='2':
        print("The door opens. You're free. YOU WIN")

    #anything else will result in a loss
    else:
        print("You hurt your finger pressing a button that doesn't exist. GAME OVER")

#the second outcome based off choice one, this leads us down the stairs path which will lead us to another choice
elif choice1=='stairs':

    #the next choice for the user has 3 outcomes
    stairschoice1=int(input("There are 10 cookies on a plate how many do you eat? :"))

    #if they type anything less then 2 they lose
    if stairschoice1<2:
        print("Your friends eat all the rest. You get too hungry and have to quit. GAME OVER")


    #if they type any number bigger then 5 they lose
    elif stairschoice1>5:
        print("You get a stomach ache and can't search any more. GAME OVER")

    #if they pick 3 they are prompted with another question which is based off how many cookies they ate, if they answer correct they win, otherwise they loose
    elif 2<=stairschoice1<=5:
        stairschoice2= float(input("You notice a secret keypad under the cookie plate. Enter the weight of the remaining cookies in ounces, if each one weighs 1.5 ounces. :"))
        cookie_answer= (10-stairschoice1)*1.5
        if stairschoice2==cookie_answer:
            print("A secret door opens for you to exit. YOU WIN")
        else:
            print("Incorrect. GAME OVER")

#the third outcome of the first choice which just ends the game
else:
    print("That's not a valid direction. You trip and fall. GAME OVER")