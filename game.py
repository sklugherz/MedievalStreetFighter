import pygame
from pygame import mixer
import sys

from fighter import Fighter


#class Game:
#	def __init__(self, fighter1, fighter2)
#		self.fighter1 = fighter1
#		self.fighter2 = fighter2
		


#INITIALIZE
mixer.init()
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler") 
clock = pygame.time.Clock()

#AUDIO
pygame.mixer.music.load("assets/Audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/Audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/Audio/magic.wav")
magic_fx.set_volume(0.75)

#IMAGES
bg_image = pygame.image.load("assets/Background/background.jpg").convert_alpha()
wizard_sheet = pygame.image.load("assets/EvilWizard/wizard.png").convert_alpha()
warrior_sheet = pygame.image.load("assets/FantasyWarrior/warrior.png").convert_alpha()

#FONTS
count_font = pygame.font.Font("assets/Fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/Fonts/turok.ttf", 80)

#ICONS
victory_icon = pygame.image.load("assets/Icons/victory.png").convert_alpha()
#FRAMES PER FIGHTER ANIMATIONS
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#DEFINE FIGHTER VARIABLES
WARRIOR_SIZE = 162 #pixels
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#GAME VARIABLES
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0] #p1,p2
round_over = False
ROUND_OVER_CD = 2000

#COLOR VARIABLES
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


#FUNCTIONS
def draw_bg():
	scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.blit(scaled_bg, (0, 0))


def draw_health_bar(health, x, y):
	ratio = health / 100
	pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
	pygame.draw.rect(screen, RED, (x, y, 400, 30))
	pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

def draw_text(text, font, color, x, y):
	img = font.render(text, True, color)
	screen.blit(img, (x, y))



fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	draw_bg()
	draw_health_bar(fighter_1.health, 20, 20)
	draw_health_bar(fighter_2.health, 580, 20)
	#draw score
	draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
	draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)
	#update countdown
	if intro_count <= 0:
		fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2, round_over)
		fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1, round_over)
	else:
		#displayer timer
		draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
		if (pygame.time.get_ticks() - last_count_update) >= 1000:
			intro_count -= 1
			last_count_update = pygame.time.get_ticks()


	#update fighter animations
	fighter_1.update()
	fighter_2.update()

	fighter_1.draw(screen)
	fighter_2.draw(screen)

	#check for defeat
	if round_over == False:
		if fighter_1.alive == False:
			score[1] += 1
			round_over = True
			round_over_time = pygame.time.get_ticks()
		elif fighter_2.alive == False:
			score[0] += 1
			round_over = True
			round_over_time = pygame.time.get_ticks()
	else:
		#victory img
		screen.blit(victory_icon, (360, 150))
		# reset game
		if (pygame.time.get_ticks() - round_over_time) > ROUND_OVER_CD:
			round_over = False
			intro_count = 3
			fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
			fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)


	pygame.display.flip()
	clock.tick(60)
