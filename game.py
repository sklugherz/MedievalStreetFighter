import pygame
import sys
from constants import RED,WHITE,YELLOW
from helper import draw_bg
from pygame import mixer

class Game:
	def __init__(self, fighter1, fighter2, screen):
		self.fighter_1 = fighter1
		self.fighter_2 = fighter2
		self.screen = screen
		self.clock = pygame.time.Clock()

		#FONTS
		self.count_font = pygame.font.Font("assets/Fonts/turok.ttf", 80)
		self.score_font = pygame.font.Font("assets/Fonts/turok.ttf", 80)

		#ICONS
		self.victory_icon = pygame.image.load("assets/Icons/victory.png").convert_alpha()
		
		#IMAGES
		self.game_bg = pygame.image.load("assets/Background/background.jpg").convert_alpha()

		#GAME VARIABLES
		self.intro_count = 3
		self.last_count_update = pygame.time.get_ticks()
		self.score = [0, 0] #p1,p2
		self.round_over = False
		self.game_over = False
		self.ROUND_OVER_CD = 2000

		#AUDIO
		mixer.init()
		pygame.mixer.music.load("assets/Audio/music.mp3")
		pygame.mixer.music.set_volume(0.5)
		

	def draw_health_bar(self, health, x, y):
		ratio = health / 100
		pygame.draw.rect(self.screen, WHITE, (x - 2, y - 2, 404, 34))
		pygame.draw.rect(self.screen, RED, (x, y, 400, 30))
		pygame.draw.rect(self.screen, YELLOW, (x, y, 400 * ratio, 30))

	def draw_text(self, text, font, color, x, y):
		img = font.render(text, True, color)
		self.screen.blit(img, (x, y))

	def run_game(self):
		from menu import main_menu
		pygame.mixer.music.play(-1, 0.0, 5000)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
					#maybe give control back to main menu before total exit
			#drawBG
			draw_bg(self.game_bg, self.screen)
			self.draw_health_bar(self.fighter_1.health, 20, 20)
			self.draw_health_bar(self.fighter_2.health, 580, 20)
			#draw score
			self.draw_text("P1: " + str(self.score[0]), self.score_font, RED, 20, 60)
			self.draw_text("P2: " + str(self.score[1]), self.score_font, RED, 580, 60)
			#update countdown
			if self.intro_count <= 0:
				self.fighter_1.move(self.screen.get_width(), self.screen.get_height(), self.fighter_2, self.round_over)
				self.fighter_2.move(self.screen.get_width(), self.screen.get_height(), self.fighter_1, self.round_over)
			else:
				#displayer timer
				self.draw_text(str(self.intro_count), self.count_font, RED, self.screen.get_width() / 2, self.screen.get_height() / 3)
				if (pygame.time.get_ticks() - self.last_count_update) >= 1000:
					self.intro_count -= 1
					self.last_count_update = pygame.time.get_ticks()

			#update fighter animations
			self.fighter_1.update()
			self.fighter_2.update()

			self.fighter_1.draw(self.screen)
			self.fighter_2.draw(self.screen)

			#check for defeat
			if self.round_over == False:
				if self.fighter_1.alive == False:
					self.score[1] += 1
					if self.score[1] >= 3:
						self.game_over = True
					self.round_over = True
					self.round_over_time = pygame.time.get_ticks()
				elif self.fighter_2.alive == False:
					self.score[0] += 1
					if self.score[0] >= 3:
						self.game_over = True
					self.round_over = True
					self.round_over_time = pygame.time.get_ticks()
			else:
				#victory img
				self.screen.blit(self.victory_icon, (360, 150))
				# reset game
				if (pygame.time.get_ticks() - self.round_over_time) > self.ROUND_OVER_CD:
					if self.game_over == True:
						# TODO
						main_menu() #potentially changes call method if menu becomes self contained class
					else:
						self.round_over = False
						self.intro_count = 3
						self.fighter_1.reset_health()
						self.fighter_2.reset_health()
						"""
						TODO
						SET X AND Y FOR EACHFIGHTER TO ORIGINAL POS
						GET DATA FROM NEW SELECTCHARACTER CLASS
						
						"""

			pygame.display.flip()
			self.clock.tick(60)
