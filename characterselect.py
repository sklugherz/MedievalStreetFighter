import pygame
import sys
from button import Button
from characters import characters
from fighter import Fighter
from helper import draw_bg, get_font
from constants import MENU_ORANGE, WHITE
from game import Game

class CharacterSelect:
    def __init__(self, screen, bg):
        self.screem = screen
        self.bg = bg

        #LOAD CHARACTER CROPS 
        self.elvenWarrior_crop = pygame.image.load("assets/FantasyWarrior/crop.png")
        self.darkWizard_crop = pygame.image.load("assets/EvilWizard/crop.png")


    def run_select(self):
        p1_selected = False

        while True:
            draw_bg(self.bg, self.screen)
            mouse_pos = pygame.mouse.get_pos()

            SELECT_TEXT = get_font(100).render("SELECT YOUR \n FIGHTERS", True, MENU_ORANGE)
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if elvenWarrior_button.checkForInput(mouse_pos):
                        #query database
                        x = characters[0]
                        ew_sheet = x["sheet"]
                        ew_animations_steps = x["animationSteps"]
                        ew_soundfx = x["soundfx"]
                        ew_volume = x["volume"]
                        ew_data = [x["size"], x["scale"], x["offset"]]
                        if p1_selected == False:
                            f1 = Fighter(1, 200, 310, False, ew_data, ew_sheet, ew_animations_steps, ew_soundfx, ew_volume)
                            p1_selected = True
                            elvenWarrior_button.text_input = "P1"
                        else:
                            f2 = Fighter(2, 700, 310, True, ew_data, ew_sheet, ew_animations_steps, ew_soundfx, ew_volume)     
                            game = Game(f1, f2, self.screen)
                            game.run_game()
                    if darkWizard_button.checkForInput(mouse_pos):
                        x = characters[1]
                        dw_sheet = x["sheet"]
                        dw_animations_steps = x["animationSteps"]
                        dw_soundfx = x["soundfx"]
                        dw_volume = x["volume"]
                        dw_data = [x["size"], x["scale"], x["offset"]]
                        if p1_selected == False:
                            f1 = Fighter(1, 200, 310, False, dw_data, dw_sheet, dw_animations_steps, dw_soundfx, dw_volume)
                            p1_selected = True
                            darkWizard_button.text_input = "P1"
                        else:
                            f2 = Fighter(2, 700, 310, True, dw_data, dw_sheet, dw_animations_steps, dw_soundfx, dw_volume)
                            game = Game(f1, f2, self.screen)
                            game.run_game()

            pygame.display.update()	