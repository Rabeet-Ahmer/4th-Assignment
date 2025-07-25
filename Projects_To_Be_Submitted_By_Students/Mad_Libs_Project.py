import random

def main():
    print("Mad Lib Generator! 📝 \n")
    noun1: str = str(input("Enter a noun (e.g., dragon, sandwich):\n"))
    adj1: str = str(input("Enter an adjective (e.g., sparkling, mischievous):\n"))
    verb1: str = str(input("Enter a verb (e.g., dance, explode):\n"))
    noun2: str = str(input("Enter another noun (e.g., wizard, toaster):\n"))
    adj2: str = str(input("Enter another adjective (e.g., gigantic, perplexed):\n"))
    verb2: str = str(input("Enter another verb (e.g., sing, teleport):\n"))
    place: str = str(input("Enter a location (e.g., castle, supermarket):\n"))
    emotion: str = str(input("Enter an emotion (e.g., joy, bewilderment):\n"))
    
    SENTENCE: list = [
        f"On a day filled with {emotion}, the {adj1} {noun1.capitalize()} was attempting to {verb1} quietly in the {place}, when suddenly, without warning, a {adj2} {noun2.capitalize()} appeared out of nowhere, causing such a commotion that the {noun1.capitalize()} forgot all about {verb1}ing and instead became completely absorbed in watching the {noun2.capitalize()} {verb2} wildly, which resulted in an unexpected series of events that nobody in the {place} could have possibly predicted.",

        f"While the {adj1} {noun1.capitalize()} was practicing how to {verb1} professionally in the middle of the {place}, an extraordinary thing occurred: a {adj2} {noun2.capitalize()} came bursting through the ceiling and began to {verb2} violently, which not only interrupted the {noun1.capitalize()}'s {verb1}ing session but also created such an absurd spectacle that everyone present was torn between running away in fear and staying to watch the unbelievable display of the {noun2.capitalize()} continuing to {verb2} with increasing intensity.",

        f"The {place} had never seen anything quite like it - first the {adj1} {noun1.capitalize()} started to {verb1} uncontrollably near the entrance, drawing everyone's attention, and then, as if that wasn't strange enough, a {adj2} {noun2.capitalize()} materialized from thin air and proceeded to {verb2} with such enthusiasm that the original {noun1.capitalize()} stopped mid-{verb1} and simply stared in amazement at the unfolding chaos that was now dominating the entire {place}."
    ]
    
    print("\nYour Mad Lib Story:\n")
    print(random.choice(SENTENCE))

if __name__ == "__main__":
    main()
