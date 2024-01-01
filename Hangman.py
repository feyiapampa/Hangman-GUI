import random
import re
import string


class Hangman:
    # Access the wordlist text file as a dictionary
    def __init__(self):
        self.word = ''
        self.hidden_word = ''
        self.guessed_letters = []
        self.attempts_left = 0
        self.current_stage = 0
        self.outcome = ''
        
        # printing the hangman structure
        self.hangman_stages = [
            '''
            _______
            |/      |
            |      
            |      
            |     
            |     
            -     
            ''',
            '''
            _______
            |/      |
            |      (_)
            |      
            |     
            |     
            -     
            ''',
            '''
            _______
            |/      |
            |      (_)
            |       |
            |       
            |     
            -     
            ''',
            
            '''
            _______
            |/      |
            |      (_)
            |      \|/
            |       
            |     
            -     
            ''',
            '''
            _______
            |/      |
            |      (_)
            |      \|/
            |       |
            |     
            -     
            ''',
            '''
            _______
            |/      |
            |      (_)
            |      \|/
            |       |
            |     /    \\
            -     
            '''
        ]
    #--------------------------------------------------------

    #--------------------------------------------------------    
    # Function to initialize the game state   
    def initialize_game(self, level):
        print('Initializing a new game...')
        self.word = self.choose_word(level)
        self.hidden_word = ['_'] * (len(self.word))
        self.guessed_letters = []
        self.attempts_left = 0
        if len(self.word) == 5:
            self.attempts_left = 6  # Easy level for words of length 5 or fewer
        elif len(self.word) <= 8:
            self.attempts_left = 6  # Medium level for words of length 6 to 8
        else:
            self.attempts_left = 6  # Hard level for words longer than 8
        print(self.word, self.hidden_word, self.guessed_letters, self.attempts_left)
     
    #--------------------------------------------------------   
    # Function to choose a random word based on difficulty level and word length
    def choose_word(self, level):
        
        if level == "easy":
            easy_words = [word.strip() for word in open('wordlist.txt', mode='r') if len(word)== 5 ]
            return random.choice(easy_words).lower()
        elif level == "medium":
            medium_words = [word.strip() for word in open('wordlist.txt', mode='r') if 6<= len(word)<= 8]
            return random.choice(medium_words).lower()
        elif level == "hard":
            hard_words = [word.strip() for word in open('wordlist.txt', mode='r') if len(word)> 8]
            return random.choice(hard_words).lower()   
    #--------------------------------------------------------
    # Function to display the current state of the word
    def display_word(self, hidden_word, guessed_letters):
        displayed_word = ''
        for letter in hidden_word:
            if letter in guessed_letters or letter == " ":
                if letter == " ":
                    displayed_word += '/ '
                else:
                    displayed_word += letter + ' '
            else:
                displayed_word += '_ '    
        return displayed_word.rstrip()  
    #--------------------------------------------------------
    # Example of a check letter function
    def check_letter(self, word, hidden_word, guessed_letters, letter):
        if letter in guessed_letters:
            return "You already guessed that letter."
        guessed_letters.append(letter)
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            return "Good guess!"
        else:
            return "Oops! That letter is not in the word."

    #--------------------------------------------------------
    def guess_letter(self, letter):
        result = ''
    
        if self.attempts_left > 0 and '_' in self.hidden_word:
            result = self.check_letter(self.word, self.hidden_word, self.guessed_letters, letter)
            
            if result != "Good guess!":
                self.attempts_left -= 1
                result = self.hangman_stages[self.current_stage]
                self.current_stage += 1
                return result + 'Oops! That letter is not in the word' + '\n'

                 
        if self.attempts_left < 1: 
            result = "Sorry, you're out of attempts. The word was: " + self.word   
            
        if '_' not in self.hidden_word:
            result = "Congratulations! You've guessed the word: " + self.word 
                
        return result

    # ---------------------------



