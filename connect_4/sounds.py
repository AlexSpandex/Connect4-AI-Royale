import pygame

class Sounds:

    pygame.init()

    # plays music
    def start():
        """Starts the music"""
        if True:
            try:
                pygame.mixer.music.load("connect_4/music/Sabor-Fresa.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1, 0.0, 500)
            except pygame.error as pygame_error:
                print(f'Cannot open {"vibes.mp3"}')
                raise SystemExit(1) from pygame_error
            
    # stops the music
    def stop():
        """Stops the music"""
        pygame.mixer.fadeout(500)
        pygame.mixer.music.stop()

    # end screen music
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