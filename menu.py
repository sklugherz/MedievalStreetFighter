import pygame
from pygame import mixer
import sys
from game import Game
from fighter import Fighter
from button import Button
from constants import MENU_ORANGE, MENU_WHITE, WHITE
from characters import characters

mixer.init()
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 

#AUDIO
pygame.mixer.music.load("assets/Audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

#IMAGES
menu_bg = pygame.image.load("assets/Background/menu.png").convert_alpha()
play_rect = pygame.image.load("assets/Menu/PlayRect.png")
options_rect = pygame.image.load("assets/Menu/OptionsRect.png")
quit_rect = pygame.image.load("assets/Menu/QuitRect.png")

#CHARACTER SELECTION CROPS
elvenWarrior_crop = pygame.image.load("assets/FantasyWarrior/crop.png")
darkWizard_crop = pygame.image.load("assets/EvilWizard/crop.png")

# clock = pygame.time.Clock()

def select_character():
    p1_selected = False

    while True:
        draw_bg(menu_bg)
        mouse_pos = pygame.mouse.get_pos()

        SELECT_TEXT = get_font(100).render("SELECT YOUR FIGHTERS", True, MENU_ORANGE)
        SELECT_RECT = SELECT_TEXT.get_rect(center=(SCREEN_WIDTH / 2, 100))

        #FIGHTER CARD 
        elvenWarrior_button = Button(elvenWarrior_crop, (SCREEN_WIDTH / 2 - 20, 300), "", get_font(32), WHITE, WHITE)
        darkWizard_button = Button(darkWizard_crop, (SCREEN_WIDTH / 2 + 20, 300), "", get_font(32), WHITE, WHITE)

        screen.blit(SELECT_TEXT, SELECT_RECT)

        for button in [elvenWarrior_button, darkWizard_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if elvenWarrior_button.checkForInput(mouse_pos):
                    #query database
                    x = characters[0]
                    ew_sheet = x["sheet"]
                    ew_animations_steps = x["animationSteps"]
                    ew_soundfx = x["soundfx"]
                    ew_volume = x["volume"]
                    ew_data = [x["size"], x["scale"], x["offset"]]
                    if p1_selected == False:
                        f1 = Fighter(1, 200, 310, False, ew_data, ew_sheet, ew_animations_steps, ew_soundfx, ew_volume)
                        p1_selected = True
                        elvenWarrior_button.text_input = "P1"
                    else:
                        f2 = Fighter(1, 200, 310, False, ew_data, ew_sheet, ew_animations_steps, ew_soundfx, ew_volume)     
                        return f1,f2
                if darkWizard_button.checkForInput(mouse_pos):
                    x = characters[1]
                    dw_sheet = x["sheet"]
                    dw_animations_steps = x["animationSteps"]
                    dw_soundfx = x["soundfx"]
                    dw_volume = x["volume"]
                    dw_data = [x["size"], x["scale"], x["offset"]]
                    if p1_selected == False:
                        f1 = Fighter(2, 700, 310, True, dw_data, dw_sheet, dw_animations_steps, dw_soundfx, dw_volume)
                        p1_selected = True
                        darkWizard_button.text_input = "P1"
                    else:
                        f2 = Fighter(2, 700, 310, True, dw_data, dw_sheet, dw_animations_steps, dw_soundfx, dw_volume)
                        return f1,f2

        pygame.display.update()	

#FUNCTIONS
def get_font(size):
    return pygame.font.Font("assets/Fonts/8bit.ttf", size)

def draw_bg(bg):
    scaled_bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def play():
    fighter_1, fighter_2 = select_character()
    pygame.display.set_caption("Fight!") 
    game = Game(fighter_1, fighter_2, screen)
    game.run_game()

def options():
    pass

def main_menu():
    pygame.display.set_caption("Menu")
    while True:
        draw_bg(menu_bg)
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
                    play()
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    options()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()