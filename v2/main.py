import pygame as pg
from pygame.locals import *
from pygame_assets.Button import Button
from menu_screen import main_menu
from load_game import cache_games_menu
from game import game_view

WIDTH = 800
HEIGHT = 600
FPS = 5

def initialize_display(screen):
    pass

def handle_event(screen):
    pass

def active_view(screen: pg.display, gameIsRunning: bool, identifier: str, font: pg.font.Font) -> None:

    while gameIsRunning:
        if identifier == "main_menu":
            identifier = main_menu(screen, fps=FPS, font=font)
        elif identifier == "cached_games":
            identifier = cache_games_menu(screen, fps=FPS, font=font)
        elif identifier == "game":
            identifier = game_view(screen)



if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Slot Machine Game")
    initial_identifier = "main_menu"
    running = True
    font = pg.font.Font('freesansbold.ttf', 16)
    active_view(screen, running, initial_identifier, font)