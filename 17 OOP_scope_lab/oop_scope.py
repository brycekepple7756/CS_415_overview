#
# Bryce Kepple
# Scope lab
#


from Stack import Stack

#sets stack as an object from the stack class
stack=Stack()

#intro
print("Welcome to the scope simulator. Available commands are:")
print("\tquit\t- exit the simulator")
print("\tset \t- set a variable in the current scope")
print("\tget \t- get a variable from the current scope")
print("\tenter\t- enter  a new scope")
print("\texit\t- exit the current scope")
print("\tprint\t- print all the active scopes")
print()

#gives us starting scope
print("Entered global scope. There are 1 active scopes")

#starts a loop where commands can constantly be imputed
while True:
    command= input("enter command>")

    if command == "set":
        var=input("enter variable name>")
        val=input("enter value>")

        #adds the variable and value from above to the scope at the end of the list
        stack.top().update({var:val})



    elif command == "get":
        search_var=input("enter variable name that you want to search>")
        found=False

        #searches the stack backwards for the first occasion of the variable and marks it as found
        for i in reversed(range(len(stack))):
            if search_var in stack[i]:
                print("the variable",search_var,"is",stack[i][search_var])
                found=True
                break

        #if its not marked as found informs the user
        if not found:
            print("The variable is not defined")


    elif command == "enter":

        #adds a scope to the end of the stack and informs user how many scopes there are
        stack.push({})
        print("Entering a new scope. There are",stack.__len__(),"active scopes")



    elif command == "exit":

        #removes last scope and inform the user
        stack.pop()
        print("there are currently",stack.__len__(),"active scopes")



    elif command == "print":

        #goes through the list and prints out each dictionary
        for i, key in enumerate(stack):

            #used to print the scope we are currently on
            print(stack.__len__()-i-1,key)



    elif command == "quit":

        #breaks the loop and says goodbye
        print("Quitting, goodbye")
        break


