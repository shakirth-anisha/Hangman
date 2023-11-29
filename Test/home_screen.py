import os

from tkinter import Label, Button, PhotoImage
from start_screen import start_screen
from categories_screen import categories_screen
from multiplayer_screen import multiplayer_screen
from instructions_screen import instructions_screen

BLACK = "#1C1C1E"

def home_screen(hangman):
    
    def destruction():
        hangman_txt.destroy()
        single_player_button.destroy()
        multiplayer_button.destroy()
        instructions_button.destroy()
        home_txt.destroy()
        back_button.destroy()
        
    def single_player_mode():
        destruction()
        categories_screen()
        
    def multiplayer_mode():
        destruction()
        multiplayer_screen()
    
    def instructions_mode():
        destruction()
        instructions_screen()
        
    #Buttons/Labels
    hangman_txt = Label(hangman, image=hangman_img, background=BLACK)
    hangman_txt.place(x=225, y=40)
    home_txt = Label(hangman, image=home_img, background=BLACK)
    home_txt.place(x=450, y=230)
    single_player_button = Button(hangman, image=single_player_img, background=BLACK, command=single_player_mode)
    single_player_button.place(x=50,y=230)
    multiplayer_button = Button(hangman, image=multiplayer_img, background=BLACK, command=multiplayer_mode)
    multiplayer_button.place(x=50, y=430)
    instructions_button = Button(hangman, image=instructions_img, background=BLACK, command=instructions_mode)
    instructions_button.place(x=50, y=630)
    
    def back_btn():
        destruction()
        start_screen()
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0)
    back_button.place(x=25, y=25)
    
hangman_img = PhotoImage(file=f"{os.getcwd()}/Images/Hangman.png")
home_img = PhotoImage(file=f"{os.getcwd()}/Images/Home_Screen.png")
single_player_img = PhotoImage(file=f"{os.getcwd()}/Images/Single_Player.png")
multiplayer_img = PhotoImage(file=f"{os.getcwd()}/Images/Multiplayer.png")
single_player_img = PhotoImage(file=f"{os.getcwd()}/Images/Single_Player.png")
instructions_img = PhotoImage(file=f"{os.getcwd()}/Images/Instructions.png")
back_img = PhotoImage(file=f"{os.getcwd()}/Images/Back.png")