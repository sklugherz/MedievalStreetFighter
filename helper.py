import pygame

def draw_bg(bg, screen):
    scaled_bg = pygame.transform.scale(bg, (screen.get_width(), screen.get_height()))
    screen.blit(scaled_bg, (0, 0))

def get_font(size):
    return pygame.font.Font("assets/Fonts/8bit.ttf", size)
