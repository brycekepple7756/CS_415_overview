# Jason Reeves
# Matplotlib Graphing Function for Tuple Lab

import matplotlib.pyplot


# Plot the provided list of points in Matplotlib.
def plot_points(points):
    # Grab the axes to set the graph's title
    axes = matplotlib.pyplot.subplot(1, 1, 1)
    axes.set_title("Tuple Lab Data")

    # Plot each point individually
    for point in points:
        matplotlib.pyplot.plot(point[0], point[1], point[2] + "x")

    # Display the completed graph
    matplotlib.pyplot.show()
