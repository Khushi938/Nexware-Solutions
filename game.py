import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
    
def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose, Computer wins!"

# Main program loop
while True:
    try:
        x = int(input("Press 1 to play the game or any other number to exit: "))
        if x != 1:
            break
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

    except ValueError:
        print("That's not a valid number. Please try again.")

print("Thanks for playing!")