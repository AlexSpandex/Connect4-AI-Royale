"""Runs the sounds that are being played"""

import pygame


class Sounds:
    pygame.init()

    # plays music
    @staticmethod
    def title_music():
        """Starts the menu screen music"""
        
        if True:
            try:
                pygame.mixer.music.load("connect_4/music/title_2.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(0, 0.0, 500)
                
            except pygame.error as pygame_error:
                print(f'Cannot open {"title_2.mp3"}')
                raise SystemExit(1) from pygame_error
            
    @staticmethod
    def game_music():
        if True:
            try:
                pygame.mixer.music.load("connect_4/music/endless_fight.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1, 0.0, 500)
                
            except pygame.error as pygame_error:
                print(f'Cannot open {"endless_fight.mp3"}')
                raise SystemExit(1) from pygame_error
            
    @staticmethod
    def battle_music():
        if True:
            try:
                pygame.mixer.music.load("connect_4/music/hard_revenge.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1, 0.0, 500)
                
            except pygame.error as pygame_error:
                print(f'Cannot open {"hard_revenge.mp3"}')
                raise SystemExit(1) from pygame_error
            
    # stops the music
    @staticmethod
    def stop():
        """Stops the music"""
        
        pygame.mixer.fadeout(500)
        pygame.mixer.music.stop()

    # end screen music
    @staticmethod
    def end_music():
        """ending music"""
        
        if True:
            try:
                pygame.mixer.music.load("")
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1, 0.0, 500)
            except pygame.error as pygame_error:
                print(f'Cannot open {"TheWickedWild.mp3"}')
                raise SystemExit(1) from pygame_error
