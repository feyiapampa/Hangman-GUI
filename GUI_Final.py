import csv
from tkinter import *
from csci_final_project import *
import tkinter as tk 


#----------------------------------------------------------
class HangmanGUI:
    def __init__(self):
        self.game = Hangman()

        self.window = Tk()
        self.window.title("Hangman")
        self.window.geometry('750x600')

        self.frame_game = Frame(self.window, bg='black')
        self.frame_input = Frame(self.window, bg='grey')
    
        self.window.rowconfigure(0,weight=1)
        self.window.rowconfigure(1,weight=1)
        self.window.rowconfigure(2,weight=1)
        self.window.rowconfigure(3,weight=1)
        self.window.columnconfigure(0, weight=1) 

        self.frame_game.grid()
        self.frame_input.grid(row=3, column=0, rowspan=1, sticky='WENS')
        
        self.frame_input.rowconfigure(0,weight=1)
        self.frame_input.columnconfigure(0, weight=1)
        self.frame_input.columnconfigure(1, weight=1)
        self.frame_input.columnconfigure(2, weight=1)
        
        #------------------------Creates variable that contains the information from Frame - FOR TOP ROW (rows 0-2 which are part of the first column)---------------------------

        self.frame_input_0 = Frame(self.frame_game)
        self.frame_input_0.grid(row=0, column=0)
        
        
        #-----------------------Creates variable that contains the information from Frame - FOR BOTTOM ROW (columns in row3, which are part if the second column)-------------------------------    
        self.frame_input_1 = Frame(self.frame_input, bg='grey')
        self.frame_input_1.grid(row=0, column=0,rowspan=1, sticky='WENS')
        
        self.frame_input_2 = Frame(self.frame_input, bg='grey')
        self.frame_input_2.grid(row=0, column=1,sticky='WENS')
        
        self.frame_input_3 = Frame(self.frame_input, bg='grey')
        self.frame_input_3.grid(row=0, column=2,sticky='WENS')
        
        
        #----------------------- Column where the buttons for the game are(for each column in row 3)-------------------------------
        
        self.var = IntVar()
        R1 = Radiobutton( self.frame_input_1, text="Easy", variable=self.var, value=1)
        R1.grid( sticky="WE")
        R2 = Radiobutton( self.frame_input_1, text="Medium", variable=self.var, value=2)
        R2.grid( sticky="WE")
        R3 = Radiobutton( self.frame_input_1, text="Hard", variable=self.var, value=3)
        R3.grid( sticky="WE")
                
        #Creates variable that displays a "start" button () 
        btn_start = Button(self.frame_input_1, text="Start", command=self.select_level)
        btn_start.grid(row=3, column=0, sticky="WE")
        
        #---------------------------- Creates variable that displays a "Submit" button (where user guesses a letter)----------------------------------------------------------------------------------------------------------
        
        guess_txt = Label(self.frame_input_2, text = "Guess").grid(row = 0,column = 0, sticky='W')
        self.guess_input = Entry(self.frame_input_2)
        self.guess_input.grid(row=0, column=1, sticky='W')
        
        btn_guess = Button(self.frame_input_2, text="Guess", command=self.new_guess)
        btn_guess.grid(row=1, column=0, sticky="WE")
        
        #---------------------------- Creates variable that displays the list of used letters ----------------------------------------------------------------------------------------------------------        
  
        self.guessed_letters_box = Label(self.frame_input_3, bg="SILVER", text='')
        self.guessed_letters_box.grid(row=0, column=0, sticky="EW")
        
        #---------------------------- Creates variable that displays the Hangman game ----------------------------------------------------------------------------------------------------------        
        
        frame3 = Frame(self.frame_input_0, relief=RAISED)
        frame3.grid(row=0, column=0, sticky="ns")
  
        self.output_box = Label(frame3, width=40, text='', height=20, bg="SILVER")
        self.output_box.grid(row=0, column=0, sticky="we")

        btn_restart = Button(self.frame_input_1, text="Restart", command=self.restart_game)
        btn_restart.grid(row=4, column=0, sticky="WE")  

        # self.game.play_hangman()
        self.window.mainloop()
        
    # def print_structure():
    #     self.output_box.config(text=)
        
    def select_level(self):
        
        if self.game.word == '':
            option = str(self.var.get())
            print("You selected the option " + option)
      
            if option == '1':
                self.game.initialize_game('easy')
            elif option == '2':
                self.game.initialize_game('medium')
            else:
                self.game.initialize_game('hard')
            out = f'Guessed letters: {str(self.game.guessed_letters)} \nAttempts left: {self.game.attempts_left}'
            self.guessed_letters_box.config(text=out)
            
            out2 = str(self.game.hidden_word)
            self.output_box.config(text=out2)
                
    def new_guess(self):
        letter = self.guess_input.get()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
        else:
            result = self.game.guess_letter(letter)
            
            out = f'Guessed letters: {str(self.game.guessed_letters)} \nAttempts left: {self.game.attempts_left}'
            self.guessed_letters_box.config(text=out)
             
            if 'Congratulations' in result or 'Sorry' in result:
                out2 = ''
            elif self.game.attempts_left == 0:
                result =  result = "Sorry, you're out of attempts. The word was: " + self.game.word
                out2 = ''
            else:
                out2 = f'{str(self.game.hidden_word)}'
                
            self.output_box.config(text=result + out2)
        
        if ("_" not in self.game.hidden_word):
            self.game.guess_letter

    def restart_game(self):
        self.game = Hangman()  # Reinitialize the Hangman instance
        self.output_box.config(text='')  # Clear the output display
        self.guessed_letters_box.config(text='')  # Clear guessed letters display
            
h = HangmanGUI()
        