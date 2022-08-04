PROJECT TITLE: PHRASE HUNTER GAME (OBJECT-ORIENTED PROGRAMMING)

---TABLE OF CONTENTS---
SECTION 1: GENERAL INFO
SECTION 2: TECHNOLOGIES
SECTION 3: LICENSE

SECTION 1: GENERAL INFO

This is my third project in the Python TechDegree program at Treehouse. I'm so excited to share it with you!

The file phrase.py contains a class titled "Phrase."

It has 4 methods: __init__, display, check_guess, and check_complete.

Method 1: The __init__ method.
- This method structures each instance of the Phrase class. It receives two parameters: self and phrase. The phrase parameter represents the actual phrase that will be passed in as an argument (a string that is converted to all lowercase.)

Method 2: The display method.
- The "display" method loops through each letter in self.phrase. It then loops through each letter in the parameter "guesses," which represents a list of each guess the user enters. If a letter in self.phrase is simultaneously in the "guesses" list, the letter will print to the screen.

If the letter is not in the "guesses" list, an underscore will be printed to the screen.

Method 3: The check_guess method.
- This method takes two parameters: self and guess, which represents a list of the user's guesses. If all the letters in guesses are in self.phrase, this method will return True. If not, it will return False.

Method 4: The check_complete method.
- This method takes 2 parameters: self and guesses. "guesses" represents a list of the user's guesses. The method loops through every value/letter in self.phrase. If every letter is not present in guesses, it returns False. Otherwise, it returns True.

The file game.py contains a class titled "Game."

It has 7 methods: __init__, start, get_random_phrase, welcome, get_guess, game_over, and prompt_to_play_again.

Method 1: __init__
- This method structures each instance of the Game class. It contains an instance attribute called self.missed, which represents the number of times the user guesses incorrectly. The default value is 0.

The next instance attribute is self.phrases, which contains a list of phrases that are objects of the Phrase class.

There are 2 instance attributes remaining: self.active_phrase and self.guesses.

self.active_phrase calls the get_random_phrase method on the Game class.

Last, self.guesses holds an empty list. As the program runs, the user's inputs (their guesses) will be appended to this list.

Method 2: start
- This method takes one parameter: self. It calls the welcome method of the Game class, which presents a welcome screen. 

Then, in a while block that runs while self.missed is less than 5, and calling the check_complete method on the active_phrase attribute returns false, the number missed is printed to the console.

The display method from the Phrase class is then called on self.active_phrase, and the self.guesses list is passed in as the argument on the display method. This shows a series of underscores, and if the user guesses a letter within self.active_phrase, then the underscore is converted to that letter.

The following variable, user_guess, captures the results from the get_guess method.

Below user_guess, an if statement calls the check_guess method (from the Phrase class) on self.active_phrase. If it returns false, the self.missed instance attribute is incremented by 1.

Then the while block ends, and the game_over method is called on the Game class.

Method 3: get_random_phrase.
- This method has one parameter: self. 
- This method creates a variable called current_active_phrase, which represents a random choice from the list self.phrases. The method then returns the current active_phrase. In the __init__ method, self.active_phrase is assigned to whatever this method returns.

Method 4: welcome.
- This method prints out a welcome screen for the Phrase Hunter game. It also informs users that in order to quit any time, all they need to do is enter the word "Quit"

Method 5: get_guess.
- This method collects and returns the user's guess. It contains a try block to end the program if the user enters "Quit," and to return a ValueError if the user enters anything other than "Quit" or a single letter.
- If the user does not raise a ValueError, the script returns their guess.

Method 6: game_over.
- This method checks to see if the user has lost the game (indicated by the self.missed attribute reaching 5) or won the game (indicated by calling the check_complete method from the Phrase class on self.active_phrase.) If they have won or lost, the user is prompted to determine if they'd like to play again.

Method 7: prompt_to_play again.
- This method prompts the user to play again. If they select yes, a new instance of the game class is created and run.
- If they select no (or type quit), the game ends.

In the "app" file, there is a __name__ method. When app.py is run, an object of the Game class is created and the start method is called.

SECTION 2: TECHNOLOGIES

Project is created with:
- Python

SECTION 3: LICENSE

Copyright (c) [2022] [Stephen Asher Orr]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.