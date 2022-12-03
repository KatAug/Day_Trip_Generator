
import random

destination_list = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
restaurant_list = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
mode_of_transportation_list = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
things_to_do_list = ["Hiking", "Bicycling", "Dancing", "Singing Karaoke", "Swimming"]

greeting = "Thank you for choosing to use the Day Trip Generator! Let's get started:"

print(greeting)

pick_destination = random.choice(destination_list)
my_destination = f"Your destination is {pick_destination}!"

def destination():
    print(my_destination)
destination()

user_input= input("Does this destination sound good to you?(Y/N)")
my_destination = f"Your destination is {pick_destination}!"

while user_input == ("N"):
    print("Let us try again!")
    pick_destination = random.choice(destination_list)
    print(f"Your destination is {pick_destination}!")
    user_input= input("Does this destination sound good to you?(Y/N)")
    if user_input == ("Y"):
        print(f"{pick_destination} is a great destination!")


pick_restaurant = random.choice(restaurant_list)
my_restaurant = f"You will dine at {pick_restaurant}!"

def restaurant():
    print(my_restaurant)
restaurant()

user_input= input("Does this restaurant sound good to you?(Y/N)")
my_restaurant = f"Your restaurant is {pick_restaurant}!"

while user_input == ("N"):
    print("Let us try again!")
    pick_restaurant = random.choice(restaurant_list)
    print(f"Your restaurant is {pick_restaurant}!")
    user_input= input("Does this restaurant sound good to you?")
    if user_input == ("Y"):
        print(f"{pick_restaurant} is a great place to eat!")


pick_mode_of_transportation = random.choice(mode_of_transportation_list)
my_transportation = f"You will arrive by {pick_mode_of_transportation}!"

def transportation():
    print(my_transportation)
transportation()

user_input= input("Does this mode of transportation sound good to you?(Y/N)")
my_transportation = f"Your mode of transportation is {pick_mode_of_transportation}!"

while user_input == ("N"):
    print("Let us try again!")
    pick_mode_of_transportation = random.choice(mode_of_transportation_list)
    print(f"Your mode of transportation is {pick_mode_of_transportation}!")
    user_input= input("Does this mode of transportation sound good to you?")
    if user_input == ("Y"):
        print(f"By {pick_mode_of_transportation} is a great way to travel!")

pick_things_to_do = random.choice(things_to_do_list)
my_things_to_do = f"You will be {pick_things_to_do}!"

def things_to_do():
    print(my_things_to_do)
things_to_do()

user_input = input("Does that sound good to you?(Y/N)")
my_things_to_do = f"You will be {pick_things_to_do}"

while user_input == ("N"):
    print("Let us try again!")
    pick_things_to_do = random.choice(things_to_do_list)
    print(f"You will be {pick_things_to_do}!")
    user_input= input("Does that sound good to you?(Y/N)")
    if user_input == ("Y"):
        print(f"{pick_things_to_do} will be a lot of fun!!")

user_input = input(f"Does traveling to {pick_destination} via {pick_mode_of_transportation}, eating at {pick_restaurant} and {pick_things_to_do} sound like the perfect day trip?(Y/N)")
my_day_trip_dictionary = {"destination":[destination_list], "restaurant": [restaurant_list], "transportation": [mode_of_transportation_list], "entertainment": [things_to_do_list]}

while user_input == "N":
    user_input = input(f"Which part would you like to change? {pick_destination}, {pick_restaurant}, {pick_mode_of_transportation}, or {pick_things_to_do}?")
    if user_input == pick_destination:
        pick_destination = random.choice(destination_list)
        print(f"Your new destination is {pick_destination}!")
        user_input= input("Does that sound good to you?(Y/N)")
        if user_input == "N":
            pick_destination = random.choice(destination_list)
            print(f"Your new destination is {pick_destination}!")
            user_input= input("Does the new destination sound good to you?(Y/N)")
    if user_input == pick_restaurant:
        pick_restaurant = random.choice(restaurant_list)
        print(f"Your new place to eat will be {pick_restaurant}!")
        user_input= input("Does that sound good to you?(Y/N)")
        if user_input == "N":
            pick_restaurant = random.choice(restaurant_list)
            print(f"Your new place to eat will be {pick_restaurant}!")
            user_input= input("Does this new place to eat sound good to you?(Y/N)")
    if user_input == pick_mode_of_transportation:
        pick_mode_of_transportation  = random.choice(mode_of_transportation_list)
        print(f"Your new mode of transportation will be {pick_mode_of_transportation}!")         
        user_input= input("Does that sound good to you?(Y/N)")
        if user_input == "N":
            pick_mode_of_transportation = random.choice(mode_of_transportation_list)
            print(f"Your new mode of transportation will be {pick_mode_of_transportation}!")
            user_input= input("Does that sound good to you?(Y/N)")
    if user_input == pick_things_to_do:
        pick_things_to_do = random.choice(things_to_do_list)
        print(f"You will be {pick_things_to_do}!")
        user_input= input("Does that sound good to you?(Y/N)")
        if user_input == "N":
            pick_things_to_do = random.choice(things_to_do_list)
            print(f"You will be {pick_things_to_do}!")
            user_input= input("Does that sound good to you?(Y/N)")
if user_input == "Y":
    print(f"Traveling to {pick_destination} via {pick_mode_of_transportation}, eating at {pick_restaurant} and {pick_things_to_do} will be amazing! Enjoy your day trip!")


my_day_trip_dictionary = {"destination":[destination_list], "restaurant": [restaurant_list], "transportation": [mode_of_transportation_list], "entertainment": [things_to_do_list]}




    














