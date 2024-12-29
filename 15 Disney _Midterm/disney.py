#
# Bryce Kepple
# Disney Ride queue simulator
#

#creates empty lists that will hold the two queues
disney_pass_line=[]
line=[]

#creates a function that adds a user
def add_user():
    user=input("Enter the name of the person joining the line: \n")
    return user







#loop prompts user to enter commands
while True:
    cmd=input("Enter an option (a, da, b, p, or q) :\n ")

    #adds a person to the normal line
    if cmd=="a":
        line.append(add_user())

    #adds a person to the Disney pass line
    elif cmd=="da":
        disney_pass_line.append(add_user())


    elif cmd=="p":

        #checks to see if the list is empty prints out no one is waiting if it is
        if disney_pass_line==[]:
            print("Disney Pass Queue: No one is waiting to board")

        #if the list isnt empty prints it out
        if len(disney_pass_line)>1:
            print("Disney Pass Queue:",disney_pass_line)

        #does the same as above but with the normal line
        if len(line)==0:
            print("Regular Queue    : No one is waiting to board")
        if len(line)>0:
            print("Regular Queue    :",line)

    elif cmd=="b":
        #creates an empty list which represents the cart
        cart=[]

        #loops 5 times
        for i in range(0,5):

            #if the disney pass line isnt empty it grabs next person in line
            if len(disney_pass_line)>0:
                print("adding person",disney_pass_line[0],"from Disney queue")
                cart.append(disney_pass_line[0])
                disney_pass_line.pop(0)

            #if disney pass line is empty and normal line isnt then it grabs next person from normal line
            elif len(line)>0:
                print("adding person",line[0],"from regular queue")
                cart.append(line[0])
                line.pop(0)

            #if both lines empty breaks loop
            else:
                break

        #prints out results
        print("these people where dequeued and boarded the ride:",cart)
        print("disney pass queue:",disney_pass_line)
        print("Regular queue    :",line)












    #prints out queue status and ends program
    elif cmd=="q":
        if disney_pass_line==[]:
            print("Disney Pass Queue: No one is waiting to board")
        if len(disney_pass_line)>1:
            print("Disney Pass Queue:",disney_pass_line)
        if len(line)==0:
            print("Regular Queue    : No one is waiting to board")
        if len(line)>0:
            print("Regular Queue    :",line)

        print("goodbye")
        break

    #if wrong command is typed prompts user to try again
    else:
        print("Invalid command. Please enter \'a\', \'da\', \'b\', \'p\', or \'q\'")