
import random

destinations = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
restaurants = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
mode_of_transportation = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
entertainment = ["playing Bingo", "Dancing", "Karaoke", "bouncing in a Bouncy Castle", "the Comedy Club"]

greeting = "Thank you for choosing Day Trip Generator! Let's get started:"
print(greeting)

pick_destination = random.choice(destinations)
my_destination = f"Your destination is {pick_destination}!"

def destination():
    print(my_destination)
destination()

user_input= input("Does this destination sound good to you?")
#while loop?? 

pick_restaurant = random.choice(restaurants)
my_restaurant = f"You will dine at {pick_restaurant}!"
def restaurant():
    print(my_restaurant)
restaurant()

pick_mode_of_transportation = random.choice(mode_of_transportation)
my_transportation = f"You will arrive via {pick_mode_of_transportation}!"
def transportation():
    print(my_transportation)
transportation()

pick_entertainment = random.choice(entertainment)
my_entertainment = f"While there, you will enjoy {pick_entertainment}!"
def entertainment():
    print(my_entertainment)
entertainment()


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

my_day_trip_dictionary = {"destination":[destinations], "restaurant": [restaurants], "transportation": [mode_of_transportation], "thing to do":[entertainment]}
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


