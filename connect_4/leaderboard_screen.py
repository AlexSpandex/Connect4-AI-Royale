"""this is the leaderbaord screen file"""

import sys
import pygame
from connect_4.sounds import Sounds
from connect_4.leaderboard_data import LeaderboardData
import connect_4.rgbcolors


class LeaderBoardScreen:
    """Sets up the leader board screen for the game"""

    def __init__(self, screen):
        """
        initialize the LeaderBoardScreen instance.

        Parameters:
        - screen (pygame.Surface): the pygame screen for rendering.
        """
        pygame.init()
        self.leaderboard_data = LeaderboardData()
        self.screen = screen

        # Define fonts
        self.font_title = pygame.font.Font(pygame.font.get_default_font(), 48)
        self.font_stats = pygame.font.Font(None, 32)

        # Initialize player stats
        self.player_wins = 0
        self.player_losses = 0

        # Initialize AI(ALPHA) stats
        self.monte_carlo_wins = 0
        self.monte_carlo_losses = 0

        # Initialize AI(MONTE) stats
        self.alpha_beta_wins = 0
        self.alpha_beta_losses = 0

    def update_player_stats(self):
        """
        update and render player stats on the screen
        """
        # Player Stats
        player_stats_text = self.font_stats.render(
            "Player", True, connect_4.rgbcolors.light_blue
        )
        self.screen.blit(player_stats_text, (50, 150))

        player_wins_text = self.font_stats.render(
            f"Wins: {self.player_wins}", True, connect_4.rgbcolors.green
        )
        player_losses_text = self.font_stats.render(
            f"Losses: {self.player_losses}", True, connect_4.rgbcolors.red
        )

        self.screen.blit(player_wins_text, (50, 200))
        self.screen.blit(player_losses_text, (50, 250))

    def update_monte_carlo_stats(self):
        """
        update and render monte carlo stats on the screen
        """
        # Monte Carlo AI Stats
        monte_carlo_stats_text = self.font_stats.render(
            "Monte Carlo AI", True, connect_4.rgbcolors.light_blue
        )
        self.screen.blit(monte_carlo_stats_text, (300, 150))

        monte_carlo_wins_text = self.font_stats.render(
            f"Wins: {self.monte_carlo_wins}", True, connect_4.rgbcolors.green
        )
        monte_carlo_losses_text = self.font_stats.render(
            f"Losses: {self.monte_carlo_losses}", True, connect_4.rgbcolors.red
        )

        self.screen.blit(monte_carlo_wins_text, (300, 200))
        self.screen.blit(monte_carlo_losses_text, (300, 250))

    def update_alpha_beta_stats(self):
        """
        update and render alpha beta stats on the screen
        """
        # Alpha-Beta AI Stats
        alpha_beta_stats_text = self.font_stats.render(
            "Alpha-Beta AI", True, connect_4.rgbcolors.light_blue
        )
        self.screen.blit(alpha_beta_stats_text, (550, 150))

        alpha_beta_wins_text = self.font_stats.render(
            f"Wins: {self.alpha_beta_wins}", True, connect_4.rgbcolors.green
        )
        alpha_beta_losses_text = self.font_stats.render(
            f"Losses: {self.alpha_beta_losses}", True, connect_4.rgbcolors.red
        )

        self.screen.blit(alpha_beta_wins_text, (550, 200))
        self.screen.blit(alpha_beta_losses_text, (550, 250))

    def draw_leaderboard(self):
        """
        draw the leaderboard on the screen
        """
        self.screen.fill(connect_4.rgbcolors.grey16)

        # Title for the leaderboard screen
        title_text = self.font_title.render(
            "Connect 4 Leaderboard", True, connect_4.rgbcolors.white
        )
        # setting the location of the title to be in the middle
        title_rect = title_text.get_rect(center=(350, 50))
        self.screen.blit(title_text, title_rect)

        # Player Stats
        self.update_player_stats()

        # Monte Carlo AI Stats
        self.update_monte_carlo_stats()

        # Alpha-Beta AI Stats
        self.update_alpha_beta_stats()

        pygame.display.flip()

    def run(self):
        """handles the leaderboard screen"""
        # initialize game sounds
        Sounds.stop()
        Sounds.leaderboard_music()

        # Main game loop
        while True:
            for event in pygame.event.get():
                if (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ) or event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    print("Space button pressed leaveing leaderboard...")
                    Sounds.stop()
                    Sounds.title_music()
                    return

            # Update player stats from leaderboard data
            self.player_wins = self.leaderboard_data.data.get("Player 1", {}).get(
                "wins", 0
            )
            self.player_losses = self.leaderboard_data.data.get("Player 1", {}).get(
                "losses", 0
            )

            # Update Monte Carlo AI stats from leaderboard data
            self.monte_carlo_wins = self.leaderboard_data.data.get(
                "MonteCarlo", {}
            ).get("wins", 0)
            self.monte_carlo_losses = self.leaderboard_data.data.get(
                "MonteCarlo", {}
            ).get("losses", 0)

            # Update Alpha-Beta AI stats from leaderboard data
            self.alpha_beta_wins = self.leaderboard_data.data.get("AlphaBeta", {}).get(
                "wins", 0
            )
            self.alpha_beta_losses = self.leaderboard_data.data.get(
                "AlphaBeta", {}
            ).get("losses", 0)

            self.draw_leaderboard()
            pygame.display.update()
