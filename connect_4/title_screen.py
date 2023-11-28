"""Title Screen"""

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
    
def players_vs_player_action():
    print("Player vs Player button clicked")
    
# Function for sound action
def sound_action():
    # Add sound-related actions here
    print("Sound button clicked")
    
