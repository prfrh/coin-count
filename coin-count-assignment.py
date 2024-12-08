import os

#Coin types and the weight per gram
coin_values = {
    '1p': 0.01,
    '2p': 0.02,
    '5p': 0.05,
    '10p': 0.10,
    '20p': 0.20,
    '50p': 0.50,
    '£1': 1.00,
    '£2': 2.00
}

#a dictionary to store volunteers data
volunteers = []

#a function to load the data from the coin count.txt file
def load_data():
    if os.path.exists('CoinCount.txt'):
        with open("coincount.txt", "r") as file:
            for line in file:
                name, bags_checked, bags_correct, total_value = line.strip().split(',')
                volunteers[name] = {
                    'bags_checked': int(bags_checked),
                    'bags_correct': int(bags_correct),
                    'total_value': float(total_value)
                }

# Function to save data to CoinCount.txt file
def save_data():
    with open('CoinCountmock.txt', 'w') as file:
        for name, data in volunteers.items():
            file.write(f"{name},{data['bags_checked']},{data['bags_correct']},{data['total_value']}\n")

def get_name():
    flag = True
    while flag:
        name = input ('Please enter your name: ')
        if name is int:
            print("The name entered did not match expected format. Please try again")
            flag = True
        else:
            flag = False
    return name


def bags_checked():
    flag = True
    while flag:
        bags_check = input('Please enter the number of bags checked: ')
        if bags_check is not int:
            print("The value entered did not match expected format. Please try again")
            flag = True
        else:
            flag = True
    return bags_check


def bags_value():
    flag = True
    while flag:
        bag_value = input('Please enter the value of the bag: ')
        if bag_value is not int:
            print("The value entered did not match expected format. Please try again")
            flag = True
        else:
            flag = True
    return bag_value


def type_of_coin():
    flag = True
    while flag:
        coin = input('Please enter the coin: ')
        if coin != 0.01 or 0.02 or 0.05 or 0.1 or 0.2 or 0.5 or 1.0 or 2.0:
            print ("Error, invalid coin")
        else:
            flag = True

    return coin


def weight_of_bag():
    flag = True 
    while flag:
        bags_weight = input("Enter the weight for the bag.")
        if bags_weight is not int:
            print("The value entered did not match expected format. Please try again")
            flag = True
        else:
            flag = True

    return bags_weight


