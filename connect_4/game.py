"""Main logic to run the game"""

import pygame
import sys
from connect_4.title_screen import TitleScreen
from connect_4.sounds import Sounds
# from connect_4.player import PlayerGame
from connect_4.playervsmonte import PlayerAIGame
from connect_4.playervsalpha import PlayerAlpha
import connect_4.rgbcolors


class Game:
    """Makes the game run"""

    def __init__(self):
        pygame.init()

        self.selected_option = None
        self.title_screen = TitleScreen()
        # self.player_game = PlayerGame(self.title_screen.screen)
        self.player_vs_ai_game = PlayerAIGame(self.title_screen.screen)
        self.player_vs_alpha_game = PlayerAlpha(self.title_screen.screen)

    def run(self):
        """Main loop"""

        # plays the music when game starts
        Sounds.title_music()

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
                            self.player_vs_ai_game.run()

                        elif self.title_screen.selected_option == "Player vs AI":
                            # self.player_game.run()
                            self.player_vs_alpha_game.run()

                        elif self.title_screen.selected_option == "Leaderboard":
                            # Implement functionality here
                            pass

            self.title_screen.screen.fill(connect_4.rgbcolors.grey16)
            self.title_screen.draw_menu()
            pygame.display.update()
            self.title_screen.clock.tick(30)
