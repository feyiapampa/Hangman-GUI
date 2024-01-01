# Hangman-GUI

We undertook the development of the classic Hangman game in Python. Hangman is an engaging word-guessing game where players attempt to decipher a hidden word by guessing its individual letters. The player is presented with the word's length and given six opportunities to guess incorrectly. An incorrect guess results in the gradual display of the hangman's figure. If the hangman's complete figure is drawn after six failed attempts and the player hasn't guessed all the letters, the game ends. On successfully guessing all the letters within the word before exhausting the six attempts, the player emerges as the winner. 


Project Structure and Components: 

Choosing the Level: 
Players begin by selecting a difficulty level: easy, medium, or hard. Each level corresponds to word lengths; easy words contain 5 or fewer characters, medium words span between 6 and 8 characters, and hard words have 9 or more characters. The chosen level is stored in the variable 'level.' 


Playing the Hangman Game: 

play_hangman(self, word): 
This method orchestrates the entire gameplay. A while loop powers the game, continuing until all the letters in the word are guessed. For each incorrect attempt, an additional stage of the hangman figure is displayed. The loop persists until the sixth error or until all the underscores in the word are replaced by letters, signifying a successful guess. 

choose_word(self, level): 
This method generates a random word based on the selected level. A text file containing a dictionary of words is utilized for word selection. Words are parsed, grouped by level, and stored in corresponding lists. A word is randomly chosen from the appropriate level's list using random.choice(level), returned as 'word_to_guess.' 

Initialize_game(self, word_to_guess): 
Upon receiving the 'word_to_guess,' this method initializes the game state. It creates blank underscores matching the word's length, sets the player's available attempts to six, and initializes the list of guessed letters. The method returns the blank underscores, guessed letters list, and remaining attempts. 

display_word(self, hidden_word, guessed_letters): 
This method assists in displaying the guessed letters correctly in the word by replacing the underscores with actual letters when guessed correctly. 

check_letter(self, word, hidden_word, guessed_letters, letter): 
The method evaluates the letter guessed by the user. It checks if the letter has been guessed before. If not, it's added to the guessed letters list. Additionally, if the letter exists in the word, the corresponding underscore is replaced with the letter. 


Bugs and limitations: 
Initially, we faced issues with the initialize_game function displaying one extra underscore, later realizing Python's length function includes zero. We resolved multiple functions inadvertently returning 'None' instead of values. The code was initially structured using functions and nested functions, later reorganized to utilize Object-Oriented Programming (OOP) for better attribute management. While implementing the GUI, we encountered challenges with buttons, texts, and inputs, seeking assistance from our instructor. 

Team Member Contributions: 
Our team collaborated throughout most of the project, jointly developing code and addressing issues together. Andre devoted additional time outside of team meetings to collaborate with the instructor on GUI issues, while Emma and Feyi focused on resolving code bugs in the main game file. 

Future Extensions: 
Enhancements for the Hangman game include introducing animations and improved graphics. Adding hints, such as revealing a random unguessed letter or integrating online dictionary definitions, could enhance the gaming experience. 
