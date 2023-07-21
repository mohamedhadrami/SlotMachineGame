import pygame as pg
from pygame.locals import *
from pygame_assets.Button import Button
import cache_mgm

CACHE_PATH = "./cache/"

def get_cached_data() -> list:
    data = cache_mgm.check_cache()
    return list(data.keys())

def cache_games_menu(screen: pg.display, 
              fps: int, 
              font: pg.font.Font) -> None:
    #button1 = Button((5, 5), (100, 100), (0,255,0), "GO 1")
    #button2 = Button((215, 5), (100, 100), (0,255,0), "Quit")

    clock = pg.time.Clock()
    running = True

    screen.fill((225, 225, 225))
    i = 0  
    for game in get_cached_data():
        print(game)
        text = font.render(game, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.bottomleft = (50, 100 + i)
        screen.blit(text, text_rect)
        i += 50

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            '''
            if button1.is_clicked(event):
                return "stage2"
            if button2.is_clicked(event):
                pg.quit()
                exit()
            '''
        pg.display.flip()

        clock.tick(fps)