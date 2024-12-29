#
# Bryce Kepple
# Battleship
#
#imports load and print functions for the grid
from battleship_helper import load_grid
from battleship_helper import print_grid




def enter_coordinates():
    #creates a dictionary of possible letters and number corrasponding
    xcords={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
    #has user input letter a-j in and if its incorrect tell user and loops again
    while True:
        xcord_input=input("Enter the Colum of your shot (A-J): ")
        xcord_input=xcord_input.upper()
        if xcord_input=="Q" or xcord_input== "QUIT":
            return None

        elif xcord_input not in xcords:
            print("invalid cords")
            continue

        else:
            break
    #has user input number 1-10 and loops until user correctly does so
    while True:

        ycord_input=input("Enter the y cord coordinates (1-10): ")

        if ycord_input=="q" or ycord_input=="quit":
            return None

        elif not ycord_input.isdigit():
            print("invalid coordinates")

        elif int(ycord_input)<1 or int(ycord_input)>10:
            print("invalid coordinates")

        else:
            break
    #turns x cord into a number and the y cord minus one and then returns a list that has x,y cord
    xcoordinate=xcords[xcord_input]
    ycoordinate=int(ycord_input)-1
    return [xcoordinate,ycoordinate]





def fire(shot,grid):
    #takes the coordinate and checks to see if theres a ship their
    #if there isnt returns a .
    if grid[shot[1]][shot[0]] == ".":
        return "."

    #if there is turns that place into a . and returns the letter of the ship hit
    else:
        hit=grid[shot[1]][shot[0]]
        grid[shot[1]][shot[0]]="."
        return hit


def check_win(grid):
    #checks every item in the list and if its all "." then returns that u won
    for row in grid:
        for item in row:
            if item != ".":
                return False
    return True

def main():
    #Creates a variable for turns, variable for the file, and makes a grid with all "."
    turns=0
    file=input("Enter the file name: ")
    fire_grid=[]
    for x in range(0,10):
        new_row=[]
        for y in range(0,10):
            new_row.append(".")
        fire_grid.append(new_row)

    #tries to load the grid with give file if it doesnt work prints out an error message and ends the game
    try:
        oppenent_grid=load_grid(file)
    except FileNotFoundError:
        print("ERROR:Opponent file not found")
        return

    #creates a loop that the game runs in
    while True:
        #prints out the grd, runs the enter coords function and sets it to a variable and then puts that variable into
        # the fire function which is also assigned to a variable
        print_grid(fire_grid)
        shot=enter_coordinates()

        #if q was typed shot will equal none so it checks for that and ends game if it is equal to none
        if shot is None:
            print("you failed to sink enemy ships. You Lose!")
            print("Game Over")
            break
        shot_result=fire(shot,oppenent_grid)

        # check the fire board to see if you are trying to shoot a letter if so prints message then sends you through the loop again
        if fire_grid[shot[1]][shot[0]] != ".":
            print("you already shot here!")

        #checks to see if that fire function returned a letter, if it did it puts that letter on the fire grid then turns goes up by 1
        elif shot_result!=".":
            fire_grid[shot[1]][shot[0]] = "H"
            turns+=1
            print("Hit!")

        #if it didnt hit a ship that means it was a miss so it prints an M in the spot and adds 1 to turns
        else:
            fire_grid[shot[1]][shot[0]] = "M"
            oppenent_grid[shot[1]][shot[0]] = "."
            turns+=1
            print("Miss!")
        #checks to see if you won, if you did prints a victory line and tells you how many turns it took, if not go through loop again
        if check_win(oppenent_grid):
            print("All ships have been sunk!")
            print("Victory took",turns,"turns.")
            break













if __name__ == '__main__':
    main()

