
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

def picked_destination(list):
    confirm_bool = True
    while confirm_bool == True:
        pick_destination = random.choice(list)
        user_input = input(f"You will be traveling to {pick_destination}! Does that destination appeal to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{pick_destination} will be great!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False
 
def picked_restaurant(list):
    confirm_bool = True
    while confirm_bool == True:
        pick_restaurant = random.choice(list)
        user_input = input(f"You will be eating at {pick_restaurant}! Does that restaurant sound good to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{pick_restaurant} will be awesome!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False 

def picked_mode_of_transportation(list):
    confirm_bool = True
    while confirm_bool == True:
        pick_mode_of_transportation = random.choice(list)
        user_input = input(f"You will be traveling via {pick_mode_of_transportation}! Will that form of transportation work for you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"Traveling via {pick_mode_of_transportation} will be perfect!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False

def picked_things_to_do(list):
    confirm_bool = True
    while confirm_bool == True:
        pick_things_to_do = random.choice(list)
        user_input = input(f"You will be {pick_things_to_do}! Does that sound good to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{pick_things_to_do} will be a lot of fun!")
            print("")
        if user_input == "n":
            print("Let's try again!")
            print("")
        else:
            confirm_bool = False
#Need to confirm that my day trip is "complete" once I like all of the random selections.
def confirmation():
    confirm = False
    while confirm == False:
        user_input = input(f"Does traveling to {picked_destination} via {picked_mode_of_transportation}, eating at {picked_restaurant} and {picked_things_to_do} sound like the perfect day trip? (y/n): ")
        print("")
    if user_input == "y":
        print(f"You have confirmed that you will be traveling to {picked_destination} via {picked_mode_of_transportation}, eating at {picked_restaurant} and {picked_things_to_do}! Have a great time on your day trip!")
        print("")
    if user_input == "n":
        print("What would you like to change?")
    else: 
        confirm = True

greeting()
picked_destination(destination_list)
picked_restaurant(restaurant_list)
picked_mode_of_transportation(mode_of_transportation_list)
picked_things_to_do(things_to_do_list)
confirmation()
 
#want to store my final day trip selections in a Dictionary, with a unique key value pair for each piece of my day trip.
# for key, value in my_day_trip_dictionary.items():
#     print(f"{key}: {value}")

