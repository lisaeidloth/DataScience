import pygame as pg
import random


class Duck(pg.sprite.Sprite):

    speed = 5
    images = []
    screen = 0

    def __init__(self, screen_rect):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.screen = screen_rect
        self.rect = self.image.get_rect(midtop=(random.random() * self.screen.width, 0))

    def update(self):
        """called every time around the game loop.
        Every frame we move the sprite 'rect' down.
        Delete on bottom.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= self.screen.height:
            self.kill()
