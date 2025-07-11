#import logo from art.py
#import vs icon from art.py
from art import logo, vs



#import random function get random values from list
import random

#import dictionary of values from game_data.py
import game_data

#demo compare message: Compare A: Cristiano Ronaldo, A Footballer, From Portugal then the vs icon then Compare B
def format_data(account):
    """Format the account data into this printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# #get a temp list to store the current B that will become A in the next comparison
# temp_choice = []

#need to randomly choose an entry from a list. this entry will be a dictionary with the IG value to compare.
#when choosing values from array to compare ensure the same two values are never chosen

def check_answer(user_guess, a_followers, b_followers):
    """Take the user's guess and the follower counts and returns if the user guessed correctly"""
    # if a_followers > b_followers and user_guess == "a"  this is a long way to do this
    if a_followers > b_followers:
        # if user_guess == "a":
        #     return True
        # else:
        #     return False
        ## Same AS
        # if user_guess == "a":
        return user_guess == "a" #will return true if this is true and false if it isn't
    else:
        return user_guess == "b"
        ## this says if A has more followers and they guessed A, return True.
        ## if B has more followers and they guessed B, return True
        ## if the opposite happens return False

print(logo)
score = 0
continue_game = True
choice_b = random.choice(game_data.data)

#repeat game
while continue_game:
    choice_a = choice_b
    choice_b = random.choice(game_data.data)

    if choice_a == choice_b:
        choice_b = random.choice(game_data.data)

    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Against B: {format_data(choice_b)}")

    #get the user choice, A or B, for which is user
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear the screen
    print("\n" * 30)
    print(logo)

    ## Check if user is correct
    ## Get follower count of each account
    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]

    ## Use if statement to check if user is correct
    is_correct = check_answer(choice, a_follower_count, b_follower_count)

    ## Now give user feedback on their guesses
    ## track and  give score
    if is_correct:
        score += 1
        print(f"You're right! You win! Your current score is {score}")
    else:
        print(f"Sorry, you're wrong. Game over! Your final score is: {score}")
        continue_game = False


# now make the game repeatable



#need a function to compare IG followers from 2 dictionary entries. do this by saving one
#to A and the other to B. Need a temp variable to store the current new choice. so if from choice A
# and choice B whoever wins the first game becomes A then the next option chosen at random becomes B
# then this B, if the game continues, will become the next A


#Message if correct answer: You're right! Current score: 1
#Message if incorrect answer: Sorry, that's wrong. Final score: 1

# function to iterate current score across games

# Game ends when the user guesses incorrectly

#write a function that takes in two choices or dictionaries and compares the IG followers of both then returns
#the account with more followers

# def higher_or_lower(choice1, choice2):
#     if choice1 < choice2:
#         print("Choice A is larger.")
#     else:
#         print("Choice B is larger.")