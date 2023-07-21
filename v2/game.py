
import pygame as pg
from pygame.locals import *
from pygame_assets.Button import Button
from Board import Board

def game_view(screen: pg.display, 
              fps: int, 
              font: pg.font.Font) -> None:
    cached_games = Button((5, 5), 
                          (100, 50), 
                          (0,255,0), 
                          "See cached games")
    #button2 = Button((215, 5), (100, 100), (0,255,0), "Quit")

    clock = pg.time.Clock()
    running = True

    screen.fill((225, 225, 225))
    cached_games.draw(screen)

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            if cached_games.is_clicked(event):
                return "cached_games"
            '''
            if button2.is_clicked(event):
                pg.quit()
                exit()
            '''
        pg.display.flip()

        clock.tick(fps)