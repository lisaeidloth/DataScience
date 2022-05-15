import pygame as pg


class Time(pg.sprite.Sprite):

    def __init__(self, screen_rect):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.font = pg.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = "red"
        self.value = 0.0
        self.update()
        self.rect = self.image.get_rect(bottomleft=screen_rect.bottomleft)

    def update(self):
        msg = "Time: %d" % self.value
        self.image = self.font.render(msg, True, self.color)
