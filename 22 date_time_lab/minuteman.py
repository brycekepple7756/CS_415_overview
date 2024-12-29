#
# Bryce Kepple
# Datetime Lab
#

from datetime import datetime
from datetime import timedelta

def read_lending_data(filename):

    #opens file
    with open(filename, 'r') as f:

        #creates list that will be returned
        lending_data = []
        lines=f.readlines()

        #goes through each line, gets rid of the \n, splits the data
        # then makes a dictionary for each key and puts a value
        # then adds each dictionary for each line
        for line in lines:
            line=line[:-1]
            data = line.split(',')
            new_row = {}
            fields = ['book_id','user_id','checkout','checkin']
            for i, field in enumerate(fields):
                new_row[field] = data[i]
            lending_data.append(new_row)

        #makes each time in the data a datetime object
        for line in lending_data:
            line['checkout']=datetime.strptime(line['checkout'],'%Y-%m-%d %H:%M:%S')
            line['checkin']=datetime.strptime(line['checkin'], '%Y-%m-%d %H:%M:%S')
        return lending_data



#used for testing
def report_dummy_data():
    analyzed_data = [
        ('Rich Dad Poor Dad',timedelta(days=100.5)),
        ('Becoming', timedelta(days=200.133)),
        ('Dreams From My Father', timedelta(days=193.21)),
        ('Just for the Summer', timedelta(days=88)),
        ('The Women', timedelta(days=300.12)),
        ('Foundation', timedelta(days=57.125)),
        ('Iron Flame', timedelta(days=75.3)),
        ('Fourth Wing', timedelta(days=174.2)),
        ('Table for Two', timedelta(days=85.5)),
        ('The Anxious Generation', timedelta(days=56.113)),
    ]
    return analyzed_data


def analyze_lending(lending_data):
    #return report_dummy_data()

    #creates an empty dictonary which holds the book name and time delta representing the time checked out
    book_times={}
    for entry in lending_data:
        time_checked_out=entry['checkin']-entry['checkout']

        #if the book is not already in the dictionary adds it to it
        if entry['book_id'] not in book_times:
            book_times.update({entry['book_id']: time_checked_out})

        #if it is adds that time to the dictionary
        else:
            book_times[entry['book_id']]+=time_checked_out
    analyzed_data = []

    #puts the dictionaries into tuples
    for key in book_times:
        temp_tuple=(key,book_times[key])
        analyzed_data.append(temp_tuple)
    return analyzed_data



def helper(tuple):
    return tuple[1]

def print_lending_report(books):
    # creates a temp list of data takes the max value of the datetime delta and prints it then removes that from the temp list while looping 5 times so it prints top 5 books
    print("Top Books by Total Days Checked Out:")
    temp_list=books
    for i in range(0,5):
        temp_book=max(temp_list,key=helper)
        temp_days=temp_book[1].days
        temp_seconds=temp_book[1].seconds
        print(f'{i+1}{"." :<15s}{temp_book[0]} {temp_days+temp_seconds/86400:.2f}')
        temp_list.remove(temp_book)





#runs functions in correct order
def main():
    lending_data = read_lending_data("lending_data.csv")
    analyzed_data = analyze_lending(lending_data)
    print_lending_report(analyzed_data)





if __name__ == "__main__":
     main()
