import random

def get_player_names():
    player1_name = input("Enter Player 1's name: ").strip()
    player2_name = input("Enter Player 2's name: ").strip()
    
    # Use default names if empty input
    if not player1_name:
        player1_name = "Player 1"
    if not player2_name:
        player2_name = "Player 2"
        
    return player1_name, player2_name

def get_valid_bounds():
    while True:
        try:
            min_num = int(input("Enter the minimum number: "))
            max_num = int(input("Enter the maximum number: "))
            
            if min_num >= max_num:
                print("Minimum number must be less than maximum number!")
                continue
                
            return min_num, max_num
        except ValueError:
            print("Please enter valid numbers!")

def play_guessing_game():
    print("Welcome to the 2-Player Number Guessing Game!")
    print("First, let's meet our players!\n")
    
    player1_name, player2_name = get_player_names()
    print(f"\nWelcome {player1_name} and {player2_name}!")
    print("Now, let's set the range for our number.")
    
    min_num, max_num = get_valid_bounds()
    number = random.randint(min_num, max_num)
    
    player1_attempts = 0
    player2_attempts = 0
    current_player = 1
    
    print(f"\nA number between {min_num} and {max_num} has been chosen.")
    
    while True:
        current_name = player1_name if current_player == 1 else player2_name
        print(f"\n{current_name}'s turn")
        try:
            guess = int(input(f"Enter your guess ({min_num}-{max_num}): "))
            
            if guess < min_num or guess > max_num:
                print(f"Please enter a number between {min_num} and {max_num}!")
                continue
                
            if current_player == 1:
                player1_attempts += 1
            else:
                player2_attempts += 1

            if guess == number:
                print(f"Correct! {current_name} wins!")
                print(f"\nGame Statistics:")
                print(f"{player1_name} took {player1_attempts} attempts")
                print(f"{player2_name} took {player2_attempts} attempts")
                
                # Determine who had fewer attempts
                if player1_attempts < player2_attempts:
                    print(f"{player1_name} was more efficient!")
                elif player2_attempts < player1_attempts:
                    print(f"{player2_name} was more efficient!")
                else:
                    print("Both players were equally efficient!")
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
            
            # Switch players
            current_player = 2 if current_player == 1 else 1
            
        except ValueError:
            print("Please enter a valid number!")

# Main game loop
while True:
    play_guessing_game()
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
