#
# Bryce Kepple
# Fraud triangle
#

# steps
# first take all 3 files and parse through them

# create a list of dictionaries for each data files (user, purchase, shipping)

# user dictionaries contain
# time stamp-date
# CC - string
# market_account - string
# product_desc - string
# cost - float
# shipping_address - string
# cc_billing_address - string

# purchase dictionaries contain
# time stamp-date
# CC - string
# product_desc - string
# cost - float
# cc_billing_address - string
# product_purchase_number - string

# shipping dictionaries contain
# time stamp-date
# cost - float
# shipping_address - string
# product_purchase_number - string


# rules for detecting fraud
# the order is, user orders, the scammer purchases, the object is shipped
# the time delta between the user ordering and the scammer will be at most 2 mins
# the time between the scammer and the shipper will be at most 1 day
# the user credit card will not be the same as the scammers
# the user and scammer product description will be the same
# the cost for the scammers and shippers will be the same but the users and scammers may not be the same
# the shipping address will be the same for the shipper and user
# the product purchase number for the scammer and shipper will be the same


#plan for program to detect fraud
# group all dictionarys between the user and orderer that have the same product description add them to a list and then add that list to a bigger list
# organize every list by the time delta and group all the possible orderers that could have committed fraud
# eliminate all that could not have

from datetime import datetime
from datetime import timedelta
from idlelib.editor import keynames

#gets the files from the user
def get_files():
    user_file=input("Enter the user file name: ")
    purchase_file=input("Enter the purchase file name: ")
    shipper_file=input("Enter the shipper file name: ")
    files = (user_file, purchase_file, shipper_file)
    return files

