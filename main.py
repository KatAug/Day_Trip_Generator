
import random

destinations = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
restaurants = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
mode_of_transportation = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
entertainment = ["Bingo", "Dancing", "Karaoke", "Bouncy Castle", "Comedy Club"]

pick_destination = random.choice(destinations)
pick_restaurant = random.choice(restaurants)
pick_mode_mode_of_transportation = random.choice(mode_of_transportation)
pick_entertainment = random.choice(entertainment)
#print(destinations, restaurants, mode_of_transportation, entertainment)
print(pick_destination)
print(pick_restaurant)
print(pick_mode_mode_of_transportation)
print(pick_entertainment)



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

