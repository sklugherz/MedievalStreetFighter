import pygame
import sys
from button import Button
from constants.colors import MENU_ORANGE, MENU_WHITE, WHITE
from core.helper import draw_bg, get_font
from constants.event import Event
class Menu:
    def __init__(self, screen, bg, fsm):
        self.screen = screen
        self.fsm = fsm
        
        #IMAGES
        self.bg = bg
        self.play_rect = pygame.image.load("../assets/Menu/PlayRect.png").convert_alpha()
        self.options_rect = pygame.image.load("../assets/Menu/OptionsRect.png").convert_alpha()
        self.quit_rect = pygame.image.load("../assets/Menu/QuitRect.png").convert_alpha()

        # STATIC TEXT
        self.MENU_TEXT = get_font(100).render("MAIN MENU", True, MENU_ORANGE)
        self.MENU_RECT = self.MENU_TEXT.get_rect(center=(self.screen.get_width() / 2, 100))

        # BUTTONS
        self.PLAY_BUTTON = Button(self.play_rect, pos=(self.screen.get_width() / 2, 250), 
                            text_input="PLAY", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)
        self.OPTIONS_BUTTON = Button(self.options_rect, pos=(self.screen.get_width() / 2, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)
        self.QUIT_BUTTON = Button(self.quit_rect, pos=(self.screen.get_width() / 2, 550), 
                            text_input="QUIT", font=get_font(75), base_color=MENU_WHITE, hovering_color=WHITE)

    #FUNCTIONS
    def options(self):
        pass

    def main_menu(self):
        pygame.display.set_caption("Menu")
        running = True
        while running:
            draw_bg(self.bg, self.screen)
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.MENU_TEXT, self.MENU_RECT)

            for button in [self.PLAY_BUTTON, self.OPTIONS_BUTTON, self.QUIT_BUTTON]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.PLAY_BUTTON.checkForInput(mouse_pos):
                        # EVENT
                        # CHANGE STATE
                        self.fsm.transition(Event.START_CHARACTER_SELECT)
                        running = False
                    if self.OPTIONS_BUTTON.checkForInput(mouse_pos):
                        # TODO
                        self.options() 
                    if self.QUIT_BUTTON.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()