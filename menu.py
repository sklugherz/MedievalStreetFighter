import pygame

import sys
from button import Button
from constants import MENU_ORANGE, MENU_WHITE, WHITE
from helper import draw_bg, get_font
from characterselect import run_select


pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 

#IMAGES
menu_bg = pygame.image.load("assets/Background/menu.png").convert_alpha()
play_rect = pygame.image.load("assets/Menu/PlayRect.png")
options_rect = pygame.image.load("assets/Menu/OptionsRect.png")
quit_rect = pygame.image.load("assets/Menu/QuitRect.png")


#FUNCTIONS
def select_characters():
    run_select(screen, menu_bg)
    

def options():
    pass

def main_menu():
    pygame.display.set_caption("Menu")
    while True:
        draw_bg(menu_bg, screen)
        mouse_pos = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, MENU_ORANGE)
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH / 2, 100))

        PLAY_BUTTON = Button(play_rect, pos=(SCREEN_WIDTH / 2, 250), 
                            text_input="PLAY", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)
        OPTIONS_BUTTON = Button(options_rect, pos=(SCREEN_WIDTH / 2, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)
        QUIT_BUTTON = Button(quit_rect, pos=(SCREEN_WIDTH / 2, 550), 
                            text_input="QUIT", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    select_characters()
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    options()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()