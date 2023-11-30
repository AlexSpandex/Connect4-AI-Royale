"""The board for connect 4"""

import pygame
import sys


class Board:
    """Sets up the board for the game"""
    
    def __init__(self):
        
        pygame.init()
        
        self.width, self.height = 800, 600
        self.screen = pygame. display.set_mode((self.width, self.height))