#reads the user data and turns it into a list of dictionaries
def read_user_data(file):
    user_data=[]
    file_fields=["timestamp","cc","market_account","product_desc","cost","shipping_address","cc_billing_address"]
    with open(file, "r") as f:
        for line in f:
            line=line.strip()
            fields=line.split("|")
            dictionary = {}
            for i, key in enumerate(file_fields):
                if key in ["timestamp"]:
                    try:
                        val = datetime.strptime(fields[i], '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        continue
                else:
                    val = fields[i]
                dictionary[key] = val
            user_data.append(dictionary)
        user_data.pop(0)
        return user_data

#reads the purchase data and turns it into a list of dictionaries
def read_purchase_data(file):
    purchase_data = []
    file_fields = ["timestamp", "cc","product_desc","product_purchase_number","cost","cc_billing_address"]
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            fields = line.split("|")
            dictionary = {}
            for i, key in enumerate(file_fields):
                if key in ["timestamp"]:
                    try:
                        val = datetime.strptime(fields[i], '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        continue
                else:
                    val = fields[i]
                dictionary[key] = val
            purchase_data.append(dictionary)
        purchase_data.pop(0)
        return purchase_data

#reads the shipper data and turns it into a list of dictionaries
def read_shipper_data(file):
    shipper_data = []
    file_fields = ["timestamp", "cost","product_purchase_number","shipping_address"]
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            fields = line.split("|")
            dictionary = {}
            for i, key in enumerate(file_fields):
                if key in ["timestamp"]:
                    try:
                        val = datetime.strptime(fields[i], '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        continue
                else:
                    val = fields[i]

                dictionary[key] = val
            shipper_data.append(dictionary)
        shipper_data.pop(0)
        return shipper_data
#sorts the user data and purchase data into groups based off of the product description
def sort_by_product(user_data, purchase_data):
    groups=[]
    for item in user_data:
        new_group_needed=True
        for group in groups:
            if item["product_desc"] in group[0][1]["product_desc"]:
                group.append(("user",item))
                new_group_needed=False
        if new_group_needed:
            groups.append([("user",item)])

    for item in purchase_data:
        for group in groups:
            if item["product_desc"] in group[0][1]["product_desc"]:
                group.append(("purchase",item))

    return groups


#goes through the groups and makes pairs of user and purchase that fit the critera for fraud
def find_possible_user_purchase_pairs(product_groups):
    possible_user_purchase_pairs = []
    for group in product_groups:
        for item_user in group:
            if item_user[0] == "user":
                for item_purchase in group:
                    if item_purchase[0] == "purchase":
                        if item_purchase[1]["cc"] != item_user[1]["cc"]:
                            if item_purchase[1]["timestamp"] - item_user[1]["timestamp"] < timedelta(minutes=2):
                                possible_user_purchase_pairs.append([item_user[1],item_purchase[1]])
    return possible_user_purchase_pairs


# goes through the pairs and finds any shipping that matches
def find_fraud(pairs,shipper_data):
    fraud=[]
    for pair in pairs:
        for shipment in shipper_data:
            if pair[1]["product_purchase_number"] == shipment["product_purchase_number"]:
                user_addy=pair[0]["shipping_address"].replace(" ","")
                shipment_addy=shipment["shipping_address"].replace(" ","")
                split_user_addy=user_addy.split(",")
                if split_user_addy[3][0] == "0":
                    split_user_addy[3]=split_user_addy[3][1:]
                split_shipment_addy = shipment_addy.split(",")
                if split_shipment_addy[3][0] == "0":
                    split_shipment_addy[3]=split_shipment_addy[3][1:]
                if split_user_addy == split_shipment_addy:
                    if pair[1]["cost"] == shipment["cost"]:
                        fraud.append((pair[0],pair[1],shipment))

    return fraud

                    

    # will check each pair for a possible shipper match
    # matches will have the same price, and product number as the purchaser
    # matches will have the same address as the user
    # maybe search list and use if statements
    # returns list of tuples of the that have the user fraudster and shipper

# prints out the fraud
def print_fraud(fraud_tuples):
    fraudsters={}
    for fraud_tuple in fraud_tuples:
        scammed_money=float(fraud_tuple[1]["cost"])
        market_name=fraud_tuple[0]["market_account"]
        if market_name in fraudsters.keys():
            fraudsters[market_name]=[fraudsters[market_name][0]+1,fraudsters[market_name][1]+scammed_money]


        else:
            fraudsters.update({market_name:[1,scammed_money]})

    for keys in fraudsters.keys():
        print(f'account: {keys} fraud incidents:{fraudsters[keys][0]} fraud total cost ${fraudsters[keys][1] :.2f}')

    for x in range(4):
        print()

    print("individual fraud triples")
    print("------------------------")

    for fraud_tuple in fraud_tuples:
        print(f'UserTx     :  timestamp: {fraud_tuple[0]["timestamp"]}  cc: {fraud_tuple[0]["cc"]:<18s}market_account: {fraud_tuple[0]["market_account"]:<21s}product_desc: {fraud_tuple[0]["product_desc"]:<27s}cost: ${float(fraud_tuple[0]["cost"]):<10.2f}shipping_address: {fraud_tuple[0]["shipping_address"]:<44s}cc_billing_address: {fraud_tuple[0]["cc_billing_address"]:<55s}product_purchase_number:                                     ')
        print(f'PurchaseTx :  timestamp: {fraud_tuple[1]["timestamp"]}  cc: {fraud_tuple[1]["cc"]:<18s}market_account: {"":<21s}product_desc: {fraud_tuple[1]["product_desc"]:<27s}cost: ${float(fraud_tuple[1]["cost"]):<10.2f}shipping_address: {"":<44s}cc_billing_address: {fraud_tuple[1]["cc_billing_address"]:<55s}product_purchase_number: {fraud_tuple[1]["product_purchase_number"]}')
        print(f'ShipmentTx :  timestamp: {fraud_tuple[2]["timestamp"]}  cc: {"":<18s}market_account: {"":<21s}product_desc: {"":<27s}cost: {" ":<11s}shipping_address: {fraud_tuple[2]["shipping_address"]:<44s}cc_billing_address: {"":<55s}product_purchase_number: {fraud_tuple[2]["product_purchase_number"]}')
        print()

def main():
    files = get_files()
    user_file=read_user_data(files[0])
    purchase_file=read_purchase_data(files[1])
    shipper_file=read_shipper_data(files[2])
    sorted_products=sort_by_product(user_file,purchase_file)
    possible_pairs=find_possible_user_purchase_pairs(sorted_products)
    detected_fraud=find_fraud(possible_pairs,shipper_file)
    print_fraud(detected_fraud)






if __name__ == '__main__':
    main()
