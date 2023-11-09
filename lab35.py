#!/usr/bin/env python3
# this program suggests a restaurant to go to based on which type of cuisine you feel like having

import random

def main():

    # dictionary of restaurants for each cuisine
    restaurants = {
        "Italian": ["Olive Garden", "Carrabba's Italian Grill", "Maggiano's Little Italy"],
        "Mexican": ["Taco Bell", "Chipotle Mexican Grill", "Qdoba Mexican Eats"],
        "Asian": ["P.F. Chang's", "Pei Wei Asian Diner", "Sushi Sake"],
        "American": ["McDonald's", "Burger King", "Denny's"],
    }


    while True:
            #here is the initial question asking what cuisine the user wants
            # .strip() gets rid of any extra spaces the user might add and .title() capitilizes the cuisine to match the keys in the dictionary
            
            cuisine_preference = input("What type of cuisine are you in the mood for? (Italian, Mexican, Asian, American): ").strip().title()

            #first it is checking to see if the cuisine type exists as a key in the dictonary
            
            if cuisine_preference in restaurants:
                
                #next a restaurant_suggestion variable is made using the random module to pick one of the restaurants from the dictionary according to the cuisine preference the user entered
                restaurant_suggestion = random.choice(restaurants[cuisine_preference])
                
                #This will display the restaurant suggestion to the user
                print(f"For {cuisine_preference} cuisine, you can try: {restaurant_suggestion}")
                
                # this is for if the user does not pick from the available options 
            else:
                print("Sorry, we don't have that option")
                
            #finally at the end of the program there is the option to try again or leave
            try_again = input("Would you like to try again? (Yes/No): ").strip().lower()
            if try_again == "no":
                break  
            elif try_again !="yes" and try_again !="no":
                print("Invalid Input, Goodbye")
                break

if __name__ == "__main__":
    main()
