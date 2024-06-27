import pygame

from game import Game
from menu import Menu
from characterselect import CharacterSelect

from state import State
from fsm import FSM

    
def main():
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
            mn = Menu(screen, menu_bg, fsm)
            mn.main_menu()
        elif current_state == State.CHARACTER_SELECT:
            cs = CharacterSelect(screen, menu_bg, fsm)
            f1,f2 = cs.run_select() # RETURN THE FIGHTERS 
        elif current_state == State.GAME:
            gm = Game(screen, f1, f2, fsm)
            gm.run_game()
        
        # Add a condition to stop the main loop if needed
        # For this example, we'll stop after one full cycle
        # if current_state == State.MENU and fsm.get_state() == State.MENU:
        #     running = False

main()