
import random

destination_list = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
restaurant_list = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
mode_of_transportation_list = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
things_to_do_list = ["Hiking", "Bicycling", "Dancing", "Singing Karaoke", "Swimming"]

greeting = "Thank you for choosing to use my Day Trip Generator! Let's get started:"
print(greeting)

pick_destination = random.choice(destination_list)
my_destination = f"Your destination is {pick_destination}!"

def destination():
    print(my_destination)
destination()

user_input= input("Does this destination sound good to you?")
my_destination = f"Your destination is {pick_destination}!"

while user_input == ("No"):
    print("Let us try again!")
    pick_destination = random.choice(destination_list)
    print(f"Your destination is {pick_destination}!")
    user_input= input("Does this destination sound good to you?")
if user_input == ("Yes"):
    print(f"{pick_destination} is a great destination!")


pick_restaurant = random.choice(restaurant_list)
my_restaurant = f"You will dine at {pick_restaurant}!"

def restaurant():
    print(my_restaurant)
restaurant()

user_input= input("Does this restaurant sound good to you?")
my_restaurant = f"Your restaurant is {pick_restaurant}!"

while user_input == ("No"):
    print("Let us try again!")
    pick_restaurant = random.choice(restaurant_list)
    print(f"Your restaurant is {pick_restaurant}!")
    user_input= input("Does this restaurant sound good to you?")
if user_input == ("Yes"):
    print(f"{pick_restaurant} is a great place to eat!")


pick_mode_of_transportation = random.choice(mode_of_transportation_list)
my_transportation = f"You will arrive by {pick_mode_of_transportation}!"

def transportation():
    print(my_transportation)
transportation()

user_input= input("Does this mode of transportation sound good to you?")
my_transportation = f"Your mode of transportation is {pick_mode_of_transportation}!"

while user_input == ("No"):
    print("Let us try again!")
    pick_mode_of_transportation = random.choice(mode_of_transportation_list)
    print(f"Your mode of transportation is {pick_mode_of_transportation}!")
    user_input= input("Does this mode of transportation sound good to you?")
if user_input == ("Yes"):
    print(f"By {pick_mode_of_transportation} is a great way to travel!")

pick_things_to_do = random.choice(things_to_do_list)
my_things_to_do = f"You will be {pick_things_to_do}!"

def things_to_do():
    print(my_things_to_do)
things_to_do()

user_input = input("Does that sound good to you?")
my_things_to_do = f"You will be {pick_things_to_do}"

while user_input == ("No"):
    print("Let us try again!")
    pick_things_to_do = random.choice(things_to_do_list)
    print(f"You will be {pick_things_to_do}!")
    user_input= input("Does that sound good to you?")
if user_input == ("Yes"):
    print(f"{pick_things_to_do} will be a lot of fun!!")

my_day_trip_dictionary = {"destination":[destination_list], "restaurant": [restaurant_list], "transportation": [mode_of_transportation_list], "entertainment": [things_to_do_list]}




#pick_destination = random.choice(destinations)
#pick_restaurant = random.choice(restaurants)
#pick_mode_of_transportation = random.choice(mode_of_transportation)
#pick_entertainment = random.choice(entertainment)


#print(pick_destination)
#print(pick_restaurant)
#print(pick_mode_of_transportation)
#print(pick_entertainment)



#print("Hello World")

#As a developer, I want to make at least three commits with descriptive messages

#As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate lists.

#destinations = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
#restaurants = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
#mode_of_transportation = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
#entertainment = ["Bingo", "Dancing", "Karaoke", "Bouncy Castle", "Comedy Club"]

#As a developer, I want to store my final day trip selections in a Dictionary, with a unique key value pair for each piece of my day trip. 

#my_day_trip_dictionary = {"destination":[destinations], "restaurant": [restaurants], "transportation": [mode_of_transportation]}
#print(my_day_trip_dictionary)

#As a user, I want a destination to be randomly selected for my day trip. 
# pick_destination = random.choice(destinations)

#As a user I want a restaurant to be randomly selected for my day trip.
# pick_restaurant = random.choice(restaurants)

#As a user I want a mode of transportation to be randomly selected for my day trip.
#pick_mode_mode_of_transportation = random.choice(mode_of_transportation)

#As a user I want a form of entertainment to be randomly selected for my day trip. 
#pick_entertainment = random.choice(entertainment)

#As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don't like one or more of those things. 

#As a user, I want to be able to confirm that my day trip is "complete" once I like all of the random selections. 

#As a user, I want to display my completed trip in the console. 

#Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


