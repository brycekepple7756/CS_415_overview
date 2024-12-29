#
# Bookworm starter file.
# Written by Craig Smith
#
#

from datetime import datetime



def print_bookworms(bookworm_data,max_books):

    #takes a list of tuples in each tuple there is a person and the max amount of books they had checkout at once
    # sorts the list of tuples from highest to lowest based off the amount of books
    # prints out the max amount of books lent out at once and then prints the rankings of the bookworms highest to lowest
    print("max overall lent:",max_books)
    print("Bookworms:")
    bookworm_data.sort(key=lambda x: x[1], reverse=True)
    num=0
    print(f'{"Rank":<4s}{"Patron":>25s}{"Count":^10s}')
    for bookworm in bookworm_data:
        num+=1
        print(f'{num:<4d}{bookworm[0]:>25s}{bookworm[1]:^10d}')



def convert_to_events(data):
    # goes through each row in the data and breaks the check out and check in times into 2 separate events
    events=[]
    for row in data:
        start_event={'type':"start",'patron_id':row['patron_id'],'book_id':row['book_id'],'time':row['start']}
        events.append(start_event)
        end_event={'type':"end",'patron_id':row['patron_id'],'book_id':row['book_id'],'time':row['end']}
        events.append(end_event)

    return events



def separate_by_patron(events):
    #creates a dictionary where every user is a key and there value is a list of tuples that contain whether the checkout is a start or end
    # and the time that the event took place
    patrons={}
    for event in events:
        if event['patron_id'] in patrons:
            patrons[event['patron_id']].append((event['type'],event['time']))
        else:
            patrons.update({event['patron_id']: [(event['type'],event['time'])]})

    # sorts the list of tuples for each user by chronological order and then returns that dictionary
    for patron in patrons:
        patrons[patron].sort(key=lambda x: x[1])

    return patrons





def find_bookworms(sorted_patrons):
    #goes through each patron in the dictionary and sets the bookworm count to 0 and the peak count to 0
    patrons_data=[]
    for key in sorted_patrons:
        bookworm_count=0
        peak_count=0

        #goes through each item for that patron and adds one to the bookworm count if the item is a start and minus one if it is an end
        # each time it goes through an item the peak count is updated if the bookworm count is larger
        for item in sorted_patrons[key]:
            if item[0]=="start":
                bookworm_count+=1
            elif item[0]=="end":
                bookworm_count-=1
            if bookworm_count>peak_count:
                peak_count=bookworm_count
        #after going through all the items a tuple is made of
        patrons_data.append((key,peak_count))
    return patrons_data

def find_max_books(events):

    #sets the max books and books to 0
    max_books=0
    books=0

    # sorts the events based off of the time and then goes through those times and adds 1 if the type is start and subtracts it if its type is end
    # after that if the max books is smaller then the books it updates the max book count
    events.sort(key=lambda x: x['time'])
    for event in events:
        if event['type']=="start":
            books+=1
        elif event['type']=="end":
            books-=1
        if books>max_books:
            max_books=books
    return max_books





FILE_FIELDS = ['book_id', 'patron_id', 'start', 'end']

def read_lending_data(file):
    """
    :param file: the name of CSV lending data to read in.
    :return: A list of dictionaries where the keys are field names and the values are the values for that row in the file.
    See the list FILE_FIELDS
    """
    lending_data = []
    with open(file, 'r') as fh:
        for line in fh:
            line = line.strip()
            if len(line) == 0 or line.startswith('#'):
                continue

            fields = line.split(',')
            lent = {}
            for i, key in enumerate(FILE_FIELDS):
                if key in ['start', 'end']:
                    val = datetime.strptime(fields[i],'%m/%d/%Y %H:%M')
                else:
                    val = fields[i]
                lent[key] = val
            lending_data.append(lent)
        fh.close()
        return lending_data


def main():

    # asks the user for a file and sets default as lendind data
    default_lending_file = 'lending_data.csv'
    lending_file = input(f"enter lending data CSV file [{default_lending_file}] > ") or default_lending_file

    #reads the data converts it to events and then separates the events by patron, after that it finds the max books
    # uses the separated events to find the bookworm data and then finally prints the bookworm data
    lending_data = read_lending_data(lending_file)
    events = convert_to_events(lending_data)
    separated_events = separate_by_patron(events)
    max_books = find_max_books(events)
    bookworm_data=find_bookworms(separated_events)
    print_bookworms(bookworm_data,max_books)


#
if __name__ == "__main__":
    main()
