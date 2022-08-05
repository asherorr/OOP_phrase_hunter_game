from string import ascii_lowercase
from phrase import Phrase
import random
import sys


class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase('There is a snake in my boot'),
            Phrase('Life is like a box of chocolates'),
            Phrase('An eye for an eye'),
            Phrase('Better late than never'),
            Phrase('Cool as a cucumber')
        ]
        self.active_phrase = Game.get_random_phrase(self)
        self.guesses = [" "]

    def start(self):
        Game.welcome(self)
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"\nNumber missed: {self.missed} out of 5.")
            self.active_phrase.display(self.guesses)
            user_guess = Game.get_guess(self)
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        Game.game_over(self)

    def get_random_phrase(self):
        current_active_phrase = random.choice(self.phrases)
        return current_active_phrase

    def welcome(self):
        print("=============================")
        print(" WELCOME TO PHRASE HUNTER!")
        print("=============================")
        print("Objective: guess each letter in the phrase!")
        print("\nTo quit the game at any time, enter 'Quit'")

    def get_guess(self):
        while True:
            try:
                acquire_guess = str(input("\nEnter a letter: ")).lower()
                if acquire_guess == "QUIT".lower():
                    print("OK! The game is closing down now.")
                    sys.exit()
                if len(acquire_guess) > 1:
                    raise ValueError("Please enter only one letter.")
                for letter in acquire_guess:
                    if letter not in ascii_lowercase:
                        raise ValueError("Please enter only a letter.")
            except ValueError as err:
                print(f"Oh no! We ran into an issue. {err}")
            else:
                return acquire_guess
            
    def game_over(self):
        if self.missed >= 5:
            print("Game over!")
            print("Only 5 incorrect guesses are allowed per game. Feel free to try again!")
            Game.prompt_to_play_again(self)
        if self.active_phrase.check_complete(self.guesses) == True:
            print("You won the game! Congratulations!")
            Game.prompt_to_play_again(self)

    def prompt_to_play_again(self):
        while True:
            prompt_to_play_again = input("Would you like to play again? Enter yes or no: ")
            try:
                if not any (entry in prompt_to_play_again.lower() for entry in ("yes", "no", "quit")):
                    raise ValueError("Please enter only yes or no.")
            except ValueError as err:
                print(f"Oh no! We ran into an issue. {err}")
            else:
                if prompt_to_play_again.lower() == "yes":
                    new_instance = Game()
                    new_instance.start()
                if prompt_to_play_again.lower() == "no" or "quit":
                    print("OK! The game is closing down now.")
                    sys.exit()
