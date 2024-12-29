from copy import deepcopy


class State(object):
    """
    A state object for BFS an DFS. This encapsulates the current state of searching and includes the current position
    in the maze that is expanded from. row and col values in this State object contain the row and col position in the
    maze that is being expanded. If this was a graph, row and col combine to specify which is the current node.
    """
    def __init__(self):
        self.row = 0
        self.col = 0
        self.matrix = []

    def get_char(self):
        """
        Returns the current character from the maze.
        :return:
        """
        return self.get_char_at(self.row, self.col)

    def get_char_at(self, r, c):
        """
        Returns the character at position (r,c) from the maze.
        :param r:
        :param c:
        :return:
        """
        return self.matrix[r][c]

    def max_rows(self):
        """
        Returns the maximum number of rows in the maze.
        :return:
        """
        return len(self.matrix)

    def max_cols(self):
        """
        Returns the maximum number of columns in the maze.
        :return:
        """
        return len(self.matrix[0])

    def __deepcopy__(self, memodict={}):
        """
        Returns a deep copy of this state.
        :param memodict: an optional parameter for memoization of previous states.
        :return: a copy of this state suitable for transformation into a "next" state derived from this state.
        """
        new_guy = State()
        new_guy.matrix = deepcopy(self.matrix)
        new_guy.row = self.row
        new_guy.col = self.col
        return new_guy

    def set_char(self, row, col, c):
        """
        Sets the character at position (row,col) from the maze.
        :param row:
        :param col:
        :param c:
        :return: None
        """
        self.matrix[row][col] = c

    def print_maze(self):
        """
        Prints the maze contained in this state.
        :return: None
        """
        for row in self.matrix:
            print("".join(row))

    def print(self, s):
        """
        Prints the maze contained in this state with a header string, s, prior.
        :param s: a header string
        :return: None
        """
        print(s)
        self.print_maze()
