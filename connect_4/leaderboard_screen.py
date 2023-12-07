import pygame
import sys
from connect_4.sounds import Sounds
from connect_4.leaderboard_data import LeaderboardData
from connect_4.title_screen import TitleScreen


class LeaderBoardScreen:
    def __init__(self):
        pygame.init()
        self.leaderboard_data = LeaderboardData()
        self.title_screen = TitleScreen()
        # Define fonts
        self.font_title = pygame.font.Font(pygame.font.get_default_font(), 48)
        self.font_stats = pygame.font.Font(None, 32)

        # Initialize player stats
        self.player_wins = 0
        self.player_losses = 0
        self.player_draws = 0

        # Initialize AI stats
        self.monte_carlo_wins = 0
        self.monte_carlo_losses = 0
        self.monte_carlo_draws = 0

        self.alpha_beta_wins = 0
        self.alpha_beta_losses = 0
        self.alpha_beta_draws = 0

        self.BACKGROUND_COLOR = (31, 31, 31)  # Dark background
        self.TITLE_COLOR = (255, 255, 255)  # White text
        self.STATS_COLOR = (173, 216, 230)  # Light blue text

        self.screen = pygame.display.set_mode((700, 700))

    # Function to draw the leaderboard
    def draw_leaderboard(self):
        self.screen.fill(self.BACKGROUND_COLOR)

        # Title
        title_text = self.font_title.render(
            "Connect 4 Leaderboard", True, self.TITLE_COLOR
        )
        title_rect = title_text.get_rect(center=(350, 50))
        self.screen.blit(title_text, title_rect)

        # Player Stats
        player_stats_text = self.font_stats.render("Player", True, self.STATS_COLOR)
        self.screen.blit(player_stats_text, (50, 150))

        player_wins_text = self.font_stats.render(
            f"Wins: {self.player_wins}", True, self.STATS_COLOR
        )
        player_losses_text = self.font_stats.render(
            f"Losses: {self.player_losses}", True, self.STATS_COLOR
        )
        player_draws_text = self.font_stats.render(
            f"Draws: {self.player_draws}", True, self.STATS_COLOR
        )

        self.screen.blit(player_wins_text, (50, 200))
        self.screen.blit(player_losses_text, (50, 250))
        self.screen.blit(player_draws_text, (50, 300))

        # Monte Carlo AI Stats
        monte_carlo_stats_text = self.font_stats.render(
            "Monte Carlo AI", True, self.STATS_COLOR
        )
        self.screen.blit(monte_carlo_stats_text, (300, 150))

        monte_carlo_wins_text = self.font_stats.render(
            f"Wins: {self.monte_carlo_wins}", True, self.STATS_COLOR
        )
        monte_carlo_losses_text = self.font_stats.render(
            f"Losses: {self.monte_carlo_losses}", True, self.STATS_COLOR
        )
        monte_carlo_draws_text = self.font_stats.render(
            f"Draws: {self.monte_carlo_draws}", True, self.STATS_COLOR
        )

        self.screen.blit(monte_carlo_wins_text, (300, 200))
        self.screen.blit(monte_carlo_losses_text, (300, 250))
        self.screen.blit(monte_carlo_draws_text, (300, 300))

        # Alpha-Beta AI Stats
        alpha_beta_stats_text = self.font_stats.render(
            "Alpha-Beta AI", True, self.STATS_COLOR
        )
        self.screen.blit(alpha_beta_stats_text, (550, 150))

        alpha_beta_wins_text = self.font_stats.render(
            f"Wins: {self.alpha_beta_wins}", True, self.STATS_COLOR
        )
        alpha_beta_losses_text = self.font_stats.render(
            f"Losses: {self.alpha_beta_losses}", True, self.STATS_COLOR
        )
        alpha_beta_draws_text = self.font_stats.render(
            f"Draws: {self.alpha_beta_draws}", True, self.STATS_COLOR
        )

        self.screen.blit(alpha_beta_wins_text, (550, 200))
        self.screen.blit(alpha_beta_losses_text, (550, 250))
        self.screen.blit(alpha_beta_draws_text, (550, 300))

        pygame.display.flip()

    def run(self):
        
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

            self.draw_leaderboard()
            pygame.display.update()
