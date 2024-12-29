#
#Bryce Kepple
# List Loop
#

#import stats and random functions
import random
import statistics

# creating variables that will be used as global variables later on
min_list= 0
max_list=0
average_list=0





def list_stats(array):
    #setting the following variables as global to be used throughout the function
    global min_list
    global max_list
    global average_list

    #if the list is empty sets the values to none
    if array == '':
        min_list=None
        max_list=None
        average_list=None
        return

    # sets the values to the first number in the list
    min_list = array[0]
    max_list = array[0]
    #sets the x and sum to 0 so the while loop can run amd the sum can be added
    x=0
    sum_list=0

    while x <50:
        #used for getting the sum of all numbers in the list
        sum_list+=array[x]

        #goes down the list and replaces that number if the next number is bigger or smaller than the min or max
        if min_list > array[x]:
            min_list = array[x]
        if max_list < array[x]:
            max_list = array[x]

        #used so the loop will go 50 times
        x=x+1

    #finds the average number in the list and then returns the min max and avg
    average_list = sum_list / len(array)
    return min_list, max_list, average_list

def check_work(array):
    # used to make sure that the function we made matches the function imported
    check_min= min(array)
    check_max= max(array)
    check_avg= statistics.mean(array)
    return check_min, check_max, check_avg




#creating variables for later
numbers=[]
n=0


while n<50:
    #creates a list that adds 50 random numbers 1-100 by looping
    number=random.randint(1,100)
    numbers.append(number)

    #used to make the loop end after 50
    n+=1

# calls the list stats function and makes sure a valid list was created
list_stats(numbers)
if min_list==None or max_list==None or average_list==None:
    print("ERROR: empty list provided ")
else:
    # checks the work using the function then prints out the values from the first function
    check_work(numbers)
    print("Minimum value in array: ", min_list)
    print("Maximum value in array: ", max_list)
    print("Average value in array: ", average_list)

    # if the work matches it tells the user that all the work matches
    if check_work(numbers)==list_stats(numbers):
        print("all values match")
