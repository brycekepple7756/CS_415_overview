#
# Bryce Kepple
# Scope lab
#

#sets the stack to only contain one empty dictionary and sets the current scope we are in to 0
stack=[{}]
scope=0

#lists out all the commands
print("Welcome to the scope simulator. Available commands are:")
print("\tquit\t- exit the simulator")
print("\tset \t- set a variable in the current scope")
print("\tget \t- get a variable from the current scope")
print("\tenter\t- enter  a new scope")
print("\texit\t- exit the current scope")
print("\tprint\t- print all the active scopes")

#tells us that there is one active scope
print()
print("Entered global scope. There are 1 active scopes")

#makes a loop that will go on until broken
while True:

    #gets the users input for a command
    command= input("enter command>")


    if command == "set":

        #if the user types set they will be prompted to input a variable name and value that they wanna add
        variable_name=input("enter variable name>")
        variable_value=input("enter variable value>")

        #updates the dictionary that represents our current scope with the values the user inputted above
        stack[scope].update({variable_name:variable_value})


    elif command == "get":

        #the user inputs the variable they want to find
        search_variable=input("enter variable name>")

        #sets a variable telling us whether we found the variable to false
        var_found=False

        # uses a for loop that goes through our stack backwards
        for x in range(scope,-1,-1):

            #if the variable is found it prints out the value and sets var_found to true
            if search_variable in stack[x]:
                print("The value of","\'"+search_variable+"\'","is",stack[x][search_variable])
                var_found=True
                break

        #if the loop completes and the variable was not found it prints out that it is not defined
        if not var_found:
            print("Variable","\'"+search_variable+"\'","is not defined")


    elif command == "enter":

        #adds a new dictionary and increases our current scope by 1
        stack.append({})
        scope+=1

        #prints out how many scopes there are ( the plus one is there because we start at 0 for what scope we are in)
        print("Entering a new scope. There are",scope+1,"active scopes")



    elif command == "exit":

        #if the current scope us greater than zero we get rid of the scope we just left and move into the one before it
        if scope>0:
            stack.pop(scope)
            print("Exiting scope. There are", scope, "active scopes")
            scope-=1

        #if it is 0 then tell user we cant leave our main scope
        else:
            print("cannot exit global scope")


    elif command == "print":

        #uses a for loop that is backwards and prints all the dictionaries
        for x in range(scope,-1,-1):
            print(x,"\t",stack[x])


    elif command == "quit":

        #breaks the loop and says goodbye
        print("Quitting, goodbye")
        break


