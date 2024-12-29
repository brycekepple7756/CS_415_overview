#
# Bryce Kepple
# 11 Dictionary Lab
#


#defines a function that checks to make sure a given plate is valid
def validate_nh_license_plate(plate):

    #makes sure the plate has a length of 7
    if len(plate) == 7:

        #makes sure the plate only has digits
        if plate.isdigit():

            #returns true if it passes both test and returns false if it fails either
            return True
        else:
            return False
    else:
        return False

#defines a function that will be used for adding info to a dictionary
def enter_record():

    #puts the user into a loop
    correct_plate_entered = False
    while not correct_plate_entered:

        #prompts the user to enter a license plate
        license_plate = input("Enter the vehicle plate number. ")

        #if the plate is valid it breaks the loop and ask the user for more info
        if validate_nh_license_plate(license_plate):
            correct_plate_entered = True
            name = input("Enter a name: ")
            address=input("Enter a street address: ")

            #returns the data entered as a tuple
            data= (license_plate, name, address)
            return data

        #if it isn't it tells the user to try again and sends them back through the loop
        else:
            print("Invalid plate number entered. Please enter a valid 7-digit plate number.")

#defines a function that adds the info that was added to the dictionary
def insert_record(record_tuple, plate_dictionary):

    #separates the data and adds the plate as the key in the dictionary
    # then adds the name and address as a tuple in as the value in the dictionary
    add_name=record_tuple[1:3]
    plate= record_tuple[0]
    plate_dictionary.update({plate:add_name})

#defines a function that checks the dictionary to see if there is a plate in the dictionary
def lookup_record(plate, plate_dictionary):

    #if there is a plate that returns the value of the key
    if plate in plate_dictionary:
        return plate_dictionary[plate]

    #if there isn't it returns nothing
    else:
        return None

#creating the empty dictionary
plate_db={}



#creates a loop where the user can type in commands until they type in quit command
quit=False
print("Welcome to the Department of Motor Vehicles!")
while not quit:
    command=input("Enter a command. ")

    #if the user types an "a" they run through the enter record function and then the value returned from that
    #is put into the insert function which will insert the data into the dictionary
    if command == "a":
        insert_record(enter_record(), plate_db)

    #when the user types "s" they are put in a loop that they cant leave until they type a valid license plate
    elif command == "s":
        valid_plate= False
        while not valid_plate:
            plate=input("Enter the plate number to search for > ")
            validate_nh_license_plate(plate)

            #if the plate is valid it breaks the loop
            if validate_nh_license_plate(plate):
                valid_plate= True

                #it then runs the look-up function to see if there is a plate that matches
                if lookup_record(plate, plate_db) is not None:
                    print("Information for plate",plate+":")
                    #if there is a plate that matches it prints out the name and address
                    print("----Name:", plate_db[plate][0])
                    print("----Address:", plate_db[plate][1])

                #if there is no plate that matches it tells the user
                else:
                    print("No record of",plate,"exists")

            #tells the uer to try again after typing an invalid plate
            else:
                print("Invalid plate please enter a valid plate")


    #if the user types "p" it creates a tuple of all the keys
    elif command == "p":
        keys=(plate_db.keys())

        #then it runs a loop through each key, printing out the plate number, the name associated, and hen the address associated
        for key in keys:
            print("Information for plate",key)
            print("----Name:", plate_db[key][0])
            print("----Address:", plate_db[key][1])

    # if the q command is typed it changes the value of quit to true which breaks the loop
    elif command == "q":
        print("Goodbye")
        quit = True

    #if anything else is typed it tells user invalid command and loops back
    else:
        print("Invalid command")




