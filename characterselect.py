import pygame
import sys
from button import Button
from helper import draw_bg, get_font
from constants import MENU_ORANGE, WHITE
from event import Event

class CharacterSelect:
    def __init__(self, screen, bg, fsm):
        self.screen = screen
        self.bg = bg
        self.fsm = fsm

        # LOAD CHARACTER CROPS 
        self.elvenWarrior_crop = pygame.image.load("assets/FantasyWarrior/crop.png").convert_alpha()
        self.darkWizard_crop = pygame.image.load("assets/EvilWizard/crop.png").convert_alpha()

        # FIGHTER CARDS
        ### CAN PROBABLY AUTOMATE LOADING/BUTTON CREATION
        self.cards = []

        self.elvenWarrior_button = Button(self.elvenWarrior_crop, (self.screen.get_width() / 2 - 20, 300), "", get_font(32), WHITE, WHITE)
        self.darkWizard_button = Button(self.darkWizard_crop, (self.screen.get_width() / 2 + 20, 300), "", get_font(32), WHITE, WHITE)

        self.cards.append(self.elvenWarrior_button)
        self.cards.append(self.darkWizard_button)

        # STATIC TEXT
        self.SELECT_TEXT = get_font(50).render("SELECT YOUR FIGHTERS", True, MENU_ORANGE)
        self.SELECT_RECT = self.SELECT_TEXT.get_rect(center=(self.screen.get_width() / 2, 100))

        

    def run_select(self):
        pygame.display.set_caption("Pre-Fight")
        p1_selected = False
        running = True
        while running:
            draw_bg(self.bg, self.screen)
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.SELECT_TEXT, self.SELECT_RECT)

            for button in self.cards:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # RETURN FIGHTER NAMES ONLY SO CREATION CAN BE DONE IN GAME INSTEAD
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.elvenWarrior_button.checkForInput(mouse_pos):
                        #query database
                        if p1_selected == False:
                            f1 = "Elven Warrior"
                            p1_selected = True
                            self.elvenWarrior_button.text_input = "P1"
                            button.update(self.screen)
                        else:
                            f2 = "Elven Warrior"
                            # EVENT
                            # CHANGE GAME STATE
                            self.fsm.transition(Event.START_GAME)
                            running = False

                    if self.darkWizard_button.checkForInput(mouse_pos):
                        if p1_selected == False:
                            f1 = "Dark Wizard"
                            p1_selected = True
                            self.darkWizard_button.text_input = "P1"
                            button.update(self.screen)
                        else:
                            f2 = "Dark Wizard"
                            # EVENT
                            # CHANGE GAME STATE
                            self.fsm.transition(Event.START_GAME)
                            running = False

            pygame.display.update()	
        return f1,f2