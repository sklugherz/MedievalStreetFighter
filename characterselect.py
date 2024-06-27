import pygame
import sys
from button import Button
from characters import characters
from fighter import Fighter
from helper import draw_bg, get_font
from constants import MENU_ORANGE, WHITE
import game

class CharacterSelect:
    def __init__(self, screen, bg, fsm):
        self.screen = screen
        self.bg = bg
        self.fsm = fsm
        
        #LOAD CHARACTER CROPS 
        self.elvenWarrior_crop = pygame.image.load("assets/FantasyWarrior/crop.png").convert_alpha()
        self.darkWizard_crop = pygame.image.load("assets/EvilWizard/crop.png").convert_alpha()


    def run_select(self):
        p1_selected = False

        while True:
            draw_bg(self.bg, self.screen)
            mouse_pos = pygame.mouse.get_pos()

            SELECT_TEXT = get_font(50).render("SELECT YOUR FIGHTERS", True, MENU_ORANGE)
            SELECT_RECT = SELECT_TEXT.get_rect(center=(self.screen.get_width() / 2, 100))

            #FIGHTER CARD 
            elvenWarrior_button = Button(self.elvenWarrior_crop, (self.screen.get_width() / 2 - 20, 300), "", get_font(32), WHITE, WHITE)
            darkWizard_button = Button(self.darkWizard_crop, (self.screen.get_width() / 2 + 20, 300), "", get_font(32), WHITE, WHITE)

            self.screen.blit(SELECT_TEXT, SELECT_RECT)

            for button in [elvenWarrior_button, darkWizard_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # RETURN FIGHTER NAMES ONLY SO CREATION CAN BE DONE IN GAME INSTEAD
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if elvenWarrior_button.checkForInput(mouse_pos):
                        #query database
                        if p1_selected == False:
                            f1 = "Elven Warrior"
                            p1_selected = True
                            elvenWarrior_button.text_input = "P1"
                            button.update(self.screen)
                        else:
                            f2 = "Elven Warrior"
                            # EVENT
                            # CHANGE GAME STATE

                    if darkWizard_button.checkForInput(mouse_pos):
                        if p1_selected == False:
                            f1 = "Dark Wizard"
                            p1_selected = True
                            darkWizard_button.text_input = "P1"
                            button.update(self.screen)
                        else:
                            f2 = "Dark Wizard"
                            # EVENT
                            # CHANGE GAME STATE

            pygame.display.update()	