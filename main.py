
import random

                            #0                #1                #2                     #3                       #4
destination_list = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
                        #0            #1            #2                 #3              #4
restaurant_list = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
                                #0      #1      #2         #3           #4
mode_of_transportation_list = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
                        #0          #1          #2            #3              #4
things_to_do_list = ["Hiking", "Bicycling", "Dancing", "Singing Karaoke", "Swimming"]

my_day_trip_dictionary = {"1": "Galveston Island", 
"2": "Jacob's Well", "3": "Six Flags Fiesta", "4": "Dinosaur Valley State Park", "5": "Bracken Cave", 
"6": "Whataburger", "7": "Chili's", "8": "Texas Roadhouse","9": "Chick-Fil-A", "10": "Firehouse Subs",
"11":"bus", "12":"car", "13": "train", "14": "motorcycle", "15": "helicopter",
"16": "dancing", "17":"hiking", "18": "bicycling", "19": "singing Karaoke", "20": "swimming"}

def greeting():
    print("")
    print ("Thank you for choosing to use the Day Trip Generator!")
    print("")
    print("Let's get started:")
    print("")

def pick_destination(list):
    confirm_bool = True
    while confirm_bool == True:
        picked_destination = random.choice(destination_list)
        user_input = input(f"You will be traveling to {picked_destination}! Does that destination appeal to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{picked_destination} will be great!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False
 
def pick_restaurant(list):
    confirm_bool = True
    while confirm_bool == True:
        picked_restaurant = random.choice(restaurant_list)
        user_input = input(f"You will be eating at {picked_restaurant}! Does that restaurant sound good to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{picked_restaurant} will be awesome!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False 
def pick_mode_of_transportation(list):
    confirm_bool = True
    while confirm_bool == True:
        picked_mode_of_transportation = random.choice(mode_of_transportation_list)
        user_input = input(f"You will be traveling via {picked_mode_of_transportation}! Will that form of transportation work for you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"Traveling via {picked_mode_of_transportation} will be perfect!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False
def pick_things_to_do(list):
    confirm_bool = True
    while confirm_bool == True:
        picked_things_to_do = random.choice(things_to_do_list)
        user_input = input(f"You will be {picked_things_to_do}! Does that sound good to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{picked_things_to_do} will be a lot of fun!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False



greeting()
random_choice = pick_destination(list)
random_choice = pick_restaurant(list)
random_choice = pick_mode_of_transportation(list)
random_choice = pick_things_to_do(list)



