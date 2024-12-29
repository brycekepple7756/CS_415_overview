#
#Bryce Kepple
# Bubble Sort
#

#import random and punch timer functions from other file
import random
from punch_timer import punch_in
from punch_timer import punch_out
from punch_timer import punch_diff


#defining the function for the buble sort
def bubble_sort(array):
    #sets the length of the list = to n
    n = len(array)

    # has a loop as that goes through as many times as the length of the list
    for i in range(n):

        # makes another loop that goes from 0 to how many times as the length of the list minus what how many times
        # the loop above has already been run and minus 1
        for j in range(0, n - i - 1):

            #if the item is bigger then the item in front of it they swap places
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


#creates an empty list and puts however many numbers a user imputs into that list each number being from -100 to 100
numbers = []
number_length = int(input("Enter a number greater then 0 : "))
for i in range(number_length):
    numbers.append(random.randint(-100, 100))

#if the list is smaller than 20 items it prints the unsorted list
if number_length < 20:
    print("Unsorted list:", numbers)

#punches in the time before running the bubble sort and then punches out the time after
time1 = punch_in()
bubble_sort(numbers)
time2 = punch_out()

#if the list is smaller than 20 it prints out the sorted list
if number_length < 20:
    print("Sorted list:", numbers)

#prints out the time it took to sort the list using the time dif fucntion
print("This took", punch_diff(time1, time2), "nanoseconds")

# creates another empty list and fills it with however many numbers the user imputs each number being from -100 to 100
numbers2 = []
for i in range(number_length):
    numbers2.append(random.randint(-100, 100))

#if the length of the list is less then 20 print out the list
if number_length < 20:
    print("Unsorted list:", numbers2)

#punch in then use the built in sort function and then punch out
list2_time1 = punch_in()
numbers2.sort()
list2_time2 = punch_out()

#if the list is less then 20 print out the list
if number_length < 20:
    print("Sorted list:", numbers2)

#uses the diff function and prints out how long it took the built in function to sort a random list the same size
print("This took", punch_diff(list2_time1, list2_time2), "nanoseconds")


# Based off of the data from the graphs we are able to see that the bubblesort function that we wrote is much slower then
# the sort() function that is built into python. the bubblesort takes exponentially more time then the sort() function so in
# smaller list the difference isn't noticeable but in the larger list like the ones in the 1000s the difference is clear to the user.