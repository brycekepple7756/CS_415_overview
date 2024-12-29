#
# Bryce Kepple
# Growth graphing lab
#
import matplotlib
import matplotlib.pyplot as plt


#creating x cords and empty lists
x_cord=[1,2,3,4,5,6,7,8,9,10]
doubled_list=[]
triple_list=[]
squared_list=[]

# fills the empty lists with correct numbers based off xcords
for i in x_cord:
    doubled_list.append(i*2)
for i in x_cord:
    triple_list.append(i*3)
for i in x_cord:
    squared_list.append(i**2)

#creates a figure that will hold our graphs
growth_graphs=plt.figure()

#creates the graph in the top left
#makes its Y axis go from 0-100, have a title and a purple dashed line
a=matplotlib.pyplot.subplot(2,2,1)
line1, =matplotlib.pyplot.plot(x_cord,x_cord,)
plt.ylim(0,100)
matplotlib.pyplot.setp(line1, color='m', linestyle='--')
a.set_title("Linear Growth")

#creates the graph in the top right
#makes its Y axis go from 0-100, have a title and a purple dashed line
b=matplotlib.pyplot.subplot(2,2,2)
line2, =matplotlib.pyplot.plot(x_cord,doubled_list)
plt.ylim(0,100)
matplotlib.pyplot.setp(line2, color='m', linestyle='--')
b.set_title(" 2x Growth")

#creates the graph in the bottom left
#makes its Y axis go from 0-100, have a title and a purple dashed line
c=matplotlib.pyplot.subplot(2,2,3)
line3, =matplotlib.pyplot.plot(x_cord,triple_list)
plt.ylim(0,100)
matplotlib.pyplot.setp(line3, color='m', linestyle='--')
c.set_title(" 3x Growth")


#creates the graph in the bottom right
#makes its Y axis go from 0-100, have a title and a purple dashed line
d=matplotlib.pyplot.subplot(2,2,4)
line4, =matplotlib.pyplot.plot(x_cord,squared_list)
plt.ylim(0,100)
matplotlib.pyplot.setp(line4, color='m', linestyle='--')
d.set_title(" Exponential Growth")

#names the entire figure
growth_graphs.suptitle("Growth Comparison")

#shows the graphs
matplotlib.pyplot.show()




