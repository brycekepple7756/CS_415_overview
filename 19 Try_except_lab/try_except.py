#
# Bryce Kepple
# Try Except Lab
#



def build_number_list():

    #makes a list an empty list where numbers are typed until DONE is typed
    num_list=[]
    while True:
        x=input("Enter a number: ")

        #prints list and breaks the loop
        if x=="DONE":
            print(num_list)
            break
        else:

            #tells program to try and add the input as an int
            try:
                num_list.append(int(x))

            #if its not an int then it trys as a float
            except ValueError:
                try:
                    num_list.append(float(x))

                #if its neither it prints out an error message
                except ValueError:
                    print("ERROR: Non-numeric input provided")


def raising_arizona(string):

    #if the string parameter is any form of arizona it will cause an error
    if string.lower()=="arizona":
        raise ValueError("There is no Arizona")
    return string



if __name__ == '__main__':
    build_number_list()
    print(raising_arizona("New Mexico"))
    print(raising_arizona("arizonA"))


