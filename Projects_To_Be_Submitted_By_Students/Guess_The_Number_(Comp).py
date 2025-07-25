import random

def main() -> None:
  """Plays a number guessing game with the user."""

  num: int = random.randint(1, 100)

  user_num: int = int(input("I am thinking of a number between 1 and 100. Can you guess it?\n"))

  while user_num != num:
    if user_num > num:
      print(f"{user_num} is greater than my number")
    elif user_num < num:
      print(f"{user_num} is smaller than my number")

    user_num = int(input("Try again:\n"))

  print(f"{user_num} is correct!")

if __name__ == "__main__":
  main()
