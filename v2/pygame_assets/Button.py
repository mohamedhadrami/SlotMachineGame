import pygame as pg

class Button(object):

    def __init__(self, position, size, color, font, text):

        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = pg.Rect((0,0), size)

        self.font = font
        text = self.font.render(text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)