"""This is the title screen when the game is runned"""

import pygame
import sys
from connect_4.player import PlayerGame
import connect_4.rgbcolors


class TitleScreen:
    """Sets up the Scene of the game"""

    def __init__(self):
        
        pygame.init()

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect 4 AI Royale")
        self.clock = pygame.time.Clock()
        self.start_game = False
        self.selected_option = None

    def draw_menu(self):
        """This takes care of drawing the buttons and text on the screen"""

        font = pygame.font.Font(None, 36)
        title_text = font.render("Connect 4 Royale", True, connect_4.rgbcolors.white)

        # get title dimensions
        title_width, title_height = title_text.get_size()

        # creating button foudations
        leaderboard_button = pygame.Rect(
            (self.width / 2 - 100, self.height / 2), (200, 50)
        )
        ai_vs_ai_button = pygame.Rect(
            (self.width / 2 - 100, self.height / 2 + 60), (200, 50)
        )
        player_vs_ai_button = pygame.Rect(
            (self.width / 2 - 100, self.height / 2 + 120), (200, 50)
        )

        # creating the text for the buttons
        leaderboard_text = font.render("Leaderboard", True, connect_4.rgbcolors.white)
        ai_vs_ai_text = font.render("AI vs AI", True, connect_4.rgbcolors.white)
        player_vs_ai_text = font.render("Player vs AI", True, connect_4.rgbcolors.white)

        # Get text dimensions
        leader_width, leader_height = leaderboard_text.get_size()
        ai_width, ai_height = ai_vs_ai_text.get_size()
        player_width, player_height = player_vs_ai_text.get_size()

        # Get mouse position
        MOUSE_POS = pygame.mouse.get_pos()

        # drawing the buttons on screen
        pygame.draw.rect(self.screen, (63, 81, 181), leaderboard_button)
        pygame.draw.rect(self.screen, (63, 81, 181), ai_vs_ai_button)
        pygame.draw.rect(self.screen, (63, 81, 181), player_vs_ai_button)

        # adds the title on the screen
        self.screen.blit(
            title_text, (self.width / 2 - title_width / 2, self.height / 4)
        )

        # drawing the buttons on screen with hover effect
        for button, text, text_pos in zip(
            [leaderboard_button, ai_vs_ai_button, player_vs_ai_button],
            [leaderboard_text, ai_vs_ai_text, player_vs_ai_text],
            [
                (
                    self.width / 2 - leader_width / 2,
                    self.height / 2 + (50 - leader_height) / 2,
                ),
                (
                    self.width / 2 - ai_width / 2,
                    self.height / 2 + 60 + (50 - ai_height) / 2,
                ),
                (
                    self.width / 2 - player_width / 2,
                    self.height / 2 + 120 + (50 - player_height) / 2,
                ),
            ],
        ):
            # Check if the mouse is over the button
            is_hovered = button.collidepoint(MOUSE_POS)

            # Draw the button with hover effect
            button_color = (63, 81, 181) if not is_hovered else (33, 150, 243)
            pygame.draw.rect(self.screen, button_color, button)

            # Draw the text
            self.screen.blit(text, text_pos)

    def handle_button_event(self, mouse_pos):
        """This handles the events when buttons are being pressed"""
        leaderboard_button = pygame.Rect(
            (self.width / 2 - 100, self.height / 2), (200, 50)
        )
        ai_vs_ai_button = pygame.Rect(
            (self.width / 2 - 100, self.height / 2 + 60), (200, 50)
        )
        player_vs_ai_button = pygame.Rect(
            (self.width / 2 - 100, self.height / 2 + 120), (200, 50)
        )
        
        if leaderboard_button.collidepoint(mouse_pos):
            self.selected_option = "Leaderboard"
            print("Leaderboard button pressed")
        elif ai_vs_ai_button.collidepoint(mouse_pos):
            self.selected_option = "AI vs AI"
            print("AI vs AI button pressed")
        elif player_vs_ai_button.collidepoint(mouse_pos):
            self.selected_option = "Player vs AI"
            print("Player vs AI button pressed")