"""Main logic to run the game"""

import pygame
import sys
from connect_4.title_screen import TitleScreen
from connect_4.sounds import Sounds


class Game:
    """Makes the game run"""

    def __init__(self):
        pygame.init()

        self.start_game = False
        self.selected_option = None
        self.title_screen = TitleScreen()

    def run(self):
        """Main loop"""

        # plays the music when game starts
        Sounds.start()

        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ) or event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # calling the handle event
                    self.title_screen.handle_button_event(MENU_MOUSE_POS)

                    if self.title_screen.selected_option:
                        if self.title_screen.selected_option == "AI vs AI":
                            self.start_game = True

                        elif self.title_screen.selected_option == "Player vs AI":
                            # Implement functionality here
                            self.start_game = True

                        elif self.title_screen.selected_option == "Leaderboard":
                            # Implement functionality here
                            self.start_game = True

            self.title_screen.screen.fill((40, 40, 40))
            self.title_screen.draw_menu()
            pygame.display.update()
            self.title_screen.clock.tick(30)
