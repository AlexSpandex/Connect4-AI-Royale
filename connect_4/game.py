import pygame
import sys
from connect_4.title_screen import *
from connect_4.sounds import *
from connect_4.board import *

class Game:

    pygame.init()

    def run():
        # Main loop
        # play music
        Sounds.start()
        running = True
        while running:
            # Clear the screen
            screen.fill(BACKGROUND_COLOR)
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # Draw title at the top of the screen
            draw_text("Connect 4 AI Royale", WIDTH / 2, HEIGHT / 4)

            # Draw buttons middle of the screen
            draw_button("Leaderboard", WIDTH / 2 - 100, HEIGHT / 2, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR, leaderboard_action)
            draw_button("AI vs AI", WIDTH / 2 - 100, HEIGHT / 2 + 60, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR, ai_vs_ai_action)
            draw_button("Player vs AI", WIDTH / 2 - 100, HEIGHT / 2 + 120, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR, player_vs_ai_action)
            PLAYER = draw_button("Player vs Player", WIDTH / 2 - 100, HEIGHT / 2 + 180, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR, players_vs_player_action)
            # Draw sound button at the top right
            sound_button_width = 200
            sound_button_height = 50
            sound_button_x = WIDTH - sound_button_width - 20
            sound_button_y = 20
            SOUND_BUTTON = draw_button("Sound", sound_button_x, sound_button_y, sound_button_width, sound_button_height, BUTTON_COLOR, BUTTON_HOVER_COLOR, sound_action)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAYER:
                        players_vs_player_action()
                        Play()

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            pygame.time.Clock().tick(FPS)
