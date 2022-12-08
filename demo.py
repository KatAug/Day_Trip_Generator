import random
# destination_list = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
# restaurant_list = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
# mode_of_transportation_list = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
# things_to_do_list = ["Hiking", "Bicycling", "Dancing", "Singing Karaoke", "Swimming"]



#Take in a list 
#Randomly Choose a list item
#Ask for user verification
#Return Selected Value

def choice_selector(list):
    user_validator = False
    while user_validator == False:
        selected_item = random.choice(list)
        user_input = input(f"Do you like {selected_item}? y/n?")
        if user_input == 'y':
            print(f"Added {selected_item} to your trip!")
            return selected_item
        else:
            print("We will reselect the choice!")

# selected_destination = choice_selector(destination_list)
# selected_restaurant = choice_selector(restaurant_list)
# selected_transportation = choice_selector(mode_of_transportation_list)
# selected_entertainment = choice_selector(things_to_do_list)