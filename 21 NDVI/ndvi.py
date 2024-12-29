#
# Bryce Kepple
# 21 NDVI program
#


import termplotlib as tpl
import numpy as np



def read_smoothed_ndvi_data(file):

    #creates an empty list that will hold our data
    data=[]

    #opens file
    with open(file,'r') as f:

        # sets breaks the text into lines
        lines=f.readlines()

        #goes through each line and sets fields equal to a split up list of the line
        for i in range(len(lines)):
            fields=lines[i].split(",")

            #if the 3rd thing is smoothed it adds the line as a list to the data
            if fields[2]=="smoothed":
                line_list=lines[i].split(",")
                data.append(line_list)
    return data


def main():

    #user chooses file
    file_choice=input("enter data filename [testdata.csv] > ")
    if not file_choice:
        file_choice="testdata.csv"

    # creates a tempory holder for the data
    temp = read_smoothed_ndvi_data(file_choice)

    #creates an empty list that will hold the data for the histogram
    histogram_data=[]

    # loops through each line and adds every item after the 3rd item as a float to the histogram data list
    for x in range(len(temp)):
        for i in range(3,len(temp[x])):
            histogram_data.append(float(temp[x][i]))

    #sets the counts and bin edges using the histogram function with the histogram data and manualy sets the bins
    counts,bin_edges=np.histogram(histogram_data, bins=[-1.00,0.00,0.10,0.15,0.30,0.60,0.80,1.00])
    fig = tpl.figure()

    #sets the barh to show the counts and intervals
    fig.barh(counts,["-1.00 - 0.00","0.00 - 0.10","0.10 - 0.15","0.15 - 0.30","0.30 - 0.60","0.60 - 0.80","0.80 - 1.00"])

    #shows the histogram
    fig.show()




if __name__ == "__main__":
    main()
