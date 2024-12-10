import os


# Coin weight and the values
coin_weight = {
    "1p": 3.56,
    "2p": 7.12,
    "5p": 2.35,
    "10p": 6.5,
    "20p": 5.0,
    "50p": 8.0,
    "£1": 8.75,
    "£2": 12.00
}

coin_values = {
    "1p": 0.01,
    "2p": 0.02,
    "5p": 0.05,
    "10p": 0.10,
    "20p": 0.20,
    "50p": 0.50,
    "£1": 1.00,
    "£2": 2.00,
}


# A dictionary to store volunteers data
volunteers = []

# A function to load the data from the coin count.txt file
def load_data():
    if os.path.exists("CoinCount.txt"):
        with open("coincount.txt", "r") as file:
            for line in file:
                name, bags_checked, bags_correct, total_value = line.strip().split(",")
                volunteers[name] = {
                    "bags_checked": int(bags_checked),
                    "bags_correct": int(bags_correct),
                    "total_value": float(total_value),
                }


# Function to save data to CoinCount.txt file
def save_data():
    with open("CoinCountmock.txt", "w") as file:
        for name, data in volunteers.items():
            file.write(f"{name},{data['bags_checked']},{data['bags_correct']},{data['total_value']}")
            # need to ask joe or joel why it needs '' and doesnt accept ""


# Function for the volunteers name
def get_name():
    while True:
        name = input ("Please enter your name: ")
        if name.isdigit():
            print("The name entered did not match expected format. Please try again")
        else:
            return name


# Function to input, add or remove coins to correct the weight of the bag
def correct_weight(coin_type, said_weight, bag_weight):
    weight = coin_weight[coin_type]
    flag = True
    while True:
        if said_weight == bag_weight:
            return 0 #correction not needed
        else:
            difference = bag_weight - said_weight
            coins_needed = int(difference) / int(coin_weight)
            if difference > 0:
                return coins_needed # add coins
            else: 
                return -coins_needed # minus coins


# Function to see how accuracte the volenteer is
def check_accuracy(name):
    if name in volunteers:
        total_bags = volunteers[name]["bags_checked"]
        bags_correct = volunteers[name]["correct_bags"] 
        if total_bags > 0:
            accuracy = int((bags_correct / total_bags) * 100)
            return accuracy
    return 0


# Menu for the volenteer to interact with
def main_menu():
    load_data()

    while True:
        print("--- Coin Counting Program ---")
        print("1. add or correct coin count")
        print("2. display the total bags checked and total value")
        print("3. display the volunteers sorted by accuracy")
        print("4. EXIT PROGRAM")

        decision = input("enter you decision: ")
        if decision == "1":
            name = get_name()
            while True:
                coin = input("Please enter the coin (1p, 2p, 5p, 10p, 20p, 50p, £1, £2): ")
                if coin not in coin_weight:
                    print ("Error, invalid coin")
                else:
                    break
                    
                while True:    
                    try:
                        said_weight = int(input("Enter the said weight of the bag in grams: "))
                        break
                    except ValueError:
                        print("The number entered did not match expected format. Please try again")

                while True:
                    try:
                        bag_weight = int(input("Enter the weight of the bag to check in grams: "))
                        break
                    except ValueError:
                        print("The number entered did not match expected format. Please try again")
            

                coins_to_correct = correct_weight(coin, said_weight, bag_weight)

                # Update volunteer's data
                if name not in volunteers:
                    volunteers[name] = {"bags_checked" : 0, "bags_correct": 0, "total_value": 0}

                volunteers[name]["bags_checked"] += 1
                bag_value = bag_weight / coin_weight[coin] * coin_values[coin]
                volunteers[name]["total_value"] += bag_value

                if coins_to_correct == 0:
                    volunteers[name]["correct_bags"] += 1
                    print(f"Bag is accurate, no correction needed.")
                else:
                    print(f"Bag weight is incorrect, add/remove {int(coins_to_correct)} coins of {coin}.") 


        elif decision == "2":
            total_bags = sum(["bags_checked"] in volunteers.values())
            total_value = sum(["total_value"] in volunteers.values())
            print(f"Total bags checked: {total_bags}")
            print(f"Total value: £{total_value}")

        
        elif decision == "3":
            ordered_volunteers = sorted(volunteers.items(), key = lambda x: check_accuracy(x[0]), reverse=True )
            print("Volunteers sorted by accuracy:")
            for name, data in ordered_volunteers:
                accuracy = check_accuracy(name)
                print(f"{name}: {data['correct_bags']} out of {data['bags_checked']} bags, Accuracy: {accuracy}%")


        elif decision == "4":
            save_data()
            print("Data saved. Exiting the program.")
            break
        else:
            print("Error! Please select again.")



# Run the program
if __name__ == "__main__":
    main_menu()