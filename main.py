
import random

destination_list = ["Galveston Island", "Jacob's Well", "Six Flags Fiesta", "Dinosaur Valley State Park", "Bracken Cave"]
restaurant_list = ["Whataburger", "Chili's", "Texas Roadhouse", "Chick-fil-A", "Firehouse Subs"]
mode_of_transportation_list = ["Car", "Bus", "Train", "Motorcycle", "Helicopter"]
things_to_do_list = ["Hiking", "Bicycling", "Dancing", "Singing Karaoke", "Swimming"]


def greeting():
    print(""" 
Thank you for choosing to use the Day Trip Generator! 
    """)
greeting()
print("Let's get started:")
print("")

def selection(list):
    user_choice = False
    while user_choice == False:
        choose_option = random.choice(list)
        print(f"You got {choose_option} for your destination!")
        print("")
        user_input = input("Does that sound good?(y/n): ")
        print("")       
        if user_input == "y":
            print(f"{choose_option} is a great destination!")
            print("")
            return choose_option
        else:
            print("Let's try again!")
            print("")
result_from_selection = selection(destination_list)
def selection(list):
    user_choice = False
    while user_choice == False:
        choose = random.choice(list)
        print(f"You will be dining at {choose}!")
        print("")
        user_input = input("Does that sound good?(y/n): ")
        print("")
        if user_input == "y":
            print(f"{choose} is great restaurant!")
            print("")
            return choose
        else:
            print("Let's try again!")
            print("")
result_from_selection = selection(restaurant_list)
def selection(list):
    user_choice = False
    while user_choice == False:
        choice = random.choice(list)
        print(f"You will be arriving via {choice}!")
        print("")
        user_input = input("Does that sound good?(y/n): ")
        print("")
        if user_input == "y":
            print(f"{choice} is a great mode of transportation!")
            print("")
            return choice
        else:
            print("Let's try again!")
            print("")
result_from_selection = selection(mode_of_transportation_list)
def selection(list):
    user_choice = False
    while user_choice == False:
        option = random.choice(list)
        print(f"You will be {option}!")
        print("")
        user_input = input("Does that sound good?(y/n): ")
        print("")
        if user_input == "y":
            print(f"{option} will be fun!")
            print("")
            break
        else:
            print("Let's try again!")
            print("")
result_from_selection = selection(things_to_do_list)

my_day_trip_dictionary = {"destination": "Galveston Island", 
"well": "Jacob's Well", "flags": "Six Flags Fiesta", "dino": "Dinosaur Valley State Park", "cave": "Bracken Cave", 
"restaurant": "Whataburger", "pasta": "Chili's", "steak": "Texas Roadhouse","chicken": "Chick-Fil-A", "sub": "Firehouse Subs",
"transportation":"bus", "auto":"car", "track": "train", "wheels": "motorcycle", "fly": "helicopter",
"entertainment": "dancing", "walking":"hiking", "riding": "bicycling", "sing": "singing Karaoke", "stroke": "swimming"}


# def final_result(dict): 
# for keys in my_day_trip_dictionary:
#         print(keys)

# user_input = input("Are you happy with your day trip selections? (y/n): ") 

#As a user, I want to display my completed trip in the console.

#As developer, I want to store my final day trip selections in a Dictionary, with a unique key value pair for each piece of my day trip.
# trip = {
#     "destination": "Timbuktu",
#     # rest of your options go here as key value pairs
# }

# final_trip_results_dict = {}
# print(final_trip_results_dict["Destination"])

# my_day_trip_dictionary = {"Destination": [destination_list], "Restaurant": [restaurant_list], "Transportation": [mode_of_transportation_list], "Entertainment": [things_to_do_list]}
# print(my_day_trip_dictionary["Destination"]) 

# def select_again():
#     for keys in my_day_trip_dictionary:
#         print(keys)
#         print("")
#         user_input = input("Which part(s) would you like to change from the list above? ")
#         print("")
#     if user_input == keys:
#         choose_option = random.choice(list)
# select_again()







 

