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
pygame.display.set_caption("Menu") 

#AUDIO
pygame.mixer.music.load("assets/Audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
# sword_fx = pygame.mixer.Sound("assets/Audio/sword.wav")
# sword_fx.set_volume(0.5)
# magic_fx = pygame.mixer.Sound("assets/Audio/magic.wav")
# magic_fx.set_volume(0.75)

#IMAGES
bg_image = pygame.image.load("assets/Background/background.jpg").convert_alpha()
# wizard_sheet = pygame.image.load("assets/EvilWizard/wizard.png").convert_alpha()
# warrior_sheet = pygame.image.load("assets/FantasyWarrior/warrior.png").convert_alpha()

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
    return pygame.font.Font("assets/Fonts/turok.ttf", size)

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def play():
    pygame.display.set_caption("Fight!") 
    game = Game(fighter_1, fighter_2, screen)
    game.run_game()

def options():
    pass

def main_menu():
    pass

main_menu()