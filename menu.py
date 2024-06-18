import pygame
from pygame import mixer
import sys
from game import Game


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


mixer.init()
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler") 
clock = pygame.time.Clock()