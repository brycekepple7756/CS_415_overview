#
# Bryce Kepple
# Battleship helper
#

def load_grid(filename):
    with open(filename,'r') as f:
        lines=f.readlines()
        f.close()
        grid=[]
        for line in lines:
            row=[]
            for i in range(len(line)):
                character=line[i]
                row.append(character)
            grid.append(row)
        for i in range(len(grid)-1):
            grid[i]=grid[i][:-1]
    return grid

def print_grid(grid):
    print("   A B C D E F G H I J ")
    i=0
    for row in grid:
        temp_row=" "
        for item in row:
            temp_char=item+" "
            temp_row=temp_row+temp_char
        i=i+1
        print(f"{i:<2}{temp_row:<2}")





