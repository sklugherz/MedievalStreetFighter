import pygame
# import characterselect
import sys
from button import Button
from constants import MENU_ORANGE, MENU_WHITE, WHITE
from helper import draw_bg, get_font


class Menu:
    def __init__(self, screen, bg):
        self.screen = screen
        #IMAGES
        self.bg = bg
        self.play_rect = pygame.image.load("assets/Menu/PlayRect.png").convert_alpha()
        self.options_rect = pygame.image.load("assets/Menu/OptionsRect.png").convert_alpha()
        self.quit_rect = pygame.image.load("assets/Menu/QuitRect.png").convert_alpha()


    #FUNCTIONS
    
    # def select_characters(self):
    #     cs = characterselect.CharacterSelect(self.screen, self.menu_bg)
    #     cs.run_select()
        

    def options(self):
        pass

    def main_menu(self):
        pygame.display.set_caption("Menu")
        while True:
            draw_bg(self.menu_bg, self.screen)
            mouse_pos = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("MAIN MENU", True, MENU_ORANGE)
            MENU_RECT = MENU_TEXT.get_rect(center=(self.SCREEN_WIDTH / 2, 100))

            PLAY_BUTTON = Button(self.play_rect, pos=(self.SCREEN_WIDTH / 2, 250), 
                                text_input="PLAY", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)
            OPTIONS_BUTTON = Button(self.options_rect, pos=(self.SCREEN_WIDTH / 2, 400), 
                                text_input="OPTIONS", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)
            QUIT_BUTTON = Button(self.quit_rect, pos=(self.SCREEN_WIDTH / 2, 550), 
                                text_input="QUIT", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(mouse_pos):
                        self.select_characters()
                    if OPTIONS_BUTTON.checkForInput(mouse_pos):
                        self.options()
                    if QUIT_BUTTON.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()