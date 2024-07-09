import random
while True:
    print("You entered into the Rock-Paper-Scissors Game!!")
    print("Type your choice: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input("Your choice: ").lower()
    choices = ['rock', 'paper', 'scissors']
    AI_choice = random.choice(choices)
    if user_choice == AI_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and AI_choice == 'scissors') or \
         (user_choice == 'paper' and AI_choice == 'rock') or \
         (user_choice == 'scissors' and AI_choice == 'paper'):
        result = "You win!"
    else:
        result = "AI wins!"
    print(f"You chose: {user_choice}")
    print(f"AI chose: {AI_choice}")
    print(result)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
print("Thanks for playing!")
