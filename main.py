
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
        user_input = input("Does that sound good?(y/n):")
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
        choose_option = random.choice(list)
        print(f"You will be dining at {choose_option}!")
        print("")
        user_input = input("Does that sound good?(y/n):")
        print("")
        if user_input == "y":
            print(f"{choose_option} is great restaurant!")
            print("")
            return choose_option
        else:
            print("Let's try again!")
            print("")
result_from_selection = selection(restaurant_list)
def selection(list):
    user_choice = False
    while user_choice == False:
        choose_option = random.choice(list)
        print(f"You will be arriving via {choose_option}!")
        print("")
        user_input = input("Does that sound good?(y/n):")
        print("")
        if user_input == "y":
            print(f"{choose_option} is a great mode of transportation!")
            print("")
            return choose_option
        else:
            print("Let's try again!")
            print("")
result_from_selection = selection(mode_of_transportation_list)
def selection(list):
    user_choice = False
    while user_choice == False:
        choose_option = random.choice(list)
        print(f"You will be {choose_option}!")
        print("")
        user_input = input("Does that sound good?(y/n):")
        print("")
        if user_input == "y":
            print(f"{choose_option} will be fun!")
            print("")
            break
        else:
            print("Let's try again!")
            print("")
            return choose_option
result_from_selection = selection(things_to_do_list)
# user_input = input(f"Does traveling to {selection(destination_list)} via {selection(mode_of_transportation_list)}, eating at {selection(restaurant_list)} and {selection(things_to_do_list)} sound like the perfect day trip?(y/n)")
# print("")          
# my_day_trip_dictionary = {"Destination":[destination_list], "Restaurant": [restaurant_list], "Transportation": [mode_of_transportation_list], "Entertainment": [things_to_do_list]}
# # user_input = input(f"Does traveling to {selection(destination_list)} via {selection(mode_of_transportation_list)}, eating at {selection(restaurant_list)} and {selection(things_to_do_list)} sound like the perfect day trip?(y/n)")
# # print("")
# # user_input = input(f"Does traveling to {selection(destination_list)} via {selection(mode_of_transportation_list)}, eating at {selection(restaurant_list)} and {selection(things_to_do_list)} sound like the perfect day trip?(y/n)")
# # print("")

# def confirmation():
#     user_choice = False
#     while user_choice == False:
#         for key in dict:
#             print(key)
#             print("")
#         user_input = input("Which part(s) would you like to change from the list above?")
#         print("")

# confirmation()
    


    











# pick_things_to_do = random.choice(things_to_do_list)
# my_things_to_do = f"You will be {pick_things_to_do}!"


# def things_to_do():
#     print(my_things_to_do)
# things_to_do()
# print("")
# user_input = input("Does that sound good to you?(Y/N)")
# print("")
# my_things_to_do = f"You will be {pick_things_to_do}"
# print("")
# while user_input == ("N"):
#     print("Let us try again!")
#     print("")
#     pick_things_to_do = random.choice(things_to_do_list)
#     print(f"You will be {pick_things_to_do}!")
#     print("")
#     user_input= input("Does that sound good to you?(Y/N)")
#     print("")
#     if user_input == ("Y"):
#         print(f"{pick_things_to_do} will be a lot of fun!!")
#         print("")

# my_day_trip_dictionary = {"Destination":[destination_list], "Restaurant": [restaurant_list], "Transportation": [mode_of_transportation_list], "Entertainment": [things_to_do_list]}
# user_input = input(f"Does traveling to {pick_destination} via {pick_mode_of_transportation}, eating at {pick_restaurant} and {pick_things_to_do} sound like the perfect day trip?(Y/N)")
# print("")
# while user_input == "N":
#     def choices(dict):
#         for key in dict:
#             print(key)
#             print("")
#     choices(my_day_trip_dictionary)
#     user_input = input("Which part(s) would you like to change from the list above?")
#     print("")
# while user_input == "Destination":
#     pick_destination = random.choice(destination_list)
#     print(f"Your new destination is {pick_destination}!")
#     print("")
#     user_input = input("Does that sound good?(Y/N)")
#     print("")
#     if user_input == "N":
#         pick_destination = random.choice(destination_list)
#         print(f"Your new destination is {pick_destination}!")
#         print("")
#         user_input = input("Does that sound good?(Y/N)")
#         print("") 
# while user_input == "Restaurant":
#     pick_restaurant = random.choice(restaurant_list)
#     print(f"Your new place to eat will be {pick_restaurant}!")
#     print("")
#     if user_input == "N":
#         pick_restaurant = random.choice(restaurant_list)
#         print(f"Your new place to eat will be {pick_restaurant}!")
#         print("")
#     user_input= input("Does this new place to eat sound good to you?(Y/N)")
#     print("")
# while user_input == "Transportation":
#     pick_mode_of_transportation  = random.choice(mode_of_transportation_list)
#     print(f"Your new mode of transportation will be {pick_mode_of_transportation}!")
#     print("") 
#     user_input= input("Does that sound good to you?(Y/N)")
#     print("")      
#     if user_input == "N":
#         pick_mode_of_transportation = random.choice(mode_of_transportation_list)
#         print(f"Your new mode of transportation will be {pick_mode_of_transportation}!")
#         print("")
# while user_input == "Entertainment":
#     pick_things_to_do = random.choice(things_to_do_list)
#     print(f"You will be {pick_things_to_do}!")
#     print("")
#     if user_input == "N":
#         pick_things_to_do = random.choice(things_to_do_list)
#         print(f"You will be {pick_things_to_do}!")
#         print("")
#         user_input= input("Does that sound good to you?(Y/N)")
#         print("")   
# while user_input == "Y":
#     print(f"You will be traveling to {pick_destination} via {pick_mode_of_transportation}, eating at {pick_restaurant} and {pick_things_to_do} for your day trip! Have a wonderful time!")
#     break

