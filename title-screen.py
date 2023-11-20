# Title Screen

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 30

# Modern Colors
BACKGROUND_COLOR = (40, 40, 40)
BUTTON_COLOR = (63, 81, 181)
BUTTON_HOVER_COLOR = (33, 150, 243)
TEXT_COLOR = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4 AI Royale")

# Font
font = pygame.font.Font(None, 36)

# Function to draw text on the screen
def draw_text(text, x, y, color=TEXT_COLOR):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to create modern buttons
def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    draw_text(text, x + width / 2, y + height / 2, color=TEXT_COLOR)

# Function for leaderboard action
def leaderboard_action():
    print("Leaderboard button clicked")

# Function for AI vs AI action
def ai_vs_ai_action():
    print("AI vs AI button clicked")

# Function for Player vs AI action
def player_vs_ai_action():
    print("Player vs AI button clicked")

# Function for sound action
def sound_action():
    # Add sound-related actions here
    print("Sound button clicked")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw title at the top of the screen
    draw_text("Connect 4 AI Royale", WIDTH / 2, HEIGHT / 4)

    # Draw buttons middle of the screen
    draw_button("Leaderboard", WIDTH / 2 - 100, HEIGHT / 2, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR, leaderboard_action)
    draw_button("AI vs AI", WIDTH / 2 - 100, HEIGHT / 2 + 60, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR, ai_vs_ai_action)
    draw_button("Player vs AI", WIDTH / 2 - 100, HEIGHT / 2 + 120, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR, player_vs_ai_action)

    # Draw sound button at the top right
    sound_button_width = 200
    sound_button_height = 50
    sound_button_x = WIDTH - sound_button_width - 20
    sound_button_y = 20
    draw_button("Sound", sound_button_x, sound_button_y, sound_button_width, sound_button_height, BUTTON_COLOR, BUTTON_HOVER_COLOR, sound_action)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
