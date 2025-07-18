# Required Libraries

import random

# Create List  for difficulty levels

easy_password = ['apple', 'banana', 'grape', 'peach', 'berry']
medium_password = ['orange', 'kiwi', 'melon', 'papaya', 'mango']
hard_password = ['pineapple', 'watermelon', 'strawberry', 'blueberry', 'blackberry']

# Function for Guessing the Password

def password_guessing_game():
    print("\n!!! Welcome To Password Guessing Game !!!\n")
    print("!!! Designed By Mabtoor Mabx !!!\n")
    print("Choose The Difficulty Mode: \n 1 For Easy \n 2 For Medium \n 3 For Hard\n")

    # Choose the Difficulty Level
    choice  = input("Enter Either 1 or 2 or 3: \n").strip()

    if choice == '1':
        password = random.choice(easy_password)
        print("\n Easy Mode Activated!")
    elif choice=='2':
        password = random.choice(medium_password)
        print("\n Medium Mode Activated!")
    elif choice =='3':
        password = random.choice(hard_password)
        print("\n Hard Mode Activated!")
    else:
        print("\n Invalid Choice! Default to Easy Mode.")
        password = random.choice(easy_password)
    
    # Start Guess the Password
    attempts= 0
    print("\n Guess The Password!!!")
    print(f'\n Hint: The Password length is {len(password)}')

    while True:
        guess = input("\n Enter Your Guess:!!!").strip()
        attempts = attempts+1

        if guess.lower()==password.lower():
            print(f"Congratulations! You Guessed The correct password in {attempts} attempts.")
            break
        else:
            correct_letters = ""
            for i in range(len(guess)):
                if i < len(password) and guess[i].lower() == password[i].lower():
                    correct_letters += guess[i]
                else:
                    correct_letters = "*"
            print(f"❌ Wrong guess! Correct letters in correct position: {correct_letters}")
            print(f"Hint: Password length is {len(password)}")
    print("\n Thank You so Much for Playing The Game. Hope You Enjoyed It!!! Designed by Mabtoor Mabx")

# Run The Game

if __name__ == "__main__":
    password_guessing_game()




