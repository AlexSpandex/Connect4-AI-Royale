"""Runs the sounds that are being played"""

import os.path
import pygame


class Sounds:
    """Sets up the sounds"""

    # define main and data directories for music files
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "Music")

    # plays music
    @staticmethod
    def title_music():
        """Starts the menu screen music"""
        try:
            # load and play the title music
            pygame.mixer.music.load("connect_4/music/title_2.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(0, 0.0, 500)

        except pygame.error as pygame_error:
            # handle errors loading music
            print(f'Cannot open {"title_2.mp3"}')
            raise SystemExit(1) from pygame_error

    @staticmethod
    def game_music():
        """Plays the game music"""
        try:
            # load and play the game music
            pygame.mixer.music.load("connect_4/music/endless_fight.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, 0.0, 500)

        except pygame.error as pygame_error:
            # handle errors loading music
            print(f'Cannot open {"endless_fight.mp3"}')
            raise SystemExit(1) from pygame_error

    @staticmethod
    def battle_music():
        """Plays the battle music ai vs ai"""
        try:
            # load and play the battle music
            pygame.mixer.music.load("connect_4/music/hard_revenge.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, 0.0, 500)

        except pygame.error as pygame_error:
            # handle errors loading music
            print(f'Cannot open {"hard_revenge.mp3"}')
            raise SystemExit(1) from pygame_error

    # plays music
    @staticmethod
    def leaderboard_music():
        """Starts the menu screen music"""
        try:
            # load and play the title music
            pygame.mixer.music.load("connect_4/music/departure.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(0, 0.0, 500)

        except pygame.error as pygame_error:
            # handle errors loading music
            print(f'Cannot open {"departure.mp3"}')
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
        try:
            # load and play the ending music
            # (placeholder file name)
            pygame.mixer.music.load("")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1, 0.0, 500)

        except pygame.error as pygame_error:
            # handle errors loading music
            print(f'Cannot open {"TheWickedWild.mp3"}')
            raise SystemExit(1) from pygame_error
