
import random


destination_list = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
restaurant_list = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
mode_of_transportation_list = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
things_to_do_list = ["Hiking", "Bicycling", "Dancing", "Singing Karaoke", "Swimming"]

my_day_trip_dictionary = {
"Destination": "pick_destination",
"Restaurant": "pick_restaurant", 
"Transportation": "pick_mode_of_transportation", 
"Entertainment": "pick_things_to_do"}

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
            my_day_trip_dictionary["Destination"] = pick_destination
            confirm_bool = False
        else: 
            print("Let's try again!")
            print("") 

def picked_restaurant(list):
    confirm_bool = True
    while confirm_bool == True:
        pick_restaurant = random.choice(list)
        user_input = input(f"You will be eating at {pick_restaurant}! Does that restaurant sound good to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{pick_restaurant} will be awesome!")
            print("")
            my_day_trip_dictionary["Restaurant"] = pick_restaurant
            confirm_bool = False
        else:
            print("Let's try again!")
            print("")

def picked_mode_of_transportation(list):
    confirm_bool = True
    while confirm_bool == True:
        pick_mode_of_transportation = random.choice(list)
        user_input = input(f"You will be traveling via {pick_mode_of_transportation}! Will that form of transportation work for you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"Traveling via {pick_mode_of_transportation} will be perfect!")
            print("")
            my_day_trip_dictionary["Transportation"] = pick_mode_of_transportation
            confirm_bool = False
        else:
            print("Let's try again!")
            print("")
            
def picked_things_to_do(list):
    confirm_bool = True
    while confirm_bool == True:
        pick_things_to_do = random.choice(list)
        user_input = input(f"You will be {pick_things_to_do}! Does that sound good to you? (y/n): ")
        print("")
        if user_input == "y":
            print(f"{pick_things_to_do} will be a lot of fun!")
            print("")
            my_day_trip_dictionary["Entertainment"] = pick_things_to_do
            confirm_bool = False
        else:
            print("Let's try again!")
            print("")
def confirmation():
    confirm_bool = True
    while confirm_bool == True:
        print(f"You will be traveling to {my_day_trip_dictionary['Destination']} via {my_day_trip_dictionary['Transportation']}, eating at {my_day_trip_dictionary['Restaurant']} and {my_day_trip_dictionary['Entertainment']}!")
        print("") 
        user_input = input("Are you satisfied with this day trip? (y/n)")
        if user_input == "y":
            print("")
            print("Have a wonderful time!")
            print("") 
            confirm_bool = False  
        else:
            print("Let's try again!")
            print("")
            
               
greeting()
picked_destination(destination_list)
picked_restaurant(restaurant_list)
picked_mode_of_transportation(mode_of_transportation_list)
picked_things_to_do(things_to_do_list)
confirmation()
 

