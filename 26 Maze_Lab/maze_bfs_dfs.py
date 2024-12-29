# Jason Reeves
# Maze Solver (for PyCharm)
from logging import raiseExceptions

from state import State
import copy

# Constants
START_CHAR = 'S'
END_CHAR = 'E'
SPACE_CHAR = ' '
FILL_CHAR = '*'


def generate_start_state(maze_data):
    #creates a state object and then makes a deep copy of it
    state = State()
    state_copy = copy.deepcopy(maze_data)

    #sets the matrix of the state to the copy of the data and then searches through every row and colum for the start point
    state.matrix=state_copy
    for i in range(state.max_rows()):
        for ii in range(state.max_cols()):

            # sets the state start cords and then returns the state
            if state.get_char_at(i,ii)==START_CHAR:
                state.row=i
                state.col=ii
                return state
    raise Exception("maze error: no starting position found could not generate starting state,")




def next_states(state):

    # creates a list that will hold all legal moves
    legal_moves = []

    # makes a copy of the current state, moves it north
    state_copy = state.__deepcopy__()
    state_copy.row-=1

    #if it reaches the end it returns that state
    if state_copy.get_char() == END_CHAR:
        return [state_copy]

    #if it is in a blank space adds it to the legal move list
    if state_copy.get_char() == SPACE_CHAR:
        legal_moves.append(state_copy)

    # makes a copy of the current state, moves it east
    state_copy = state.__deepcopy__()
    state_copy.col += 1

    # if it reaches the end it returns that state
    if state_copy.get_char() == END_CHAR:
        return [state_copy]

    # if it is in a blank space adds it to the legal move list
    if state_copy.get_char() == SPACE_CHAR:
        legal_moves.append(state_copy)

    # makes a copy of the current state, moves it south
    state_copy = state.__deepcopy__()
    state_copy.row+=1

    # if it reaches the end it returns that state
    if state_copy.get_char() == END_CHAR:
        return [state_copy]

    # if it is in a blank space adds it to the legal move list
    if state_copy.get_char() == SPACE_CHAR:
        legal_moves.append(state_copy)

    # makes a copy of the current state, moves it south
    state_copy = state.__deepcopy__()
    state_copy.col -= 1

    # if it reaches the end it returns that state
    if state_copy.get_char() == END_CHAR:
        return [state_copy]

    # if it is in a blank space adds it to the legal move list
    if state_copy.get_char() == SPACE_CHAR:
        legal_moves.append(state_copy)

    #returns the list
    return legal_moves


def print_maze(maze_data, desc="MAZE"):
    #prints out the current state of maze
    print(desc)
    for row in maze_data.matrix:
        print("".join(row))


def breadth_first_solution(maze_data):

    #sets the start state, adds it to the queue, sets what round it is to 0, then makes an empty set for visited moves
    start_state = generate_start_state(maze_data)
    queue = [start_state]
    round=0
    visited = set()

    #loop will stay active while there are legal moves
    while len(queue) > 0:

        #removes first in queue and adds 1 to rounds
        current_state = queue.pop(0)
        round+=1

        #if we are at the end space print out maze and return our current state
        if current_state.get_char()==END_CHAR:
            print("BFS Round", round)
            current_state.print_maze()
            return current_state

        #if the current space we are on is empty add a fill character
        if current_state.get_char()==SPACE_CHAR:
            current_state.set_char(current_state.row,current_state.col,FILL_CHAR)

        #adds the current space we are on to the visited set
        visited.add((current_state.row,current_state.col))

        #checks all the available moves and adds all the ones we havent done yet to the queue
        available_moves = next_states(current_state)
        for move in available_moves:
            if (move.row,move.col) not in visited:
                queue.append(move)

        #prints the round we are on and the current maze
        print("BFS Round", round)
        current_state.print_maze()

    #if the loop breaks that means there is no solution and return none
    return None

def depth_first_solution(maze_data):

    # sets the start state, adds it to the queue, sets what round it is to 0, then makes an empty set for visited moves
    start_state = generate_start_state(maze_data)
    stack = [start_state]
    visited = set()
    round=0

    # loop will stay active while there are legal moves
    while len(stack) > 0:

        #removes the last item in the stack, and adds 1 to the rounds
        current_state = stack.pop(-1)
        round+=1

        # if we are at the end space print out maze and return our current state
        if current_state.get_char()==END_CHAR:
            print("DFS Round", round)
            current_state.print_maze()
            return current_state

        # if the current space we are on is empty add a fill character
        if current_state.get_char()==SPACE_CHAR:
            current_state.set_char(current_state.row,current_state.col,FILL_CHAR)

        #adds the current state to the visited set
        visited.add((current_state.row,current_state.col))

        # finds the available moves and reverses them because of DFS
        available_moves = next_states(current_state)
        available_moves.reverse()

        #searches through the moves and adds the ones we haven't done to the stack
        for move in available_moves:
            if (move.row,move.col) not in visited:
                stack.append(move)

        #prints the round and the current state of the maze
        print("DFS Round", round)
        current_state.print_maze()
    return None


def read_maze(maze_file):
    """
    :param maze_file: Name of the maze file to read in.
    :return: a matrix (list of lists) containing the maze data.

    Note that the maze data consists of characters where each character has specific meaning:
    # - a wall
    . - empty space
    S - Start position in maze
    E - End position in maze
    """
    with open(maze_file) as f:
        tmp_lines = f.readlines()
        lines = []
        for line in tmp_lines:
            if not line.startswith('//'):
                lines.append(line.strip())
        horizontal_len = len(lines[0])
        line_num = 0
        matrix = []
        for line in lines:
            l = len(line.strip())
            if len(line) != horizontal_len:
                raise Exception(f'inconsistent maze length of {len(line)} compared to {horizontal_len} on line {line_num}')
            row = [c for c in line]
            matrix.append(row)
            line_num += 1

        # valid_matrix(matrix)
        return matrix


def main():
    #converts file into matrix
    maze_file = "mazedata.txt"
    maze_data = read_maze(maze_file)

    #prints out the results for the DFS 
    print("---- DFS Path ----")
    dfs_solution = depth_first_solution(maze_data)
    if dfs_solution is None:
        print("No solution found")
    else:
        print_maze(dfs_solution, "---- DFS Solution ----")

    print("----------------------")
    #
    #prints out the solution for the BFS
    bfs_solution = breadth_first_solution(maze_data)
    if bfs_solution is None:
        print("No solution found")
    else:
        print_maze(bfs_solution, "---- BFS Solution ----")


if __name__ == "__main__":
    main()