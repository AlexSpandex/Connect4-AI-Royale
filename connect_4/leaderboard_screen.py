import pygame
import sys

BACKGROUND_COLOR = (31, 31, 31)  # Dark background
TITLE_COLOR = (255, 255, 255)  # White text
STATS_COLOR = (173, 216, 230)  # Light blue text


pygame.init()
# Create a 700x700 window
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Connect 4 Leaderboard")

# Define fonts
font_title = pygame.font.Font(pygame.font.get_default_font(), 48)
font_stats = pygame.font.Font(None, 32)

# Initialize player stats
player_wins = 0
player_losses = 0
player_draws = 0

# Initialize AI stats
monte_carlo_wins = 0
monte_carlo_losses = 0
monte_carlo_draws = 0

alpha_beta_wins = 0
alpha_beta_losses = 0
alpha_beta_draws = 0

# Function to draw the leaderboard
def draw_leaderboard():
    screen.fill(BACKGROUND_COLOR)

    # Title
    title_text = font_title.render("Connect 4 Leaderboard", True, TITLE_COLOR)
    title_rect = title_text.get_rect(center=(350, 50))
    screen.blit(title_text, title_rect)

    # Player Stats
    player_stats_text = font_stats.render("Player", True, STATS_COLOR)
    screen.blit(player_stats_text, (50, 150))

    player_wins_text = font_stats.render(f"Wins: {player_wins}", True, STATS_COLOR)
    player_losses_text = font_stats.render(f"Losses: {player_losses}", True, STATS_COLOR)
    player_draws_text = font_stats.render(f"Draws: {player_draws}", True, STATS_COLOR)

    screen.blit(player_wins_text, (50, 200))
    screen.blit(player_losses_text, (50, 250))
    screen.blit(player_draws_text, (50, 300))

    # Monte Carlo AI Stats
    monte_carlo_stats_text = font_stats.render("Monte Carlo AI", True, STATS_COLOR)
    screen.blit(monte_carlo_stats_text, (300, 150))

    monte_carlo_wins_text = font_stats.render(f"Wins: {monte_carlo_wins}", True, STATS_COLOR)
    monte_carlo_losses_text = font_stats.render(f"Losses: {monte_carlo_losses}", True, STATS_COLOR)
    monte_carlo_draws_text = font_stats.render(f"Draws: {monte_carlo_draws}", True, STATS_COLOR)

    screen.blit(monte_carlo_wins_text, (300, 200))
    screen.blit(monte_carlo_losses_text, (300, 250))
    screen.blit(monte_carlo_draws_text, (300, 300))

    # Alpha-Beta AI Stats
    alpha_beta_stats_text = font_stats.render("Alpha-Beta AI", True, STATS_COLOR)
    screen.blit(alpha_beta_stats_text, (550, 150))

    alpha_beta_wins_text = font_stats.render(f"Wins: {alpha_beta_wins}", True, STATS_COLOR)
    alpha_beta_losses_text = font_stats.render(f"Losses: {alpha_beta_losses}", True, STATS_COLOR)
    alpha_beta_draws_text = font_stats.render(f"Draws: {alpha_beta_draws}", True, STATS_COLOR)

    screen.blit(alpha_beta_wins_text, (550, 200))
    screen.blit(alpha_beta_losses_text, (550, 250))
    screen.blit(alpha_beta_draws_text, (550, 300))

    pygame.display.flip()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update and draw the leaderboard
    draw_leaderboard()
