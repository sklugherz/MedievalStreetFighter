import pygame

from game import Game
from menu import Menu
from characterselect import CharacterSelect

class State:
    MENU = 'Menu'
    CHARACTER_SELECT = 'CharacterSelect'
    GAME = 'Game'

class Event:
    START_CHARACTER_SELECT = 'StartCharacterSelect'
    START_GAME = 'StartGame'
    END_GAME = 'EndGame'

class FSM:
    def __init__(self):
        self.state = State.MENU

    def transition(self, event):
        if self.state == State.MENU:
            if event == Event.START_CHARACTER_SELECT:
                self.state = State.CHARACTER_SELECT
        elif self.state == State.CHARACTER_SELECT:
            if event == Event.START_GAME:
                self.state = State.GAME
        elif self.state == State.GAME:
            if event == Event.END_GAME:
                self.state = State.MENU

    def get_state(self):
        return self.state
    
def main():
    #initialize screen to pass reference into each loop
    pygame.init()
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    menu_bg = pygame.image.load("assets/Background/menu.png").convert_alpha()

    fsm = FSM()

    running = True
    while running:
        current_state = fsm.get_state()
        if current_state == State.MENU:
            mn = Menu(screen, menu_bg)
            mn.main_menu()
        elif current_state == State.CHARACTER_SELECT:
            cs = CharacterSelect(screen, menu_bg)
            f1,f2 = cs.run_select() # RETURN THE FIGHTERS 
        elif current_state == State.GAME:
            gm = Game(screen, f1, f2)
            gm.run_game()
        
        # Add a condition to stop the main loop if needed
        # For this example, we'll stop after one full cycle
        # if current_state == State.MENU and fsm.get_state() == State.MENU:
        #     running = False

main()