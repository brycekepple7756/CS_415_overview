#
#Bryce Kepple
#Menu Lab
#
#defining the addition function so it will add and show the user answer with work
def function_A(x,y):
    total=x+y
    print(x,"+",y,"=",total)

#defining the subtraction function so it will minus and show the user answer with work
def function_S(x,y):
    total=x-y
    print(x, "-", y, "=", total)

#setting the variable program to yes and making a loop that repeats forever while the program is = to yes
Program="yes"
while Program == "yes":

    #prompts the user to enter two numbers
    numb1=int(input("Please enter X and Y: \n"))
    numb2 = int(input())
    command=input("Enter command: \n")

    #if the user types A or S it runs the matching function and then the loop starts over
    if command == "A":
        function_A(numb1,numb2)
    elif command == "S":
        function_S(numb1,numb2)

    #if the user types Q it prints goodbye before setting the program to no which ends the loop
    elif command == "Q":
        print("Goodbye")
        Program = "NO"

    #anything else that is typed gives an error message and has the loop restart
    else:
        print("Invalid command")
