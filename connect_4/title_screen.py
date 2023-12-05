"""This is the title screen when the game is runned"""

import pygame
import connect_4.rgbcolors


class TitleScreen:
    """Sets up the Scene of the game"""

    def __init__(self):

        self.width, self.height = 700, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect 4 AI Royale")
        self.clock = pygame.time.Clock()
        self.start_game = False
        self.selected_option = None

    def draw_button(self, button_info, font):
        """Draws a button with optional hover effect."""
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = button_info["rect"].collidepoint(mouse_pos)

        button_color = (
            button_info["hover_color"] if is_hovered else button_info["base_color"]
        )
        pygame.draw.rect(self.screen, button_color, button_info["rect"])

        text_surface = font.render(button_info["text"], True, connect_4.rgbcolors.white)
        text_width, text_height = text_surface.get_size()
        text_pos = (
            button_info["rect"].x + (button_info["rect"].width - text_width) / 2,
            button_info["rect"].y + (button_info["rect"].height - text_height) / 2,
        )
        self.screen.blit(text_surface, text_pos)

    def draw_menu(self):
        """This takes care of drawing the buttons and text on the screen."""

        font = pygame.font.Font(None, 36)
        title_text = font.render("Connect 4 Royale", True, connect_4.rgbcolors.white)

        # Get title dimensions
        title_width = title_text.get_width()

        # Button data
        buttons = [
            {
                "rect": pygame.Rect((self.width / 2 - 100, self.height / 2), (200, 50)),
                "text": "Leaderboard",
                "base_color": (63, 81, 181),
                "hover_color": (33, 150, 243),
            },
            {
                "rect": pygame.Rect(
                    (self.width / 2 - 100, self.height / 2 + 60), (200, 50)
                ),
                "text": "Player Vs Monte",
                "base_color": (63, 81, 181),
                "hover_color": (33, 150, 243),
            },
            {
                "rect": pygame.Rect(
                    (self.width / 2 - 100, self.height / 2 + 120), (200, 50)
                ),
                "text": "Player vs Alpha",
                "base_color": (63, 81, 181),
                "hover_color": (33, 150, 243),
            },
        ]

        # Draw buttons
        for button_info in buttons:
            self.draw_button(button_info, font)

        # Add the title on the screen
        title_pos = (self.width / 2 - title_width / 2, self.height / 4)
        self.screen.blit(title_text, title_pos)

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
