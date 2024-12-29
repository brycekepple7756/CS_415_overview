#
# Bryce Kepple
# Quiz 2 programming
#
from tree import *

#
def load_trees():

    #opens file
    with open('trees.csv', 'r') as f:

        #creates an empty list
        tree_data = []

        #goes through every line, splits it up and gets rid of the /n
        for line in f:
            split_line = line.split(',')
            split_line[2] =split_line[2].strip()

        # makes a temp row and gets the data from the striped line and then appends the row
            new_row=[]
            for i in range(3):
                    new_row.append(split_line[i])
            tree_data.append(new_row)

        #goes through that data and turns them into tree objects and checks for errors
        line_numb=0
        tree_list=[]
        for row in tree_data:
            line_numb=line_numb+1
            try:
                tree=Tree(row[0],row[1],row[2])
                tree_list.append(tree)
            except ValueError:
                print("WARNING: Invalid data at line",line_numb)

        #returns list of tree objects
        return tree_list







def find_nearest_tree(x,y,tree_list):
    #gets a list of tuples with the tree object and the distance
    distances = []
    for tree in tree_list:
        distances.append((tree,tree.get_distance(x,y)))
    # sorts the list based off the second item in the tuple
    closest_tree=min(distances, key=lambda x: x[1])

    #returns the closest tree
    return closest_tree[0]


def main():

    #loads the trees
    tree_list=load_trees()
    print("Successfully loaded",len(tree_list),"tree(s) from file")

    #gets the x and y coords
    while True:
        try:
            x_coord=float(input("Enter x-coordinate of your location: "))
            break
        except ValueError:
            print("Invalid entry!")
    while True:
        try:
            y_coord=float(input("Enter y-coordinate of your location: "))
            break
        except ValueError:
            print("Invalid entry!")

    #prints out the closest tree and the info about it
    closest_tree=find_nearest_tree(x_coord,y_coord,tree_list)
    print("the closest tree is",closest_tree.name,"at",closest_tree.x,",",closest_tree.y)


if __name__ == "__main__":
    main()