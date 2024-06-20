import pygame
from pygame import mixer
import sys
from game import Game
from fighter import Fighter
from button import Button

mixer.init()
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 

#AUDIO
pygame.mixer.music.load("assets/Audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
# sword_fx = pygame.mixer.Sound("assets/Audio/sword.wav")
# sword_fx.set_volume(0.5)
# magic_fx = pygame.mixer.Sound("assets/Audio/magic.wav")
# magic_fx.set_volume(0.75)

#IMAGES
menu_bg = pygame.image.load("assets/Background/menu.jpg").convert_alpha()
play_rect = pygame.image.load("assets/Menu/PlayRect.png")
options_rect = pygame.image.load("assets/Menu/OptionsRect.png")
quit_rect = pygame.image.load("assets/Menu/QuitRect.png")

# clock = pygame.time.Clock()

fighter_1 = None
fighter_2 = None

def select_character():
    """
    Run character selection
    query "database"
    initialize fighters
    """
    pass
# fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
# fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
		

#FUNCTIONS
def get_font(size):
    return pygame.font.Font("assets/Fonts/8bit.ttf", size)

def draw_bg(bg):
    scaled_bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def play():
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
        PLAY_BUTTON = Button(play_rect, pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(options_rect, pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(quit_rect, pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


main_menu()