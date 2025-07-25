import random
import string

WORDS = [
    "planet", "rocket", "mirror", "castle", "shadow", "winter", "jungle", "forest", "pirate",
    "anchor", "button", "silver", "bubble", "dragon", "whistle", "candle", "tunnel", "hunter",
    "rocket", "saddle", "marble", "bottle", "ladder", "closet", "magnet", "wallet", "goblet",
    "desert", "island", "gloves", "bucket", "mystery", "danger", "ocean", "blizzard", "packet",
    "branch", "cradle", "beacon", "velvet", "engine", "sponge", "helmet", "ribbon", "window",
    "hammer", "fossil", "planet", "prison", "signal", "garage"
]

def main():
    word = random.choice(WORDS).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"'{user_letter}' is wrong letter. Lives left => {lives}")
        
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")

        print("Used letters: ", list(sorted(used_letters)))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list) ,"\n")

    if lives == 0:
        print("You lost! The word was:", word)
    else:
        print("You won! The word was:", f"'{word}'")

if __name__ == "__main__":
    main()
