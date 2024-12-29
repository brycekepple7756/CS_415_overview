#
#Bryce Kepple
#4 Conditionals Lab
#

#uses modulo division to determine if a number is odd or even (has a remainder after /2)
#then a conditional is used to determine what text to print based off being even or odd
def road_direction(interstate_number):
    if interstate_number%2 == 1:
        print("primary north-south")
    else:
        print("primary east-west")


#sets interstate number to a string to use index to pick certain number
#turns number back into an int to do modulo division and see if even or odd
#prints out text based off even or odd and I + the last numbers
def belt_or_spur(interstate_number):
    first_number=str(interstate_number)[0]
    last_numbers=str(interstate_number)[1:3]
    if int(first_number)%2 == 1:
        print("spur for I-"+last_numbers)
    else:
        print("beltway for I-" + last_numbers)




#gets input that will be used for functions
interstate_number=int(input("Enter an interstate highway integer: "))

#makes sure number is a valid 1-3 digit number
if 0<=interstate_number<=999:
    #checks if a number has 3 digits or less and runs the designated functions from above accordingly
    if interstate_number<100:
        road_direction(interstate_number)
    else:
        belt_or_spur(interstate_number)

else:
    print("invalid")

