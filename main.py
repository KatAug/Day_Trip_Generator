
import random

destination_list = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
restaurant_list = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
mode_of_transportation_list = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
things_to_do_list = ["Hiking", "Bicycling", "Dancing", "Singing Karaoke", "Swimming"]

greeting = "Thank you for choosing to use the Day Trip Generator! Let's get started:"
print("")
print(greeting)
pick_destination = random.choice(destination_list)
my_destination = f"Your destination is {pick_destination}!"
print("")
def destination():
    print(my_destination)
destination()
print("")
user_input= input("Does this destination sound good to you?(Y/N)")
print("")
my_destination = f"Your destination is {pick_destination}!"

while user_input == ("N"):
    print("Let us try again!")
    print("")
    pick_destination = random.choice(destination_list)
    print(f"Your destination is {pick_destination}!")
    print("")
    user_input= input("Does this destination sound good to you?(Y/N)")
    print("")
    if user_input == ("Y"):
        print(f"{pick_destination} is a great destination!")
        print("")

pick_restaurant = random.choice(restaurant_list)
my_restaurant = f"You will dine at {pick_restaurant}!"
def restaurant():
    print(my_restaurant)
restaurant()
print("")
user_input= input("Does this restaurant sound good to you?(Y/N)")
print("")
my_restaurant = f"Your restaurant is {pick_restaurant}!"
while user_input == ("N"):
    print("Let us try again!")
    print("")
    pick_restaurant = random.choice(restaurant_list)
    print(f"Your restaurant is {pick_restaurant}!")
    print("")
    user_input= input("Does this restaurant sound good to you?")
    print("")
    if user_input == ("Y"):
        print(f"{pick_restaurant} is a great place to eat!")
        print("")


pick_mode_of_transportation = random.choice(mode_of_transportation_list)
my_transportation = f"You will arrive by {pick_mode_of_transportation}!"


def transportation():
    print(my_transportation)
transportation()
print("")
user_input= input("Does this mode of transportation sound good to you?(Y/N)")
print("")
my_transportation = f"Your mode of transportation is {pick_mode_of_transportation}!"

while user_input == ("N"):
    print("Let us try again!")
    print("")
    pick_mode_of_transportation = random.choice(mode_of_transportation_list)
    print(f"Your mode of transportation is {pick_mode_of_transportation}!")
    print("")
    user_input= input("Does this mode of transportation sound good to you?")
    print("")
    if user_input == ("Y"):
        print(f"By {pick_mode_of_transportation} is a great way to travel!")
        print("")

pick_things_to_do = random.choice(things_to_do_list)
my_things_to_do = f"You will be {pick_things_to_do}!"


def things_to_do():
    print(my_things_to_do)
things_to_do()
print("")
user_input = input("Does that sound good to you?(Y/N)")
print("")
my_things_to_do = f"You will be {pick_things_to_do}"
print("")
while user_input == ("N"):
    print("Let us try again!")
    print("")
    pick_things_to_do = random.choice(things_to_do_list)
    print(f"You will be {pick_things_to_do}!")
    print("")
    user_input= input("Does that sound good to you?(Y/N)")
    if user_input == ("Y"):
        print(f"{pick_things_to_do} will be a lot of fun!!")

my_day_trip_dictionary = {"Destination":[destination_list], "Restaurant": [restaurant_list], "Transportation": [mode_of_transportation_list], "Entertainment": [things_to_do_list]}
user_input = input(f"Does traveling to {pick_destination} via {pick_mode_of_transportation}, eating at {pick_restaurant} and {pick_things_to_do} sound like the perfect day trip?(Y/N)")
print("")
while user_input == "N":
    def choices(dict):
        for key in dict:
            print(key)
            print("")
    choices(my_day_trip_dictionary)
    user_input = input("Which part(s) would you like to change from the list above?")
    print("")
    if user_input == "Destination":
        pick_destination = random.choice(destination_list)
        print(f"Your new destination is {pick_destination}!")
        print("")
        if user_input == "N":
            pick_destination = random.choice(destination_list)
            print(f"Your new destination is {pick_destination}!")
            print("")
        user_input= input("Does the new destination sound good to you?(Y/N)")
        print("")
    elif user_input == "Restaurant":
        pick_restaurant = random.choice(restaurant_list)
        print(f"Your new place to eat will be {pick_restaurant}!")
        print("")
        if user_input == "N":
            pick_restaurant = random.choice(restaurant_list)
            print(f"Your new place to eat will be {pick_restaurant}!")
            print("")
        user_input= input("Does this new place to eat sound good to you?(Y/N)")
        print("")
    elif user_input == "Transportation":
        pick_mode_of_transportation  = random.choice(mode_of_transportation_list)
        print(f"Your new mode of transportation will be {pick_mode_of_transportation}!")
        print("")         
        if user_input == "N":
            pick_mode_of_transportation = random.choice(mode_of_transportation_list)
            print(f"Your new mode of transportation will be {pick_mode_of_transportation}!")
            print("")
        user_input= input("Does that sound good to you?(Y/N)")
        print("")
    elif user_input == "Entertainment":
        pick_things_to_do = random.choice(things_to_do_list)
        print(f"You will be {pick_things_to_do}!")
        print("")
        if user_input == "N":
            pick_things_to_do = random.choice(things_to_do_list)
            print(f"You will be {pick_things_to_do}!")
            print("")
        user_input= input("Does that sound good to you?(Y/N)")
        print("")   
if user_input == "Y":
    print(f"You will be traveling to {pick_destination} via {pick_mode_of_transportation}, eating at {pick_restaurant} and {pick_things_to_do} for your day trip! Have a wonderful time!")

