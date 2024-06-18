import pygame
from pygame import mixer
import sys

from fighter import Fighter

class Game:
	def __init__(self, fighter1, fighter2):
		self.fighter1 = fighter1
		self.fighter2 = fighter2
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

		#FIGHTERS
		fighter_1 = Fighter(1, 200, 310, False, self.WARRIOR_DATA, warrior_sheet, self.WARRIOR_ANIMATION_STEPS, sword_fx)
		fighter_2 = Fighter(2, 700, 310, True, self.WIZARD_DATA, wizard_sheet, self.WIZARD_ANIMATION_STEPS, magic_fx)


	#FUNCTIONS
	def draw_bg(self):
		scaled_bg = pygame.transform.scale(self.bg_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.screen.blit(scaled_bg, (0, 0))


	def draw_health_bar(self, health, x, y):
		ratio = health / 100
		pygame.draw.rect(self.screen, self.WHITE, (x - 2, y - 2, 404, 34))
		pygame.draw.rect(self.screen, self.RED, (x, y, 400, 30))
		pygame.draw.rect(self.screen, self.YELLOW, (x, y, 400 * ratio, 30))

	def draw_text(self, text, font, color, x, y):
		img = font.render(text, True, color)
		self.screen.blit(img, (x, y))




	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			self.draw_bg()
			self.draw_health_bar(fighter_1.health, 20, 20)
			self.draw_health_bar(fighter_2.health, 580, 20)
			#draw score
			self.draw_text("P1: " + str(self.score[0]), self.score_font, self.RED, 20, 60)
			self.draw_text("P2: " + str(self.score[1]), self.score_font, self.RED, 580, 60)
			#update countdown
			if intro_count <= 0:
				fighter_1.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, fighter_2, round_over)
				fighter_2.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, fighter_1, round_over)
			else:
				#displayer timer
				self.draw_text(str(intro_count), self.count_font, self.RED, self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 3)
				if (pygame.time.get_ticks() - last_count_update) >= 1000:
					intro_count -= 1
					last_count_update = pygame.time.get_ticks()


			#update fighter animations
			fighter_1.update()
			fighter_2.update()

			fighter_1.draw(self.screen)
			fighter_2.draw(self.screen)

			#check for defeat
			if round_over == False:
				if fighter_1.alive == False:
					self.score[1] += 1
					round_over = True
					round_over_time = pygame.time.get_ticks()
				elif fighter_2.alive == False:
					self.score[0] += 1
					round_over = True
					round_over_time = pygame.time.get_ticks()
			else:
				#victory img
				self.screen.blit(self.victory_icon, (360, 150))
				# reset game
				if (pygame.time.get_ticks() - round_over_time) > self.ROUND_OVER_CD:
					round_over = False
					intro_count = 3
					fighter_1 = Fighter(1, 200, 310, False, self.WARRIOR_DATA, self.warrior_sheet, self.WARRIOR_ANIMATION_STEPS, self.sword_fx)
					fighter_2 = Fighter(2, 700, 310, True, self.WIZARD_DATA, self.wizard_sheet, self.WIZARD_ANIMATION_STEPS, self.magic_fx)


			pygame.display.flip()
			self.clock.tick(60)
