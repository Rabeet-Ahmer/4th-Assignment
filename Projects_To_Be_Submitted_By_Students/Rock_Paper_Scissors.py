import random

def play():
    user = input("What you choose? 'r' for Rock, 'p' for Paper, 's' for scissors?" ).lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"
    
    if winner(user, computer):
        return "You win!"
    
    return "You lose!"

def winner(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's')\
        or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True
    
def main():
    while True:
        print(play())
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
