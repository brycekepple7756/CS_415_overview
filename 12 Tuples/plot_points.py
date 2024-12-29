#
#Bryce Kepple
#Tuple lab
#

#imports necessary functions to graph points
from lab_plot import plot_points

#defines a function that gathers the x cord, y cord, and color of the point
def enter_point():
    x_cord=float(input("Enter the x coordinate of your point: "))
    y_cord=float(input("Enter the y coordinate of your point: "))
    color=input("Enter the color of your point: ")

    #puts all the info recorded from the user into a tuple and then returns that tuple
    data=(x_cord,y_cord,color)
    return data

#creates an empty list
points=[]

#makes a loop that allows the user to enter as many points as they want til the loop is broken
while True:

    #all cords are added to the points list
    points.append(enter_point())

    #if the user types "N" or "n" it breaks the loop
    Continue=input("Do you want to continue (Y/N): ")
    if Continue=='N' or Continue=='n':
        break

#prints a line
print("-"*10)

#prints every tuple within the list one at a time using a for loop
for i in range(len(points)):
    print(points[i])

#runs the plotting function using the info that was added to the points list
plot_points(points)

